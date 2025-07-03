
### Contributor
Name: 

Institution: 
Short-Institution-Name (Iname): 

Country: 

------------------

### Test case

NIST Pool Fire: Methanol

------------------

### CFD package
Code: 

Solver: 

Version: 

------------------

### Resolution

#### Computational domain discretization (flow solver)

Domain: 
- 


The coarse grid: x cm

The medium grid: x cm

The fine grid: x cm

Cell type: hexahedra

Comments:
- 


------------------

### Initial conditions

Temperature (K): 

Pressure (Pa): 101325 

Velocity (m/s): 

Comments:
- 

------------------

### Boundary conditions

Side boundaries: adiabatic wall 

Fuel inlet: 

Oxidizer inlet (bottom): 

Top Boundary: Open 

Comments:
- 

------------------

### Radiation Models (include parameters)

RTE solver: 
- FVM/FAM, DOM, MC, etc.


Angular space discretization (radiation solver)
- Number of solid angles: 160

Radiative properties model (gaseous species): 
- RADCAL, Planck Mean, WSGG, etc.

Radiative Fraction:
- not set

Solver frequency (every x time step):
- 10

Path length (m):
- 0.1

Radiation temperature (K):
- 800

Turbulence-Radiation-Interaction (TRI): 
- none

Comments:
- 


------------------

### General Models 
Turbulence model: 
- 

Combustion model: 
- 

Soot model: 
- 

Turbulence-soot interaction (TSI) model: 
- 

Comments:
- 

------------------

### Discretization methods and schemes
Time: Backward

CFL: maximum 0.7

Advection: 

Momentum: 

scalars: 

Diffusion:  

Pressure-velocity coupling

- PIMPLE:

- Inner correction iterations: 

- Non-orthogonal correction iterations: 

- outer iterations: 

------------------

### Computational Cost (hh:mm:ss)

Wall clock time (h):

- coarse:

- medium: 

- fine: 


Simulation time (s):

- For all grids: 0-30s

Number of CPUs (MPI Processes):

- 40 CPUs for all grids

CPU cost (Number of CPUs * Wall clock time / Simulation time / Total cells):

coarse: 0.27

medium: 0.48

fine: 0.55

------------------

### Averaging period

5-30 s

------------------

### Special issues/problems

------------------

### Relevant publications

