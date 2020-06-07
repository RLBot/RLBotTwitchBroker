
def highlight_player_name(player: 'PlayerInfo') -> str:
    team_class = 'blue' if player.team == 0 else 'orange'
    return f'<span class="player-name {team_class}">{player.name}</span>'
