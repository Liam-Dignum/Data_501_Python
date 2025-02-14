class Pokemon:
    def __init__(self,name):
        self.name = name
        self.moves = []
        self.basestats = {}
        self.type = ''
        self.currentstats = self.basestats
    def get_stats(self,name):
        pass
