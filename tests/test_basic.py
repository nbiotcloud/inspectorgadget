"""Basic Testing."""

from math import pi

import inspectorgadget


def test_signature():
    """Signature Testing."""
    assert inspectorgadget.get_signature(mulc) == "mulc(factor_a, factor_b=3.141592653589793)"


def mulc(factor_a, factor_b=pi):
    """
    Return product of inputs.
    """
    return factor_a * factor_b


def test_size():
    """Size Testing."""
    assert inspectorgadget.getsize(("a", pi), blacklist=type(pi)) == 106
