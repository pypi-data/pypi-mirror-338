from typing import Any

import torch

from torch_sim.integrators import (
    MDState,
    batched_initialize_momenta,
    npt_langevin,
    nve,
    nvt_langevin,
)
from torch_sim.models.lennard_jones import LennardJonesModel
from torch_sim.quantities import calc_kT
from torch_sim.state import SimState, concatenate_states
from torch_sim.units import MetalUnits


def batched_initialize_momenta_loop(
    positions: torch.Tensor,  # shape: (n_batches, n_atoms_per_batch, 3)
    masses: torch.Tensor,  # shape: (n_batches, n_atoms_per_batch)
    kT: torch.Tensor,  # shape: (n_batches,)
    seeds: torch.Tensor,  # shape: (n_batches,)
    device: torch.device,
    dtype: torch.dtype,
) -> torch.Tensor:
    """Initialize momenta for batched molecular dynamics.

    Args:
        positions: Tensor of atomic positions with shape
            (n_batches, n_atoms_per_batch, 3).
        masses: Tensor of atomic masses with shape
            (n_batches, n_atoms_per_batch).
        kT: Tensor of temperature values in energy units for
            each batch with shape (n_batches,).
        seeds: Tensor of random seeds for each batch with shape (n_batches,).
        device: The device on which to allocate the tensors (e.g., 'cpu' or 'cuda').
        dtype: The data type of the tensors (e.g., torch.float32).

    Returns:
        momenta: Tensor of initialized momenta with shape
            (n_batches, n_atoms_per_batch, 3).
    """
    n_batches = positions.shape[0]
    n_atoms_per_batch = positions.shape[1]

    # Initialize momenta tensor
    momenta = torch.zeros((n_batches, n_atoms_per_batch, 3), dtype=dtype)

    # Create a generator for each batch using the provided seeds
    generators = [torch.Generator(device=device).manual_seed(int(seed)) for seed in seeds]

    # Generate random momenta for each batch
    for batch_idx in range(n_batches):
        # Generate random velocities from normal distribution
        batch_momenta = torch.randn(
            (n_atoms_per_batch, 3), dtype=dtype, generator=generators[batch_idx]
        )

        # Scale by sqrt(mass * kT)
        mass_factors = torch.sqrt(masses[batch_idx]).unsqueeze(-1)
        kT_factor = torch.sqrt(kT[batch_idx])
        batch_momenta *= mass_factors * kT_factor

        # Remove center of mass motion if more than one atom
        if n_atoms_per_batch > 1:
            mean_momentum = torch.mean(batch_momenta, dim=0, keepdim=True)
            batch_momenta = batch_momenta - mean_momentum

        momenta[batch_idx] = batch_momenta

    return momenta


def test_batched_initialize_momenta_loop():
    from torch_sim.unbatched.unbatched_integrators import initialize_momenta

    # Set random seed for reproducibility
    seed = 42

    device = torch.device("cpu")
    dtype = torch.float64

    n_batches = 3
    n_atoms_per_batch = 4

    # Create test inputs
    positions = torch.randn(n_batches, n_atoms_per_batch, 3, dtype=dtype)
    masses = torch.rand(n_batches, n_atoms_per_batch, dtype=dtype) + 0.5
    kT = torch.tensor([0.1, 0.2, 0.3], dtype=dtype)
    seeds = torch.arange(seed, seed + n_batches, dtype=torch.int64)

    # Run non-batched version first
    unbatched_momenta = []
    for batch_idx in range(n_batches):
        state = MDState(
            positions=positions[batch_idx],
            momenta=torch.zeros_like(positions[batch_idx]),
            masses=masses[batch_idx],
            forces=torch.zeros_like(positions[batch_idx]),
            energy=torch.zeros(1, dtype=dtype),
            atomic_numbers=torch.ones(n_atoms_per_batch, dtype=torch.int64),
            cell=torch.eye(3, dtype=dtype),
            pbc=False,
        )
        state = initialize_momenta(
            state, kT[batch_idx], device, dtype, seed=int(seeds[batch_idx])
        )
        unbatched_momenta.append(state.momenta)

    unbatched_momenta = torch.stack(unbatched_momenta)

    # Run batched version
    batched_momenta = batched_initialize_momenta_loop(
        positions=positions,
        masses=masses,
        kT=kT,
        seeds=seeds,  # seeds before device and dtype
        device=device,
        dtype=dtype,
    )

    assert torch.allclose(batched_momenta, unbatched_momenta, rtol=1e-6)


