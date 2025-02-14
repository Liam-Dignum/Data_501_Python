class Combat:
    def __init__(self,playerpokemon,aipokemom):
        self.playerpokemon = playerpokemon
        self.aipokemon = aipokemom



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