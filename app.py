from models import *
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request, redirect, abort


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wigames.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
@app.before_request
def create_table():
    db.create_all()


def create_app():
  app = Flask(__name__)
  Bootstrap(app)

  return app

# rota index.html
@app.route("/")
def indexRender():
    return render_template("index.html")


# rota new-game.html new game (create game)
@app.route('/games/new' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('new-game.html')
    
    if request.method == 'POST':
        
        name = request.form['name']
        developer = request.form['developer']
        game = Game(name=name, developer=developer)

        db.session.add(game)
        db.session.commit()

        return redirect('/games')


# rota list-games.html search for all games (read all / query all)
@app.route("/games")
def RetrieveList():
    games = Game.query.all()
    return render_template("list-games.html",games = games)


# rota specific game.html
@app.route("/games/<int:id>")
def RetrieveEmployee(id):
    game = Game.query.filter_by(game_id=id).first()
    if game:
        return render_template('specific-game.html', game = game)
    return f"Game with id ={id} Doenst exist"


# rota specific-game.html or update-game.html
@app.route('/data/<int:id>/update',methods = ['GET','POST'])
def update(id):
    game = Game.query.filter_by(game_id=id).first()

    if request.method == 'POST':
    
        if game:
            db.session.delete(game)
            db.session.commit()
    
            name = request.form['name']
            developer = request.form['developer']
            game = Game(employee_id=id, name=name, developer=developer)
    
            db.session.add(game)
            db.session.commit()
    
            return redirect(f'/game/{id}')
    
        return f"Game with id = {id} Does not exist"
    
    return render_template('update-game.html', game=game)


# rota delete-game.html
@app.route('/games/<int:id>/delete', methods=['GET','POST'])
def delete(id):
    game = Game.query.filter_by(game_id=id).first()

    if request.method == 'POST':
        if game:
            db.session.delete(game)
            db.session.commit()
            return redirect('/games')
    
        abort(404)
    
    return render_template('delete-game.html')


app.run(host='localhost', port=5000)