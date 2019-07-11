from django import forms
from django.shortcuts import render, HttpResponse
import requests
import json
import random
from django.template import RequestContext

import json as simplejson
from django.shortcuts import render_to_response



# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def fortress_battle(request):
    battle_result_list = []
    userData = {}
    print('!!!!!!!******  testing fortress_battle function (in epic_battle_math.py) ok ******!!!!!!!')
    if request.method == 'POST':

        d = request.POST.get('d') # hero
        hero_race = request.POST.get('hero','')
        g = request.POST.get('g') # villain
        villain_race = request.POST.get('villain','')

        battle_terrain = request.POST.get('terrain','') 
        print(battle_terrain)

        d_pre_battle = d
        g_pre_battle = g

        d = int(d)
        d = d * 20 # total hp

        if villain_race == 'Orc':
          g = int(g)
          g = g * 30 # total hp
        else: 
          g = int(g)
          g = g * 20 # total hp
  
        round_counter = 0
        crit_hit_counter = 0
        battle_result_list = []

        while d > 0 and g > 0:

          if battle_terrain == 'Mountain' and hero_race == 'Dwarf':
            attack_roll_d = random.randint(1, 20) + 2
          elif battle_terrain == 'Forest' and hero_race == 'Elf':
            attack_roll_d = random.randint(1, 20) + 2
          elif battle_terrain == 'Fortress' and hero_race == 'Human':
            attack_roll_d = random.randint(1, 20) + 2
          else:
            attack_roll_d = random.randint(1, 20)

          print('hero rolls: ' + str(attack_roll_d))

          if attack_roll_d + 1 >= 14 and attack_roll_d < 20:
            axe_damage = random.randint(1, 10)
            g = g - axe_damage
            print('villain takes ' + str(axe_damage) + ' points from the hero axe.')

          elif attack_roll_d == 20:
            print('Critical Hit!')
            crit_hit_counter += 1
            axe_damage_crit = 3 * (random.randint(1, 10))
            g = g - axe_damage_crit
            print('villain takes ' + str(axe_damage_crit) + ' points from the hero axe.')
        
          else:
            pass
            print('hero missed!')

          if g < 1:
            break

          if battle_terrain == 'Dungeon' and villain_race == 'Goblin':
            attack_roll_g = random.randint(1, 20) + 2
          elif battle_terrain == 'Swamp' and villain_race == 'Orc':
            attack_roll_g = random.randint(1, 20) + 2
          else:
            attack_roll_g = random.randint(1, 20)

          print('villain rolls: ' + str(attack_roll_g))

          if attack_roll_g + 1 >= 15 and attack_roll_g < 20:
            spear_damage = random.randint(1, 8)
            d = d - spear_damage
            print('hero takes ' + str(spear_damage) + ' points from the villain spear.')

          elif attack_roll_g == 20:
            print('Critical Hit!')
            crit_hit_counter += 1
            spear_damage_crit = 3 * (random.randint(1, 8))
            d = d - spear_damage_crit
            print('hero takes ' + str(spear_damage_crit) + ' points from the villain spear.')

          else:
            pass
            print('villain missed!')

          round_counter += 1

        if villain_race == 'Orc':
          g_survive = (g / 30)
        else:
          g_survive = (g / 20)

        if type(g_survive) == float:
          g_survive = int(g_survive) + 1
        
        d_survive = (d / 20)
        if type(d_survive) == float:
          d_survive = int(d_survive) + 1


        if d < 1:

          if villain_race == 'Goblin':
            winner_statement = 'Goblins win!'
            print(winner_statement)
            if g_survive > 1:
              survive_statement = str(g_survive) + ' goblins survive the battle.'
              print(survive_statement)
            else:
              survive_statement = '1 goblin survives the battle.'
              print(survive_statement)

          if villain_race == 'Orc':
            winner_statement = 'Orcs win!'
            print(winner_statement)
            if g_survive > 1:
              survive_statement = str(g_survive) + ' orcs survive the battle.'
              print(survive_statement)
            else:
              survive_statement = '1 orc survives the battle.'
              print(survive_statement)
        

        if g < 1:

          if hero_race == 'Dwarf':
            winner_statement = 'Dwarves win!'
            print(winner_statement)
            if d_survive > 1:
              survive_statement = str(d_survive) + ' dwarves survive the battle.'
              print(survive_statement)
            else:
              survive_statement = '1 dwarf survives the battle.'
              print(survive_statement)

          if hero_race == 'Elf':
            winner_statement = 'Elves win!'
            print(winner_statement)
            if d_survive > 1:
              survive_statement = str(d_survive) + ' elves survive the battle.'
              print(survive_statement)
            else:
              survive_statement = '1 elf survives the battle.'
              print(survive_statement)

          if hero_race == 'Human':
            winner_statement = 'Humans win!'
            print(winner_statement)
            if d_survive > 1:
              survive_statement = str(d_survive) + ' humans survive the battle.'
              print(survive_statement)
            else:
              survive_statement = '1 human survives the battle.'
              print(survive_statement)

  
        round_statement = 'Battle duration: ' + str(round_counter) + ' one-on-one rounds'
        crit_hit_statement = str(crit_hit_counter) + ' "Critical Hits" were recorded.'
        terrain_statement = 'Terrain: ' + battle_terrain
        pre_battle_info = 'Pre-battle count: \n' + str(d_pre_battle) + ' (' + hero_race + ') ' + 'vs. ' + str(g_pre_battle) + ' (' + villain_race + ') '
        
        
        battle_result_list.append(str(winner_statement))
        battle_result_list.append(str(survive_statement))
        battle_result_list.append(str(round_statement))
        battle_result_list.append(str(crit_hit_statement))
        battle_result_list.append(str(terrain_statement))
        battle_result_list.append(pre_battle_info)

        print('testing variable' + str(battle_result_list))

        userData.update({'battle_result_list': battle_result_list})
    
    #     return HttpResponse(simplejson.dumps(userData), content_type='application/javascript')

    # return render_to_response('app/epic_battle.html', userData)


    return render(request, 'app/epic_battle.html', {'fb': battle_result_list})




# >>> a = u'hello\N{LINE SEPARATOR}world'
# >>> len(a.split('\n'))
# 1
# >>> len(a.splitlines())
# 2