def test_batched_initialize_momenta():
    from torch_sim.unbatched.unbatched_integrators import initialize_momenta

    seed = 42
    device = torch.device("cpu")
    dtype = torch.float64

    n_batches = 3
    n_atoms_per_batch = 4

    # Create test inputs
    positions = torch.randn(n_batches, n_atoms_per_batch, 3, dtype=dtype)
    masses = torch.rand(n_batches, n_atoms_per_batch, dtype=dtype) + 0.5
    kT = torch.tensor([0.1, 0.2, 0.3], dtype=dtype)
    seeds = torch.arange(seed, seed + n_batches, dtype=torch.int64)

    # Run non-batched version first
    unbatched_momenta = []
    for batch_idx in range(n_batches):
        # Use corresponding seed for each batch

        state = MDState(
            positions=positions[batch_idx],
            momenta=torch.zeros_like(positions[batch_idx]),
            masses=masses[batch_idx],
            forces=torch.zeros_like(positions[batch_idx]),
            energy=torch.zeros(1, dtype=dtype),
            atomic_numbers=torch.ones(n_atoms_per_batch, dtype=torch.int64),
            cell=torch.eye(3, dtype=dtype),
            pbc=False,
        )
        state = initialize_momenta(
            state, kT[batch_idx], device, dtype, seed=int(seeds[batch_idx])
        )
        unbatched_momenta.append(state.momenta)

    unbatched_momenta = torch.stack(unbatched_momenta)

    # Run batched version
    batched_momenta = batched_initialize_momenta(
        positions, masses, kT, seeds, device, dtype
    )

    assert torch.allclose(batched_momenta, unbatched_momenta, rtol=1e-6)

    # Verify center of mass momentum is zero for each batch
    for batch_idx in range(n_batches):
        com_momentum = torch.mean(batched_momenta[batch_idx], dim=0)
        assert torch.allclose(com_momentum, torch.zeros(3, dtype=dtype), atol=1e-10)


def test_npt_langevin(ar_double_sim_state: SimState, lj_model: LennardJonesModel):
    dtype = torch.float64
    n_steps = 200
    dt = torch.tensor(0.001, dtype=dtype)
    kT = torch.tensor(100.0, dtype=dtype) * MetalUnits.temperature
    external_pressure = torch.tensor(0.0, dtype=dtype) * MetalUnits.pressure

    # Initialize integrator
    init_fn, update_fn = npt_langevin(
        model=lj_model,
        dt=dt,
        kT=kT,
        external_pressure=external_pressure,
        alpha=40 * dt,
    )

    # Run dynamics for several steps
    state = init_fn(state=ar_double_sim_state, seed=42)
    energies = []
    temperatures = []
    for _step in range(n_steps):
        state = update_fn(state=state)

        # Calculate instantaneous temperature from kinetic energy
        temp = calc_kT(state.momenta, state.masses, batch=state.batch)
        energies.append(state.energy)
        temperatures.append(temp / MetalUnits.temperature)

    # Convert temperatures list to tensor
    temperatures_tensor = torch.stack(temperatures)
    temperatures_list = [t.tolist() for t in temperatures_tensor.T]

    energies_tensor = torch.stack(energies)
    energies_list = [t.tolist() for t in energies_tensor.T]

    # Basic sanity checks
    assert len(energies_list[0]) == n_steps
    assert len(temperatures_list[0]) == n_steps

    # Check temperature is roughly maintained for each trajectory
    mean_temps = torch.mean(temperatures_tensor, dim=0)  # Mean temp for each trajectory
    for mean_temp in mean_temps:
        assert (
            abs(mean_temp - kT.item() / MetalUnits.temperature) < 150.0
        )  # Allow for thermal fluctuations

    # Check energy is stable for each trajectory
    for traj in energies_list:
        energy_std = torch.tensor(traj).std()
        assert energy_std < 1.0  # Adjust threshold as needed

    # Check positions and momenta have correct shapes
    n_atoms = 8

    # Verify the two systems remain distinct
    pos_diff = torch.norm(
        state.positions[:n_atoms].mean(0) - state.positions[n_atoms:].mean(0)
    )
    assert pos_diff > 0.0001  # Systems should remain separated


