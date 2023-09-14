# Overview

The general idea to evaluate the settings and compare FDS and OpenFOAM data with the PMC-LBL benchmark is basically The process i


# Further information

## FDS 

### Needed Revision
To be able to run FDS with the relevant input data via CSVF files one needs a quite new FDS installation. The minimum revision is:
```
 Revision         : FDS-6.8.0-138-g51097e3-nightly
```

### Possible Issues
Running FDS for this case leads sometimes to an error like having `too many open files`.
This could be circumvent by typing 
```
ulimit -n 4096
```
before the calculation step (the number needs to be below the hard limit which can be check with `ulimit -Hn`).
