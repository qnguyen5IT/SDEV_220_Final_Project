class PlayerData:
    GAME_OVER:bool = False
    PLAYER_WON:bool = False

    BEST_SCORE:int = 0
    CURRENT_SCORE:int = 0

    def reset_player_game_state():
        if PlayerData.CURRENT_SCORE > PlayerData.BEST_SCORE:
            PlayerData.BEST_SCORE = PlayerData.CURRENT_SCORE

        PlayerData.GAME_OVER = False
        PlayerData.PLAYER_WON = False
        PlayerData.CURRENT_SCORE = 0