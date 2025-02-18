import requests
import requests_cache
import random
class Pokemon:
    def __init__(self,name):
        self.name = name
        self.moves = []
        self.basestats = {}
        self.type = []
        self.base_url = 'https://pokeapi.co/api/v2/'
        self.currentstats = {}
        self.stat_stages = {'hp': 0, 'attack': 0, 'defense': 0, 'special-attack': 0, 'special-defense': 0, 'speed': 0}
        requests_cache.install_cache('poke_cache')
    def get_stats(self):
        add_url = f'pokemon/{self.name}'
        r = requests.get(self.base_url + add_url)
        r_json = r.json()
        for types in r_json['types']:
            self.type.append(types['type']['name'])
        for stat in r_json['stats']:
            self.basestats[stat['stat']['name']] = stat['base_stat']
        self.basestats['hp'] = round((((self.basestats['hp']*2)+110)/5)*2)
        self.currentstats = self.basestats
        for moves in r_json['moves']:
            self.moves.append(moves['move']['name'])
        randlist = random.sample(range(0,len(self.moves)),4)
        self.moves = [self.moves[randlist[0]],self.moves[randlist[1]],self.moves[randlist[2]],self.moves[randlist[3]]]
        print(self.moves)
        pass
    def get_move_stats(self):
        for i,move in enumerate(self.moves):
            add_url = f'move/{self.moves[i]}'
            move_json = requests.get(self.base_url + add_url).json()
            self.moves[i] = {'name' : move_json['name'],'power' : move_json['power'], 'accuracy' : move_json['accuracy'],'damage_class':move_json['damage_class']['name'],'crit' : move_json['meta']['crit_rate'], 'type' : move_json['type']['name'], 'stat_changes': move_json['stat_changes'],'target': move_json['target']['name']}
            print(self.moves[i])
        pass
    def stat_stage_apply(self):
        for stat in self.stat_stages.keys():
            if stat != 'hp':
                if self.stat_stages[stat] < 0:
                    self.currentstats[stat] = round(self.basestats[stat]*(2/((-self.stat_stages[stat])+2)))
                elif self.stat_stages[stat] > 0:
                    self.currentstats[stat] = round(self.basestats[stat]*((2+(self.stat_stages[stat]))/2))
