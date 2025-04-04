from __future__ import annotations

from abc import ABC

from ....control.controllers import CommunicationController
from ....utils.table_types import Table
from .table import ABCTableController


class DeviceController(ABCTableController, ABC):
    def __init__(
        self, controller: CommunicationController, table: Table, offline: bool
    ):
        super().__init__(controller=controller, table=table)
        self.offline = offline

    def __new__(cls, *args, **kwargs):
        if cls is ABCTableController:
            raise TypeError(f"only children of '{cls.__name__}' may be instantiated")
        return object.__new__(cls)
