import random

import requests
import requests_cache
from pokemon import Pokemon
from combat import Combat

base_url = 'https://pokeapi.co/api/v2/'

requests_cache.install_cache('poke_cache')
#r = requests.get(base_url + 'pokedex/2')
#r_json = r.json()
#print(r_json['pokemon_entries'])
#r = requests.get(base_url + 'pokemon/1')


r = requests.get(base_url + 'generation/1')
r_json = r.json()
print(r_json['pokemon_species'])
print(len(r_json['pokemon_species']))
gen_1_list = []
for listpos in r_json['pokemon_species']:
    gen_1_list.append(listpos['name'])

print(len(gen_1_list))
print_string = ''
for items in gen_1_list:
    print_string += items + ','
print(print_string)

user_input = 0
while user_input not in gen_1_list:
    user_input = input('Enter a Pokemon name in the list\n')

pokemon1 = Pokemon(user_input)
pokemon2 = Pokemon(gen_1_list[random.randint(0,150)])

print(pokemon1.name)
print(pokemon2.name)

pokemon1.get_stats()
pokemon2.get_stats()

print(pokemon1.name, pokemon1.basestats,pokemon1.type,pokemon1.status)

print(pokemon2.name,pokemon2.basestats,pokemon2.type,pokemon2.status)


pokemon1.get_move_stats()
pokemon2.get_move_stats()

current_combat = Combat(pokemon1,pokemon2)
current_combat.turn_loop()