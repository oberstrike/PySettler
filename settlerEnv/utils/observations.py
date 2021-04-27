from utils.good import Good
from utils.settler import Settler
from utils.settlerObservation import SettlerObservation
from utils.goodObservation import GoodObservation
from utils.gameObservation import GameObservation
import settlerEnv
from utils.netVars import NetVars


class Observations:
    def __init__(self, settler_env: settlerEnv.SettlerEnv):
        net_vars = NetVars.instance()
        player_count = settler_env.process.read_int(settler_env.base_address + net_vars.player_count)
        print("player_count: %s" % player_count)

        self.settlerObservations = [SettlerObservation(settler_env, player + 1) for player
                                    in range(player_count)]
        self.goodObservations = [GoodObservation(settler_env, player + 1) for player
                                 in range(player_count)]
        self.gameObservations = GameObservation(settler_env)
        swords = self.settlerObservations[0].get_settler(Settler.SWORDSMAN_03)
        wood = self.goodObservations[0].get_good(Good.AXE)
        print("Swords: %d" % swords )
        print("Wood: %d" % wood)
        print(self.settlerObservations)

    def as_tuple(self):
        return self.player_position, self.wood, self.stone
