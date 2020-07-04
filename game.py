from flask import json
import random


def setplayer(pname,powerup):
    player = {
         "name" : pname,
         "powerup" : powerup,
         "life"    : 3,
         "win"  : 0
         }
    return player


def save(info):
    import midtest
    with open('saveinfo.txt', 'w', encoding = 'utf-8') as s:
        json.dump(info, s, ensure_ascii = False, indent='\t')


def load():
    with open('saveinfo.txt', 'r', encoding='utf-8') as load:
        data = load.read()
        player = json.loads(data)
    return player

def update(result):
    update = load()
    if result == 'drawwin' or result == 'win':
        update["win"] += 1
    elif result == 'lose':
        update["life"] -= 1
    with open('static/saveinfo.txt', 'w', encoding = 'utf-8') as s:
        json.dump(update, s, ensure_ascii = False, indent='\t')


def changenum():
    player_info = load()
    if player_info["powerup"] == '가위':
        return 1
    elif player_info["powerup"] == '바위':
        return 2
    else :
        return 3


def play(num):
    other_num = random.randint(1,3)
    powerup = random.random()
    if num == other_num:
         if changenum() == num and powerup >= 0.5: 
            update('drawwin')
            return 'drawwin'
         else:
            return 'draw'
    elif (num+1)%3 == other_num%3:
         update('lose')
         return 'lose'
    else :
         update('win')
         return 'win'
