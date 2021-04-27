import pymem

# Class for holding the settlerEnv
from pymem.pattern import pattern_scan_module

import utils.observations


class SettlerEnv:
    def __init__(self, process: pymem.Pymem):
        self.process = process
        self.base_address: int = process.base_address
        self.player_position = process.read_int(self.base_address + 0xE9482C)
        self.module = pymem.process.module_from_name(process.process_handle, "S4_Main.exe")
        character_pattern = b".\x00\x00"
        pymem.pattern.pattern_scan_module(process.process_handle, self.module, character_pattern)

        print("player_position: %s" % self.player_position)

    def get_observations(self):
        return utils.observations.Observations(self)

    def read_int(self, offset, player_offset=0, param=0):
        return self.process.read_int(self.base_address + offset + player_offset + param)


if __name__ == "__main__":
    settlerEnv = SettlerEnv(pymem.Pymem("S4_Main.exe"))
    settlerEnv.get_observations()
