import settlerEnv
from netVars import NetVars


class ResourceObservation:
    def __init__(self,
                 settler_env: settlerEnv.SettlerEnv,
                 player_position: int
                 ):
        print("[resourceObservation] player_position %d" % player_position)
        process = settler_env.process
        net_vars = NetVars.instance()
        player_offset = net_vars.get_player_offset(player_position)
        resource_offset = net_vars.resource_offset

        self.wood = process.read_int(process.base_address + resource_offset + player_offset)
        self.stone = process.read_int(process.base_address + resource_offset + player_offset + (0x04 * 25))