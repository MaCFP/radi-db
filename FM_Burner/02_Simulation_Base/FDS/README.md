
# Description of Base Data


## Simulation setup 
FDS-version 

General settings


## Mapping Procedure 
As stated, the initial simulation was done with FDS. To get these
simulation data to OpenFOAM and also into a CSVF readable FDS format
some post-processing steps were needed.  This was mainly done with the
`fireANALYSIS` tool which basically converts FDS to other common data
formats. In this case, the relevant format is CSV. There are slight
differences between the raw csv formats for the mapping to OpenFOAM
and back to FDS-CSVF.

The csv data is imported to OpenFOAM with a specially adjusted
pre-processing tool. The mesh itself is prepared before with exactly
the same cell distribution as the underlining FDS mesh.


## Results - Comparison with Data

## Selection of snapshots
### General

Ideally, the selection of the snapshots should be done by preserving
different moments (e.g. mean,...) compared to original data set.

-   This will potentially lead to many snapshots

Here, we agreed to select about 40 snapshots for the evaluation with
LBL-PMC method

-   The selection is done by selecting a time difference of $\SI{5}{\s}
     $ between each snapshots
-   So the selection is kind of predefined before the simulation
-   A selection based on `extreme snapshots` to include the complete
    range of outcome would only be possible when writing out each time
    step (which is seen as an option for the moment)

### Selection of Snapshots

The next slides give some information about the actually selected
snapshots

-   **Only** a few monitor positions were investigated, so the following
    slides give just a reduced overview about the selected snapshots

### Snapshots - Flame Temperature

![Temperature at positon $r=\SI{0}{\m}$ and
$z=3.5 \cdot D$](img/Plots/Selection_Temp_Snapshots.vsz.png)

-   The selected snapshots demonstrate a good distribution for this
    monitor point.

### Plots - Flame Soot

![Soot volume fraction at positon $r=\SI{0}{\m}$ and
$z=1.0 \cdot D$](img/Plots/Selection_Soot_ts.vsz.png)

-   The selected snapshots demonstrate a good distribution for this
    monitor point.

### Plots - Wall/Center - Radiative Heat Flux

![Radiative heat flux positon $x=\SI{0.6}{\m}$ and
$z=\SI{0.5}{\m} $](img/Plots/Selectioin_RADFL_center_155.vsz.png)

-   The selected snapshots demonstrate a (good) distribution for this
    monitor point.

### Plots - Wall/Middle - Radiative Heat Flux

![Radiative heat flux positon $x=\SI{0.6}{\m}$ and
$z=\SI{0.1}{\m} $](img/Plots/Selection_radradfl_middle_x06y0z01.vsz.png)

-   The selected snapshots **do not include extreme values** for
    radiative heat flux at this point.