def test_nvt_langevin(ar_double_sim_state: SimState, lj_model: LennardJonesModel):
    dtype = torch.float64
    n_steps = 100
    dt = torch.tensor(0.001, dtype=dtype)
    kT = torch.tensor(100.0, dtype=dtype) * MetalUnits.temperature

    # Initialize integrator
    init_fn, update_fn = nvt_langevin(
        model=lj_model,
        dt=dt,
        kT=kT,
    )

    # Run dynamics for several steps
    state = init_fn(state=ar_double_sim_state, seed=42)
    energies = []
    temperatures = []
    for _step in range(n_steps):
        state = update_fn(state=state)

        # Calculate instantaneous temperature from kinetic energy
        temp = calc_kT(state.momenta, state.masses, batch=state.batch)
        energies.append(state.energy)
        temperatures.append(temp / MetalUnits.temperature)

    # Convert temperatures list to tensor
    temperatures_tensor = torch.stack(temperatures)
    temperatures_list = [t.tolist() for t in temperatures_tensor.T]

    energies_tensor = torch.stack(energies)
    energies_list = [t.tolist() for t in energies_tensor.T]

    # Basic sanity checks
    assert len(energies_list[0]) == n_steps
    assert len(temperatures_list[0]) == n_steps

    # Check temperature is roughly maintained for each trajectory
    mean_temps = torch.mean(temperatures_tensor, dim=0)  # Mean temp for each trajectory
    for mean_temp in mean_temps:
        assert (
            abs(mean_temp - kT.item() / MetalUnits.temperature) < 150.0
        )  # Allow for thermal fluctuations

    # Check energy is stable for each trajectory
    for traj in energies_list:
        energy_std = torch.tensor(traj).std()
        assert energy_std < 1.0  # Adjust threshold as needed

    # Check positions and momenta have correct shapes
    n_atoms = 8

    # Verify the two systems remain distinct
    pos_diff = torch.norm(
        state.positions[:n_atoms].mean(0) - state.positions[n_atoms:].mean(0)
    )
    assert pos_diff > 0.0001  # Systems should remain separated


def test_nve(ar_double_sim_state: SimState, lj_model: LennardJonesModel):
    dtype = torch.float64
    n_steps = 100
    dt = torch.tensor(0.001, dtype=dtype)
    kT = torch.tensor(100.0, dtype=dtype) * MetalUnits.temperature

    # Initialize integrator
    nve_init, nve_update = nve(model=lj_model, dt=dt, kT=kT)
    state = nve_init(state=ar_double_sim_state, seed=42)

    # Run dynamics for several steps
    energies = []
    for _step in range(n_steps):
        state = nve_update(state=state, dt=dt)

        energies.append(state.energy)

    energies_tensor = torch.stack(energies)

    # assert conservation of energy
    assert torch.allclose(energies_tensor[:, 0], energies_tensor[0, 0], atol=1e-4)
    assert torch.allclose(energies_tensor[:, 1], energies_tensor[0, 1], atol=1e-4)


def test_compare_single_vs_batched_integrators(
    ar_sim_state: SimState, lj_model: Any
) -> None:
    """Test that single and batched integrators give the same results."""
    initial_states = {
        "single": ar_sim_state,
        "batched": concatenate_states([ar_sim_state, ar_sim_state]),
    }

    final_states = {}
    for state_name, state in initial_states.items():
        # Initialize integrator
        kT = torch.tensor(100.0) * MetalUnits.temperature
        dt = torch.tensor(0.001)  # Small timestep for stability

        nve_init, nve_update = nve(model=lj_model, dt=dt, kT=kT)
        state = nve_init(state=state, seed=42)
        state.momenta = torch.zeros_like(state.momenta)

        for _step in range(100):
            state = nve_update(state=state, dt=dt)

        final_states[state_name] = state

    # Check energy conservation
    ar_single_state = final_states["single"]
    ar_batched_state_0 = final_states["batched"][0]
    ar_batched_state_1 = final_states["batched"][1]

    for final_state in [ar_batched_state_0, ar_batched_state_1]:
        assert torch.allclose(ar_single_state.positions, final_state.positions)
        assert torch.allclose(ar_single_state.momenta, final_state.momenta)
        assert torch.allclose(ar_single_state.forces, final_state.forces)
        assert torch.allclose(ar_single_state.masses, final_state.masses)
        assert torch.allclose(ar_single_state.cell, final_state.cell)
