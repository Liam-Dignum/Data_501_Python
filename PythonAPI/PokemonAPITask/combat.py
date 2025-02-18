import random
from bdb import effective


class Combat:
    def __init__(self,playerpokemon,aipokemom):
        self.playerpokemon = playerpokemon
        self.aipokemon = aipokemom
        self.self_target_list = ['user']
        self.enemy_target_list = ['random-opponent', 'selected-pokemon']
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


    def turn_loop(self):
        print(f'\n{self.playerpokemon.name} :{self.playerpokemon.currentstats}\n {self.aipokemon.name} :{self.aipokemon.currentstats}\n')
        print(f'The player\'s {self.playerpokemon.name}\'s turn')
        user_input = 0
        while user_input not in range (1,5):
            user_input = int(input(f'Select move: \n1.{self.playerpokemon.moves[0]}\n2.{self.playerpokemon.moves[1]}\n3.{self.playerpokemon.moves[2]} \n4.{self.playerpokemon.moves[3]}\n'))
        print(f'{self.playerpokemon.name} used {self.playerpokemon.moves[user_input -1]['name']}\n')
        try:
            self.aipokemon.currentstats['hp'] -= self.calc_damage(self.playerpokemon,self.aipokemon,self.playerpokemon.moves[user_input -1])
        except(TypeError):
            print('Move has no power')
            self.move_effect(self.playerpokemon, self.aipokemon,self.playerpokemon.moves[user_input -1])
        print(f'The Enemy {self.aipokemon.name}\'s turn\n')

        ai_choice = random.randint(0,3)
        print(ai_choice)

        print(f'Enemy {self.aipokemon.name} Used {self.aipokemon.moves[ai_choice]['name']}')
        try:
            self.playerpokemon.currentstats['hp'] -= self.calc_damage(self.aipokemon,self.playerpokemon, self.aipokemon.moves[ai_choice])
        except(TypeError):
            print('Move has no power')
            self.move_effect(self.aipokemon,self.playerpokemon, self.aipokemon.moves[ai_choice])
        if self.playerpokemon.currentstats['hp'] <= 0:
            print(f'{self.playerpokemon.name} fainted')
            return
        elif self.aipokemon.currentstats['hp'] <= 0:
            print(f'{self.aipokemon.name} fainted')
            return
        else:
            self.turn_loop()

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
            if move['target'] == 'user':
                attacker.stat_stages[effects['stat']['name']] += effects['change']
                attacker.stat_stage_apply()
            else:
                target.stat_stages[effects['stat']['name']] += effects['change']
                target.stat_stage_apply()
