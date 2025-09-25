# 3D-Spring-Collision-Simulation-with-Two-Spheres-VPython
This simulation models the interaction of two spheres connected by a spring in 3D space using VPython. It visualizes their motion, velocity, momentum, and energy (kinetic, potential, and total mechanical) as they collide and exchange energy via the spring.

## Features
- 3D visualization of **two spheres with trails**.
- Interactive real-time graphs for:
  1. **Velocity** vs. time for both spheres
  2. **Individual momentum** (x & y) vs. time
  3. **Total system momentum** vs. time
  4. **Ball total energy** (KE, PE, ME) vs. time
  5. **Rock total energy** (KE, PE, ME) vs. time
- Calculates **initial and final system kinetic energy and momentum**.
- Spring interactions computed only when the spheres are within the spring’s equilibrium distance.

## Equations Used

**Momentum:**  
`p = m * v`  

**Velocity from Momentum:**  
`v = p / m`  

**Kinetic Energy (KE):**  
`KE = |p|^2 / (2 * m)`  

**Spring Potential Energy (PE):**  
`U_spring = 1/2 * k * L^2`  

**Spring Force:**  
`F = -k * L * R_hat`  
- `L` = displacement from equilibrium  
- `R_hat` = unit vector along line connecting spheres  

**Total Mechanical Energy (ME):**  
`ME = KE + PE`  

## Simulation Setup

- **Spheres:**
  - Ball: mass = 1 kg, radius = 0.05 m, initial velocity = 1 m/s (x-direction)
  - Rock: mass = 0.5 kg, radius = 0.05 m, initial velocity = -0.5 m/s (x-direction)
- **Spring:**
  - Equilibrium length = 1 m
  - Spring constant = 15 N/m
- **Ground:** flat green plane
- **Time step:** `dt = 0.005 s`

## How It Works

1. **Initialization**
   - Define constants (mass, spring properties, initial velocities).
   - Create VPython `sphere` objects with trails.
   - Initialize momentum, kinetic energy, and spring potential energy.
   - Print initial total kinetic energy and system momentum.

2. **Time Evolution (Loop)**
   - Update spring force if spheres are closer than equilibrium distance.
   - Update momentum and compute new velocity:  
     `p = p + F * dt`  
     `v = p / m`
   - Update positions: `pos = pos + v * dt`
   - Calculate kinetic energy: `KE = |p|^2 / (2 * m)`
   - Calculate spring potential energy: `PE = 1/2 * k * L^2`
   - Update total mechanical energy: `ME = KE + PE`
   - Update all graphs for velocity, momentum, and energy.

3. **Completion**
   - Loop continues until both spheres leave the simulation bounds.
   - Print final total kinetic energy and system momentum.
