"""Module to represent a Netatmo schedule."""
from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import TYPE_CHECKING

from pyatmo.modules.base_class import NetatmoBase

if TYPE_CHECKING:
    from .home import NetatmoHome

LOG = logging.getLogger(__name__)


@dataclass
class NetatmoSchedule(NetatmoBase):
    """Class to represent a Netatmo schedule."""

    home: NetatmoHome
    selected: bool
    away_temp: float | None
    hg_temp: float | None

    def __init__(self, home: NetatmoHome, raw_data) -> None:
        super().__init__(raw_data)
        self.home = home
        self.selected = raw_data.get("selected", False)
        self.hg_temp = raw_data.get("hg_temp")
        self.away_temp = raw_data.get("away_temp")