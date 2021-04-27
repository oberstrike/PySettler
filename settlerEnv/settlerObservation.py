import settlerEnv
from netVars import NetVars


class SettlerObservation:
    def __init__(self,
                 settler_env: settlerEnv.SettlerEnv,
                 player_position: int
                 ):
        net_vars = NetVars.instance()
        settler_offset = net_vars.settler_offset
        player_offset = net_vars.get_player_offset(player_position)
        self.worker = settler_env.read_int(settler_offset, player_offset, 0x04 * 0)
