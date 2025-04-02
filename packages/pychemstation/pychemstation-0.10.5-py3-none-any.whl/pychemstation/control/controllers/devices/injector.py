from ....control.controllers import CommunicationController
from ....utils.injector_types import (
    Draw,
    Inject,
    InjectorFunction,
    InjectorTable,
    Mode,
    Remote,
    RemoteCommand,
    SourceType,
    Wait,
)
from ....utils.macro import Response
from ....utils.table_types import RegisterFlag, Table
from ....utils.tray_types import Tray
from .device import DeviceController


class InjectorController(DeviceController):
    def __init__(
        self, controller: CommunicationController, table: Table, offline: bool
    ):
        super().__init__(controller, table, offline)

    def get_row(self, row: int) -> InjectorFunction:
        def return_tray_loc() -> Tray:
            raise NotImplementedError
            # unit = self.get_text(row, RegisterFlag.DRAW_LOCATION_UNIT)
            # tray = self.get_text(row, RegisterFlag.DRAW_LOCATION_TRAY)
            # x = self.get_text(row, RegisterFlag.DRAW_LOCATION_ROW)
            # y = self.get_text(row, RegisterFlag.DRAW_LOCATION_COLUMN)
            # return FiftyFourVialPlate.from_str("P1-A1")

        function = self.get_text(row, RegisterFlag.FUNCTION)
        if function == "Wait":
            return Wait(duration=self.get_num(row, RegisterFlag.TIME))
        elif function == "Inject":
            return Inject()
        elif function == "Draw":
            # TODO: better error handling
            is_source = SourceType(self.get_text(row, RegisterFlag.DRAW_SOURCE))
            is_volume = Mode(self.get_text(row, RegisterFlag.DRAW_VOLUME))
            vol = (
                self.get_num(row, RegisterFlag.DRAW_VOLUME_VALUE)
                if is_volume == Mode.SET
                else None
            )
            if is_source is SourceType.SPECIFIC_LOCATION:
                return Draw(amount=vol, source=return_tray_loc())
            elif is_source is SourceType.LOCATION:
                return Draw(
                    amount=vol, location=self.get_text(row, RegisterFlag.DRAW_LOCATION)
                )
        elif function == "Remote":
            return Remote(
                command=RemoteCommand(self.get_text(row, RegisterFlag.REMOTE)),
                duration=int(self.get_num(row, RegisterFlag.REMOTE_DUR)),
            )
        raise ValueError("No valid function found.")

    def load(self) -> InjectorTable:
        rows = self.get_num_rows()
        if rows.is_ok():
            row_response = rows.value
            if isinstance(row_response, Response):
                return InjectorTable(
                    functions=[
                        self.get_row(i) for i in range(int(row_response.num_response))
                    ]
                )
        elif rows.is_err():
            return InjectorTable(functions=[])
        raise ValueError("Unexpected error")
