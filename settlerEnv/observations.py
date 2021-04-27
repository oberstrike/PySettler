from netVars import NetVars
from settlerObservation import SettlerObservation
from resourceObservation import ResourceObservation
from gameObservation import  GameObservation
import settlerEnv


class Observations:
    def __init__(self, settler_env: settlerEnv.SettlerEnv):
        net_vars = NetVars.instance()
        player_count = settler_env.process.read_int(settler_env.base_address + net_vars.player_count)
        print("player_count: %s" % player_count)

        self.settlerObservations = [SettlerObservation(settler_env, player + 1) for player
                                    in range(player_count)]
        self.resourceObservations = [ResourceObservation(settler_env, player + 1) for player
                                     in range(player_count)]
        self.gameObservations = GameObservation(settler_env)
        print(self.settlerObservations)

    def as_tuple(self):
        return self.player_position, self.wood, self.stone
