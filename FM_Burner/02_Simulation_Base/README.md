# Overview
Initial and mapped setups are listed in this directory.

`FDS`: 
  - initial FDS simulation with setup and csv simulation results
  - binary files are not available in this folder
  
`OPF_mapped_snapshots`
  - all the mapped field files are available in a release with compressed openfoam files; please click here to download the relevant time steps.
  - Link to data files for the release with each snapshot: https://github.com/MaCFP/radi-db/releases/tag/FM_SimBase_v0.0.1



# Further information
## Naming conventions for fields

### Field Names

| Field           | Type                     | Field name for OPF |
|-----------------|--------------------------|--------------------|
| Nitrogen        | Mass fraction            | N2                 |
| Oxygen          | Mass fraction            | O2                 |
| Carbon dioxide  | Mass fraction            | CO2                |
| Carbon monoxide | Mass fraction            | CO                 |
| Ethylene        | Mass fraction            | C2H4               |
| Water Vapor     | Mass fraction            | H2O                |
| Soot            | Mass fraction            | Soot               |
| Nitrogen        | Volume fraction          | N2_vol             |
| Oxygen          | Volume fraction          | O2_vol             |
| Carbon dioxide  | Volume fraction          | CO2_vol            |
| Carbon monoxide | Volume fraction          | CO_vol             |
| Ethylene        | Volume fraction          | C2H4_vol           |
| Water Vapor     | Volume fraction          | H2O_vol            |
| Soot            | Volume fraction          | Soot_vol           |
| Soot            | Aerosol Volume fraction  | fvSoot             |
| Density         | (warning: dimensionless) | rho                |
| Temperature     | (Kelvin)                 |                    |

Comment: Pressure is not available in this list as it has minor impact
on the final results (this was checked for time step 15).

# Molar weights from FDS

ETHYLENE Gas Species Molecular Weight (g/mol) 28.05316

NITROGEN Gas Species Molecular Weight (g/mol) 28.01340

OXYGEN Gas Species Molecular Weight (g/mol) 31.99880

CARBON DIOXIDE Gas Species Molecular Weight (g/mol) 44.00950

WATER VAPOR Gas Species Molecular Weight (g/mol) 18.01528

CARBON MONOXIDE Gas Species Molecular Weight (g/mol) 28.01010

SOOT Gas Species Molecular Weight (g/mol) 10.91042
