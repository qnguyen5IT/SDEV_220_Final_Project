class PlayerData:
    GAME_OVER:bool = False
    PLAYER_WON:bool = False

    BEST_SCORE:int = 0
    CURRENT_SCORE:int = 0


    """ Checks to see if the player beat the high score. """
    def check_for_high_score():
        if PlayerData.CURRENT_SCORE > PlayerData.BEST_SCORE:
            PlayerData.BEST_SCORE = PlayerData.CURRENT_SCORE

    def reset_player_game_state():
        PlayerData.GAME_OVER = False
        PlayerData.PLAYER_WON = False
        PlayerData.CURRENT_SCORE = 0
