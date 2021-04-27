import settlerEnv
from netVars import NetVars


class GameObservation:
    def __init__(self,
                 settler_env: settlerEnv.SettlerEnv
                 ):
        net_vars = NetVars.instance()
        local_player = net_vars.local_player
        local_player_beds = net_vars.local_player_beds

        self.local_player = settler_env.read_int(local_player)
        self.local_player_beds = settler_env.read_int(local_player_beds)

        print("[GameObservation] local_player: %d" % self.local_player)
        print("[GameObservation] local_player_beds: %d" % self.local_player_beds)
