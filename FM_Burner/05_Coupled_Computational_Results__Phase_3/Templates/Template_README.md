
### Contributor
Name: 

Institution: 
Short-Institution-Name: 

Country: 

------------------

### Test case

FM-burner: ethylene flame

------------------

### CFD package
Code: OpenFOAM

Solver: FireFOAM

Version: v2006

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

Temperature: X K

Pressure: 101325 Pa

Velocity: 0 m/s

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
- 300

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

### Discretization methods
Time: Backward

CFL: maximum 0.7

Advection: 

Momentum: Gauss linear

scalars: Gauss limitedLinear 0.1

Diffusion:  Gaussian scheme (Gauss linear corrected)

Pressure-velocity coupling

PIMPLE:

inner correction iterations: 2

non-orthogonal correction iterations: 1

outer iterations: 3

------------------

### Computational Cost (hh:mm:ss)

Wall clock time:

coarse:8 h

medium: 60 h

fine: 150 h



Simulation time:

For all grids: 0-30s

Number of CPUs (MPI Processes):

40 CPUs for all grids

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

