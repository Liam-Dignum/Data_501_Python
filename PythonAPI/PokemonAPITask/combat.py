import random
from bdb import effective

from unicodedata import category


class Combat:
    def __init__(self,playerpokemon,aipokemom):
        self.playerpokemon = playerpokemon
        self.aipokemon = aipokemom
        self.select_target_list = ['selected-pokemon-me-first','selected-pokemon']
        self.self_target_list = ['user','ally','user-or-ally','user-and-allies','all-allies']
        self.enemy_target_list = ['random-opponent','all-other-pokemon','all-opponents']
        self.type_effectiveness = {
    "normal": {
        "effective": ["fighting"],
        "not_effective": ["ghost"]
    },
    "fire": {
        "effective": ["water", "ground", "rock"],
        "not_effective": ["fire", "grass", "ice", "bug", "steel", "fairy"]
    },
    "water": {
        "effective": ["electric", "grass"],
        "not_effective": ["fire", "water", "ice", "steel"]
    },
    "electric": {
        "effective": ["ground"],
        "not_effective": ["electric", "flying", "steel"]
    },
    "grass": {
        "effective": ["fire", "ice", "poison", "flying", "bug"],
        "not_effective": ["water", "electric", "grass", "ground"]
    },
    "ice": {
        "effective": ["fire", "fighting", "rock", "steel"],
        "not_effective": ["ice"]
    },
    "fighting": {
        "effective": ["flying", "psychic", "fairy"],
        "not_effective": ["bug", "rock", "dark"]
    },
    "poison": {
        "effective": ["ground", "psychic"],
        "not_effective": ["grass", "fighting", "poison", "bug", "fairy"]
    },
    "ground": {
        "effective": ["water", "grass", "ice"],
        "not_effective": ["poison", "rock"],
        "immune": ["electric"]
    },
    "flying": {
        "effective": ["electric", "ice", "rock"],
        "not_effective": ["grass", "fighting", "bug"],
        "immune": ["ground"]
    },
    "psychic": {
        "effective": ["bug", "ghost", "dark"],
        "not_effective": ["fighting", "psychic"]
    },
    "bug": {
        "effective": ["fire", "flying", "rock"],
        "not_effective": ["grass", "fighting", "ground"]
    },
    "rock": {
        "effective": ["water", "grass", "fighting", "ground", "steel"],
        "not_effective": ["normal", "fire", "poison", "flying"]
    },
    "ghost": {
        "effective": ["ghost", "dark"],
        "not_effective": ["poison", "bug"],
        "immune": ["normal", "fighting"]
    },
    "dragon": {
        "effective": ["ice", "dragon", "fairy"],
        "not_effective": ["fire", "water", "electric", "grass"]
    },
    "dark": {
        "effective": ["fighting", "bug", "fairy"],
        "not_effective": ["ghost", "dark"],
        "immune": ["psychic"]
    },
    "steel": {
        "effective": ["fire", "fighting", "ground"],
        "not_effective": ["normal", "grass", "ice", "flying", "psychic", "bug", "rock", "dragon", "steel", "fairy"],
        "immune": ["poison"]
    },
    "fairy": {
        "effective": ["poison", "steel"],
        "not_effective": ["fighting", "bug", "dark"],
        "immune": ["dragon"]
    }
}
    def status_effect(self,pokemon):
        turnskip = False
        for i,status in enumerate(pokemon.status):
            if status['name'] == 'burn':
                pokemon.currentstats['hp'] -= pokemon.basestats['hp']/16
                pokemon.currentstats['attack'] = pokemon.basestats['attack']/2
            if status['name'] == 'freeze':
                print(f'{pokemon.name} is frozen and cant act')
                turnskip = True

            if status['name'] == 'paralysis':
                pokemon.currentstats['speed'] = pokemon.basestats['speed'] / 4
                if random.randint(0,3) < 1:
                    print(f'{pokemon.name} is paralysed and cant act')
                    turnskip = True
            if status['name'] == 'poison':
                pokemon.currentstats['hp'] -= pokemon.basestats['hp'] / 16
            if status['name'] == 'sleep':
                status['duration'] -= 1
                print(f'{pokemon.name} is asleep and cant act')
                turnskip = True
                if status['duration'] == 1:
                    print(f'{pokemon.name} has woken up and will act next turn')
                    status[i].pop()

    def chose_target(self,attacker,target,move):
        if move['target'] in self.self_target_list:
            self.execute_move(attacker,attacker,move)
            pass
        elif move['target'] in self.enemy_target_list:
            self.execute_move(attacker, target, move)
            pass
        elif move['target'] in self.select_target_list:
            self.execute_move(attacker, target, move)
            #while True:
            #    print(f'Select Target:\n1.{attacker.name}\n2.{target.name}')
            #    try:
            #        user_input = int(input())
            #        if user_input == 1 or user_input == 2:
            #            break
            #    except:
            #        print('Enter 1 or 2')
            #if user_input == 1:
            #    self.execute_move(attacker, attacker, move)
            #else:
            #    self.execute_move(attacker, target, move)
            pass
    def player_move(self):
        print(
            f'\n{self.playerpokemon.name} :{self.playerpokemon.currentstats}, {self.playerpokemon.status}\n {self.aipokemon.name} :{self.aipokemon.currentstats},{self.aipokemon.status}\n')
        print(f'The player\'s {self.playerpokemon.name}\'s turn')
        user_input = 0
        while user_input not in range(1, 5):
            user_input = int(input(
                f'Select move: \n1.{self.playerpokemon.moves[0]}\n2.{self.playerpokemon.moves[1]}\n3.{self.playerpokemon.moves[2]} \n4.{self.playerpokemon.moves[3]}\n'))
        print(f'{self.playerpokemon.name} used {self.playerpokemon.moves[user_input - 1]['name']}\n')
        self.chose_target(self.playerpokemon, self.aipokemon, self.playerpokemon.moves[user_input - 1])

    def ai_move(self):
        print(
            f'\n{self.playerpokemon.name} :{self.playerpokemon.currentstats}, {self.playerpokemon.status}\n {self.aipokemon.name} :{self.aipokemon.currentstats},{self.aipokemon.status}\n')
        print(f'The Enemy {self.aipokemon.name}\'s turn\n')
        ai_choice = random.randint(0, 3)
        print(ai_choice)
        print(f'{self.aipokemon.name} used {self.aipokemon.moves[ai_choice]['name']}\n')
        self.chose_target(self.aipokemon, self.playerpokemon, self.aipokemon.moves[ai_choice])

    def turn_loop(self):
        #print(f'The player\'s {self.playerpokemon.name}\'s turn')
        #user_input = 0
        #while user_input not in range (1,5):
            #user_input = int(input(f'Select move: \n1.{self.playerpokemon.moves[0]}\n2.{self.playerpokemon.moves[1]}\n3.{self.playerpokemon.moves[2]} \n4.{self.playerpokemon.moves[3]}\n'))
        # print(f'{self.playerpokemon.name} used {self.playerpokemon.moves[user_input -1]['name']}\n')
        #try:
        #    self.aipokemon.currentstats['hp'] -= self.calc_damage(self.playerpokemon,self.aipokemon,self.playerpokemon.moves[user_input -1])
        #except(TypeError):
        #    print('Move has no power')
        #    self.move_effect(self.playerpokemon, self.aipokemon,self.playerpokemon.moves[user_input -1])
        #self.chose_target(self.playerpokemon,self.aipokemon,self.playerpokemon.moves[user_input -1])
        #print(f'The Enemy {self.aipokemon.name}\'s turn\n')
