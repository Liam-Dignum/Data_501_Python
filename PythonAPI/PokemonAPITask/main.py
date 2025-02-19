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
    gen_1_list.append(Pokemon(listpos['name']))

print(len(gen_1_list))
print_string = ''
for items in gen_1_list:
    print_string += items.name + ','
print(print_string)

gen_1_list[0].get_stats()

gen_1_list[1].get_stats()

print(gen_1_list[0].name, gen_1_list[0].basestats,gen_1_list[0].type,gen_1_list[0].status)

print(gen_1_list[1].name,gen_1_list[1].basestats,gen_1_list[1].type,gen_1_list[1].status)


gen_1_list[0].get_move_stats()
gen_1_list[1].get_move_stats()
current_combat = Combat(gen_1_list[0],gen_1_list[1])
current_combat.turn_loop()