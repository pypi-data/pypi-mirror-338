"""
Module to provide API for the communication with Agilent HPLC systems.

HPLCController sends commands to Chemstation software via a command file.
Answers are received via reply file. On the Chemstation side, a custom
Macro monitors the command file, executes commands and writes to the reply file.
Each command is given a number (cmd_no) to keep track of which commands have
been processed.

Authors: Alexander Hammer, Hessam Mehr, Lucy Hao
"""

import time
from typing import Optional, Union

from result import Err, Ok, Result

from ...utils.macro import (
    str_to_status,
    HPLCErrorStatus,
    Command,
    Status,
)
from ...utils.mocking.abc_comm import ABCCommunicationController


class CommunicationController(ABCCommunicationController):
    """
    Class that communicates with Agilent using Macros
    """

    def __init__(
        self,
        comm_dir: str,
        cmd_file: str = "cmd",
        reply_file: str = "reply",
        offline: bool = False,
        debug: bool = False,
    ):
        """
        :param comm_dir:
        :param cmd_file: Name of command file
        :param reply_file: Name of reply file
        :param debug: whether to save log of sent commands
        """
        super().__init__(comm_dir, cmd_file, reply_file, offline, debug)

    def get_num_val(self, cmd: str) -> Union[int, float]:
        tries = 10
        for _ in range(tries):
            self.send(Command.GET_NUM_VAL_CMD.value.format(cmd=cmd))
            res = self.receive()
            if res.is_ok():
                return res.ok_value.num_response
        raise RuntimeError("Failed to get number.")

    def get_text_val(self, cmd: str) -> str:
        tries = 10
        for _ in range(tries):
            self.send(Command.GET_TEXT_VAL_CMD.value.format(cmd=cmd))
            res = self.receive()
            if res.is_ok():
                return res.ok_value.string_response
        raise RuntimeError("Failed to get string")

    def get_status(self) -> Status:
        """Get device status(es).

        :return: list of ChemStation's current status
        """
        self.send(Command.GET_STATUS_CMD)
        time.sleep(1)

        try:
            res = self.receive()
            if res.is_err():
                return HPLCErrorStatus.NORESPONSE
            if res.is_ok():
                parsed_response = self.receive().value.string_response
                self._most_recent_hplc_status = str_to_status(parsed_response)
                return self._most_recent_hplc_status
            else:
                raise RuntimeError("Failed to get status")
        except IOError:
            return HPLCErrorStatus.NORESPONSE
        except IndexError:
            return HPLCErrorStatus.MALFORMED

    def _send(self, cmd: str, cmd_no: int, num_attempts=5) -> None:
        """Low-level execution primitive. Sends a command string to HPLC.

        :param cmd: string to be sent to HPLC
        :param cmd_no: Command number
        :param num_attempts: Number of attempts to send the command before raising exception.
        :raises IOError: Could not write to command file.
        """
        err = None
        for _ in range(num_attempts):
            time.sleep(1)
            try:
                with open(self.cmd_file, "w", encoding="utf8") as cmd_file:
                    cmd_file.write(f"{cmd_no} {cmd}")
            except IOError as e:
                err = e
                continue
            else:
                return
        else:
            raise IOError(f"Failed to send command #{cmd_no}: {cmd}.") from err

    def _receive(self, cmd_no: int, num_attempts=100) -> Result[str, str]:
        """Low-level execution primitive. Recives a response from HPLC.

        :param cmd_no: Command number
        :param num_attempts: Number of retries to open reply file
        :raises IOError: Could not read reply file.
        :return: Potential ChemStation response
        """
        err: Optional[Union[OSError, IndexError, ValueError]] = None
        err_msg = ""
        for _ in range(num_attempts):
            time.sleep(1)

            try:
                with open(self.reply_file, "r", encoding="utf_16") as reply_file:
                    response = reply_file.read()
            except OSError as e:
                err = e
                continue

            try:
                first_line = response.splitlines()[0]
                try:
                    response_no = int(first_line.split()[0])
                except ValueError as e:
                    err = e
                    err_msg = f"Caused by {first_line}"
            except IndexError as e:
                err = e
                continue

            # check that response corresponds to sent command
            if response_no == cmd_no:
                return Ok(response)
            else:
                continue
        else:
            return Err(
                f"Failed to receive reply to command #{cmd_no} due to {err} caused by {err_msg}."
            )
