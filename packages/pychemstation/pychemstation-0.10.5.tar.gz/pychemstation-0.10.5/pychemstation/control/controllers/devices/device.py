from __future__ import annotations

import abc
from typing import Union

from result import Err, Ok

from ....control.controllers import CommunicationController
from ....utils.macro import Command, Response
from ....utils.table_types import RegisterFlag, Table, TableOperation


class DeviceController(abc.ABC):
    def __init__(
        self, controller: CommunicationController, table: Table, offline: bool
    ):
        self.table_locator = table
        self.controller = controller
        self.offline = offline

    @abc.abstractmethod
    def get_row(self, row: int):
        pass

    def get_text(self, row: int, col_name: RegisterFlag) -> str:
        return self.controller.get_text_val(
            TableOperation.GET_ROW_TEXT.value.format(
                register=self.table_locator.register,
                table_name=self.table_locator.name,
                row=row,
                col_name=col_name.value,
            )
        )

    def get_num(self, row: int, col_name: RegisterFlag) -> Union[int, float]:
        return self.controller.get_num_val(
            TableOperation.GET_ROW_VAL.value.format(
                register=self.table_locator.register,
                table_name=self.table_locator.name,
                row=row,
                col_name=col_name.value,
            )
        )

    def get_num_rows(self) -> Ok[Response] | Err[str]:
        self.send(
            TableOperation.GET_NUM_ROWS.value.format(
                register=self.table_locator.register,
                table_name=self.table_locator.name,
                col_name=RegisterFlag.NUM_ROWS,
            )
        )
        self.send(
            Command.GET_ROWS_CMD.value.format(
                register=self.table_locator.register,
                table_name=self.table_locator.name,
                col_name=RegisterFlag.NUM_ROWS,
            )
        )
        res = self.controller.receive()

        if res.is_ok():
            self.send("Sleep 0.1")
            self.send("Print Rows")
            return res
        else:
            return Err("No rows could be read.")

    def send(self, cmd: Union[Command, str]):
        if not self.controller:
            raise RuntimeError(
                "Communication controller must be initialized before sending command. It is currently in offline mode."
            )
        self.controller.send(cmd)
