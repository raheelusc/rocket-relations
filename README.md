# rocket_relations

Computes ideal rocket performance parameters of characteristic velocity (c*) and thrust coefficient (CF), for given gas properties and nozzle conditions.

## Installation
Download the source code or clone the repo locally.
In the project root directory, open a terminal and create/activate
a fresh conda environment (or reuse an existing one):
```
bash
conda create -n rocketenv python=3.14
conda activate rocketenv
pip install -e .
```
## Quickstart
import rocket_relations as rr

```
c_star = rr.solve_cstar(gamma=1.2, Rs=350, T0=3500)
cf = rr.solve_cf(gamma=1.2, ratio_pe_p0=0.0125, ratio_pa_p0=0.02, ratio_Ae_Astar=10)

print(f"Characteristic velocity c*: {c_star:.4f} m/s")
print(f"Thrust coefficient CF: {cf:.7f}")
```

## Documentation
For detailed usage, see module and package docstrings:
help(rr)
help(rr.ideal.solve_cstar)
help(rr.ideal.solve_cf)

## Tests
Unit tests are located in the tests\ directory. To run all tests, install the pytest package into the environment with 
```mambda install pytest``` 
and run 
```pytest -q```
to run and review the test results.