"""Tests for evohome-async - validate the schemas of vendor's RESTful JSON."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from evohomeasync2.schemas import (
    TCC_GET_USR_ACCOUNT,
    TCC_GET_USR_LOCATIONS,
    factory_loc_status,
)

from .common import assert_schema
from .conftest import FIXTURES_V2

if TYPE_CHECKING:
    import pytest


def pytest_generate_tests(metafunc: pytest.Metafunc) -> None:
    def id_fnc(folder_path: Path) -> str:
        return folder_path.name

    folders = [
        p
        for p in Path(FIXTURES_V2).glob("*")
        if p.is_dir() and not p.name.startswith("_")
    ]
    metafunc.parametrize("folder", sorted(folders), ids=id_fnc)


def test_user_account(folder: Path) -> None:
    """Test the user account schema against the corresponding JSON."""

    assert_schema(folder, TCC_GET_USR_ACCOUNT, "user_account.json")


def test_user_locations(folder: Path) -> None:
    """Test the user locations config schema against the corresponding JSON."""

    assert_schema(folder, TCC_GET_USR_LOCATIONS, "user_locations.json")


def test_location_status(folder: Path) -> None:
    """Test the location status schema against the corresponding JSON."""

    SCH_STATUS = factory_loc_status()

    for p in Path(folder).glob("status_*.json"):
        assert_schema(folder, SCH_STATUS, p.name)
