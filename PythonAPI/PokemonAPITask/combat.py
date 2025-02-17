import random
class Combat:
    def __init__(self,playerpokemon,aipokemom):
        self.playerpokemon = playerpokemon
        self.aipokemon = aipokemom


    def turn_loop(self):
        print(f'The player\'s {self.playerpokemon.name}\'s turn')
        user_input = 0
        while user_input not in range (1,5):
            user_input = int(input(f'Select move: \n1.{self.playerpokemon.moves[0]}\n2.{self.playerpokemon.moves[1]}\n3.{self.playerpokemon.moves[2]} \n4.{self.playerpokemon.moves[3]}\n'))
        print(f'{self.playerpokemon.name} used {self.playerpokemon.moves[user_input -1]['name']}\n')

        print(f'The Enemy {self.aipokemon.name}\'s turn\n')

        print(f'Enemy {self.aipokemon.name} Used {self.aipokemon.moves[random.randint(0,4)]['name']}')


    def calc_damage(self,attacker,target,move):
        2 * self.calc_crit(move)

    def calc_crit(self,attacker,move):
        pass
    def calc_attack_defence(self,attacker,target):
        pass
    def calc_STAB(self,attacker,move):
        pass
    def calc_type_effectiveness(self,type1,type2):
        pass
    def calc_random(self):
        pass