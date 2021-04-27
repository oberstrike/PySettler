import settlerEnv
from utils.netVars import NetVars
from utils.settler import Settler


class SettlerObservation:
    def __init__(self,
                 settler_env: settlerEnv.SettlerEnv,
                 player_position: int
                 ):
        net_vars = NetVars.instance()
        settler_offset = net_vars.settler_offset
        player_offset = net_vars.get_player_offset(player_position)
        self.settlers = [settler_env.read_int(settler_offset, player_offset, 0x04 * settler.value)
                         for settler in Settler]

    def get_settler(self, settler: Settler):
        return self.settlers[settler.value]
