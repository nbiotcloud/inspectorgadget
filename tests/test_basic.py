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
    constant_c = 3.4
    assert inspectorgadget.getsize(("a", constant_c), blacklist=type(constant_c)) == 106
