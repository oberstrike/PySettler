import settlerEnv
from utils.good import Good
from utils.netVars import NetVars


class GoodObservation:
    def __init__(self,
                 settler_env: settlerEnv.SettlerEnv,
                 player_position: int
                 ):
        print("[resourceObservation] player_position %d" % player_position)
        net_vars = NetVars.instance()
        player_offset = net_vars.get_player_offset(player_position)
        resource_offset = net_vars.resource_offset

        self.goods = [settler_env.read_int(resource_offset, player_offset, 0x04 * good.value)
                      for good in Good]

    def get_good(self, good: Good):
        return self.goods[good.value]
