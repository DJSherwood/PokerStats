class player:
    def __init__(self):
        self.shown = []
        self.hidden = []
        return self

    def receive_shown(self, card):
        self.shown.append(card)
        return

    def receive_hidden(self, card):
        self.hidden.append(card)
        return
