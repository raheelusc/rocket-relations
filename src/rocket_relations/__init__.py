"""
rocket_relations
================

This package provides functions for ideal rocket flow analysis, including
calculating characteristic velocity (c*) and thrust coefficient (C_f)
for choked nozzles.

Modules
-------

- **ideal**: Functions for ideal nozzle performance.
"""

from .ideal import solve_cstar, solve_cf

__all__ = ["solve_cstar", "solve_cf"]