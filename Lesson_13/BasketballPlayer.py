class Player:
    def __init__(self, first_name, last_name, height_cm, weight_kg):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg


class BasketballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, points, rebounds, assists):
        self.points = points
        self.rebounds = rebounds
        self.assists = assists

    class FootballPlayer(Player):
        def __init__(self, first_name, last_name, height_cm, weight_kg, goals, yellow_cards, red_cards):
            self.goals = goals
            self.yellow_cards = yellow_cards
            self.red_cards = red_cards
