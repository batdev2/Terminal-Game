class rockPapersScrissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.winning = {
            "rock": "scissors",
            "scissors": "paper",
            "paper": "rock"
        }
        self.stats = {
            "wins": 0,
            "losses": 0, 
            "ties": 0
        }

    