#
        #ai_choice = random.randint(0,3)
        #print(ai_choice)
        #print(f'{self.aipokemon.name} used {self.aipokemon.moves[ai_choice]['name']}\n')
        #self.chose_target(self.aipokemon, self.playerpokemon, self.aipokemon.moves[ai_choice])
        #print(f'Enemy {self.aipokemon.name} Used {self.aipokemon.moves[ai_choice]['name']}')
        #try:
        #    self.playerpokemon.currentstats['hp'] -= self.calc_damage(self.aipokemon,self.playerpokemon, self.aipokemon.moves[ai_choice])
        #except(TypeError):
        #    print('Move has no power')
        #    self.move_effect(self.aipokemon,self.playerpokemon, self.aipokemon.moves[ai_choice])

        turn_order = self.turn_order(self.playerpokemon,self.aipokemon)
        for items in turn_order:
            if items == self.playerpokemon:
                self.player_move()
                self.turn_loop()
            else:
                self.ai_move()
                self.faint_check()
        self.turn_loop()



    def faint_check(self):
        if self.playerpokemon.currentstats['hp'] <= 0:
            print(f'{self.playerpokemon.name} fainted')
            print(
                f'\n{self.playerpokemon.name} :{self.playerpokemon.currentstats}, {self.playerpokemon.status}\n {self.aipokemon.name} :{self.aipokemon.currentstats},{self.aipokemon.status}\n')
            input('Any key to exit')
            quit()
        elif self.aipokemon.currentstats['hp'] <= 0:
            print(f'{self.aipokemon.name} fainted')
            print(
                f'\n{self.playerpokemon.name} :{self.playerpokemon.currentstats}, {self.playerpokemon.status}\n {self.aipokemon.name} :{self.aipokemon.currentstats},{self.aipokemon.status}\n')
            input('Any key to exit')
            quit()

    def execute_move(self,attacker,target,move):
        damage = [  "damage",
                    "damage+ailment",
                    "damage+lower",
                    "damage+raise",
                    "damage+heal" ]
        stat = ["net-good-stats",
                "damage+lower",
                "damage+raise"]
        ailment = ["ailment",
                "damage+ailment"]
        if self.calc_hit(attacker,target,move):
            if move['category'] in damage:
                target.currentstats['hp'] -= self.calc_damage(attacker, target, move)
            if move['category'] in stat:
                if move['category'] == 'damage+raise':
                    self.move_effect(attacker,attacker,move)
                else:
                    self.move_effect(attacker, target, move)

            if move['category'] in ailment:
                if move['ailment_chance'] > 0:
                    if random.randint(0,100) > move['ailment_chance']:
                        print(f'{move['name']} failed to apply status')
                        return
                duration = -1
                if move['ailment'] == ('sleep'):
                    duration = random.randint(1,7)
                target.status.append({'name' : move['ailment'], 'duration': duration})
        else:
            print(f'{move['name']} missed')
            pass
        pass


    def calc_damage(self,attacker,target,move):
        damage = ((2 * self.calc_crit(attacker,move) *40)/5)+2
        damage *= self.calc_attack_defence(attacker,target,move)
        damage /= 50
        for types in attacker.type:
            if move['type'] == types:
                damage *= 1.5
                print('Attackers type matches move type')
        damage *= self.calc_type_effectiveness(target.type,move['type'])
        damage *= random.randint(217,255) /255
        damage = round(damage)
        print(f'{move['name']} did {damage} damage')
        return damage

    def calc_crit(self,attacker,move):
        if move['crit'] == 0:
            crit_chance = attacker.currentstats['speed']/2
        else:
            crit_chance = (attacker.currentstats['speed']*8)/2

        if random.randint(0,256) < crit_chance:
            print(f'{move['name']} crit with {crit_chance} / 256 chance')
            return 2
        else:
            return 1

    def calc_attack_defence(self,attacker,target,move):

        if move['damage_class'] == 'physical':
            return (attacker.currentstats['attack']/target.currentstats['defense'])*move['power']
        else:
            return (attacker.currentstats['special-attack'] / target.currentstats['special-defense']) * move['power']

    def calc_type_effectiveness(self,def_type,att_type):
        dmg_mult = 1
        for types in def_type:
            if att_type in self.type_effectiveness[types]['effective']:
                dmg_mult *=2
                print('super effective')
            elif att_type in self.type_effectiveness[types]['not_effective']:
                dmg_mult *=0.5
                print('not very effective')
            else:
                dmg_mult = 1
        try:
            for types in def_type:
                if att_type in self.type_effectiveness[types]['immune']:
                    dmg_mult = 0
                    print('immune')
        except:
            print('No immunities')
        return dmg_mult
        pass
    def move_effect(self,attacker,target,move):
        for effects in move['stat_changes']:
            #if move['target'] == 'user':
            #    attacker.stat_stages[effects['stat']['name']] += effects['change']
            #    attacker.stat_stage_apply()
            #else:
                target.stat_stages[effects['stat']['name']] += effects['change']
                target.stat_stage_apply()
    def calc_hit(self,attacker,defender,move):
        if move['accuracy'] == None:
            return True
        numerator,denominator = 3,3
        accuracy = attacker.stat_stages['accuracy']
        evasion = defender.stat_stages['accuracy']
        if accuracy > 0:
            numerator += accuracy
        else:
            denominator -= accuracy
        if evasion > 0:
            denominator += evasion
        else:
            numerator -= evasion
        modified_accuracy = (numerator/denominator) * move['accuracy']
        if random.randint(1,100) < modified_accuracy:
            return True
        else:
            return False
    def turn_order(self,pokemon1,pokemon2):
        if pokemon1.currentstats['speed']>pokemon2.currentstats['speed']:
            return [pokemon1,pokemon2]
        else:
            return [pokemon2,pokemon1]