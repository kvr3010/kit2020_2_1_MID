import random, game
from flask import Flask ,json, request, render_template, url_for, redirect, session
app = Flask(__name__)

@app.route('/')
def login():
     return render_template('login.html')

@app.route('/save', methods=['GET','POST'])
def save():
    pname = request.form['pname']
    powerup = request.form['powerup']
    playerinfo = game.setplayer(pname,powerup)
    game.save(playerinfo)

    return render_template('start.html', data=playerinfo)

@app.route('/load')
def load():
    loadplayer = game.load()
    return loadplayer

@app.route('/play/<int:num>')
def input_num(num):
    player = game.load()
    result = game.play(num)
    if player['win']+1 < 3 and player['life']-1 > 0:
        if result == 'win':
            result = '이겼습니다!'
            show = '이겼습니다. 승리 : {} 기회 : {}'.format(player['win']+1,player['life'])
        elif result == 'drawwin':
            result = '강화된 {}로 이겼습니다!'.format(player['powerup'])
            show = '강화된 {}로 이겼습니다! 승리 : {} 기회 : {}'.format(player['powerup'],player['win']+1,player['life'])
        elif result == 'draw':
            result = '비겼습니다'
            show = '비겼습니다. 승리 : {} 기회 : {}'.format(player['win'],player['life'])
        else :
            result = '졌습니다.'
            show = '졌습니다.승리 : {} 기회 : {}'.format(player['win'],player['life']-1)

        return render_template('play.html', data = result ,info = show)

    elif player['win']+1 >= 3:
        result = '3번 승리로 게임에서 이겼습니다.'
        return render_template('game_result.html', data = result)
    else :
        result = '3번 패배로 게임에서 졌습니다.'
        return render_template('game_result.html', data = result)

        


if __name__ == '__main__':
    app.run(debug=True)