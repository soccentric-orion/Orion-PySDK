"""Tests for the ``acadia_sdk`` → ``orion_sdk`` deprecation shim.

The shim must emit a ``DeprecationWarning`` on import and re-export the full
public surface of :mod:`orion_sdk`. Each test re-imports ``acadia_sdk`` via
``importlib`` so the warning fires every time (an already-cached module would
not re-execute the top-level ``warnings.warn``).
"""
from __future__ import annotations

import importlib
import sys
import warnings

import orion_sdk

# The global ``filterwarnings = ["ignore::DeprecationWarning"]`` in pyproject
# swallows deprecation warnings elsewhere; ``pytest.warns`` overrides that
# filter for the matched context, so the shim's warning is observable here.
import pytest


def _fresh_import_acadia_sdk() -> "importlib.types.ModuleType":
    """Import ``acadia_sdk`` from scratch so its top-level warning re-fires."""
    sys.modules.pop("acadia_sdk", None)
    return importlib.import_module("acadia_sdk")


def test_import_warns_deprecation() -> None:
    with pytest.warns(DeprecationWarning, match="renamed to 'orion_sdk'"):
        mod = _fresh_import_acadia_sdk()
    assert mod is not None


def test_reexported_names_match_orion_sdk() -> None:
    with pytest.warns(DeprecationWarning):
        shim = _fresh_import_acadia_sdk()
    assert set(shim.__all__) == set(orion_sdk.__all__)
    # Every name in orion_sdk.__all__ is present on the shim module.
    for name in orion_sdk.__all__:
        assert hasattr(shim, name), f"shim missing re-exported name: {name!r}"
        # The re-exported object must be the very same object as in orion_sdk.
        assert getattr(shim, name) is getattr(orion_sdk, name), (
            f"shim.{name} is not orion_sdk.{name}"
        )


def test_shim_all_is_list_of_strings() -> None:
    with pytest.warns(DeprecationWarning):
        shim = _fresh_import_acadia_sdk()
    assert isinstance(shim.__all__, list)
    assert all(isinstance(n, str) for n in shim.__all__)


def test_orion_sdk_import_does_not_warn() -> None:
    """Importing the new name must NOT emit a DeprecationWarning.

    Re-importing the already-cached module would not re-trigger warnings
    anyway, so pop it first to exercise the top-level statement again.
    """
    sys.modules.pop("orion_sdk", None)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        importlib.import_module("orion_sdk")
    deprecations = [w for w in caught if issubclass(w.category, DeprecationWarning)]
    assert deprecations == [], (
        "importing 'orion_sdk' emitted an unexpected DeprecationWarning: "
        f"{[str(w.message) for w in deprecations]}"
    )