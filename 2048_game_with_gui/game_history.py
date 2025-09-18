import uuid
import json
import records

from datetime import datetime

def generate_report(count_up, count_down, count_left, count_right, status, max_value_on_gameboard):
    game_identifier = str(uuid.uuid4())
    date_of_game = datetime.now().strftime("%d.%m.%Y %H:%M")
    total_moves = count_up + count_down + count_left + count_right

    data = {
        "game_identifier": game_identifier,
        "date_of_game": date_of_game,
        "total_moves": total_moves,
        "left_moves": count_left,
        "right_moves": count_right,
        "up_moves": count_up,
        "down_moves": count_down,
        "game_result": status,
        "highest_number": max_value_on_gameboard
    }

    records.update_records(game_identifier, count_up, count_down, count_left, count_right, max_value_on_gameboard)

    with open(f"2048_game_with_gui/games/{game_identifier}.json", "w") as file:
        json.dump(data, file, indent=4)
        file.close()