import numpy as np
import pytest
from rocket_relations.ideal import solve_cstar, solve_cf

# Example scalar test
def test_solve_cstar_scalar():
    gamma = 1.2
    Rs = 350
    T0 = 3500
    expected_cstar = 1706.6214
    result = solve_cstar(gamma, Rs, T0)
    assert np.isclose(result, expected_cstar, rtol=1e-7)

def test_solve_cf_scalar():
    gamma = 1.2
    ratio_pe_p0 = 0.0125
    ratio_pa_p0 = 0.02
    ratio_Ae_Astar = 10
    expected_cf = 1.5423079
    result = solve_cf(gamma, ratio_pe_p0, ratio_pa_p0, ratio_Ae_Astar)
    assert np.isclose(result, expected_cf, rtol=1e-7)

# Example exception test
def test_solve_cstar_invalid_gamma():
    with pytest.raises(ValueError):
        solve_cstar(0.9, 350, 3500)  # gamma < 1 should raise ValueError

def test_solve_cf_invalid_pressure_ratio():
    with pytest.raises(ValueError):
        solve_cf(1.2, 1.2, 0.02, 10)  # pe/p0 >= 1 should raise ValueError

# Optional: vectorized test with NumPy arrays
def test_solve_cstar_array():
    gamma = np.array([1.2, 1.3])
    Rs = np.array([350, 300])
    T0 = np.array([3500, 3200])
    result = solve_cstar(gamma, Rs, T0)
    assert result.shape == gamma.shape
