"""Tests for SMA operational risk capital calculations.

This module defines test cases for the :func:`compute_sma_operational_risk_capital`
function. The initial test forces the code to be red (fail) so that TDD
can drive the implementation. Additional test skeletons are marked as
xfail and should be completed as the functionality is implemented.
"""

from __future__ import annotations

import math
import pytest

from orm_engine.capital import compute_sma_operational_risk_capital


def test_sma_capital_basic_example() -> None:
    """A toy example to drive the first implementation.

    The expected capital value is illustrative only. Once the
    regulatory formula is known, replace this with a real expected value.
    """
    losses = [1_000_000, 2_000_000, 500_000, 0, 3_000_000]
    capital = compute_sma_operational_risk_capital(losses)
    # ensure the result is a finite float
    assert isinstance(capital, float)
    assert math.isfinite(capital)
    # this rounding assertion will fail until implemented
    assert round(capital, -3) == 2_000_000


@pytest.mark.xfail(reason="expected to be implemented: empty input")
def test_empty_returns_zero() -> None:
    """Empty lists should produce zero capital."""
    assert compute_sma_operational_risk_capital([]) == 0.0


@pytest.mark.xfail(reason="expected to be implemented: validation of negative values")
def test_invalid_inputs_raise() -> None:
    """Negative values should raise a ValueError."""
    with pytest.raises(ValueError):
        compute_sma_operational_risk_capital([-1.0, 2.0])