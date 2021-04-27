from singleton import Singleton


@Singleton
class NetVars:
    resource_offset = 0xDAD97C
    settler_offset = 0xDACF60
    player_diff = 0x1128
    player_count = 0xE94828
    local_player = 0xE9482C
    local_player_beds = 0xDAAD54

    def get_player_offset(self, player_position: int):
        return (player_position - 1) * self.player_diff
