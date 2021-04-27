import pymem

# Class for holding the settlerEnv

import observations


class SettlerEnv:
    def __init__(self, process: pymem.Pymem):
        self.process = process
        self.base_address: int = process.base_address
        self.player_position = process.read_int(self.base_address + 0xE9482C)
        print("player_position: %s" % self.player_position)

    def get_observations(self):
        return observations.Observations(self)

    def read_int(self, offset, player_offset=0, param=0):
        return self.process.read_int(self.base_address + offset + player_offset + param)


if __name__ == "__main__":
    settlerEnv = SettlerEnv(pymem.Pymem("S4_Main.exe"))
    settlerEnv.get_observations()
