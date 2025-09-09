"""Operational risk capital calculators.

This module defines functions for computing standardized measurement approach
(SMA) capital charges for operational risk. The current implementation
provides only a placeholder function to be fleshed out via test-driven
development (TDD). All functions in this module must be pure and
deterministic – they should not perform any I/O or rely on external state.
"""

from __future__ import annotations

from typing import Iterable


def compute_sma_operational_risk_capital(losses: Iterable[float]) -> float:
    """Compute the SMA operational risk capital charge.

    Parameters
    ----------
    losses : Iterable[float]
        A collection of historical loss amounts. The SMA capital formula uses
        a standardized loss component, typically the sum of positive loss
        amounts scaled by regulatory constants. Negative or non-numeric values
        are invalid and should result in an error.

    Returns
    -------
    float
        The computed capital charge. The value must be finite.

    Notes
    -----
    This placeholder implementation raises :class:`NotImplementedError`. The
    correct formula should be implemented via TDD based on regulatory
    requirements and business acceptance criteria.
    """
    raise NotImplementedError("Implement per tests.")