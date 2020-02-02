from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'batman'

class Game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console

class User:
    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password


user1 = User('T', 'Tucano', '1234')
user2 = User('F', 'Ferrozo', '666')
user3 = User('A', 'Almeida', '999')

users = {user1.id: user1,
            user2.id: user2,
            user3.id: user3}


game1 = Game('Super Mario', 'Ação', 'SNES')
game2 = Game('Pokemon Gold', 'RPG', 'GBA')
listy = [game1, game2]

@app.route('/')
def index():
    return render_template('lista.html', titulo='Game', games=listy)

@app.route('/new')
def novo():
    if 'user_on' not in session or session['user_on'] == None:
        return redirect(url_for('login', nextt=url_for('new')))
    return render_template('new.html', titulo='New Game')

@app.route('/create', methods=['POST',])
def create():
    name = request. form['name']
    category = request. form['category']
    console = request. form['console']
    game = Game(name, category, console)
    listy.append(game)
    return redirect(url_for('index'))


@app.route('/login')
def login():
    nextt = request.args.get('nextt')
    return render_template('login.html', nextt=nextt)


@app.route('/authenticate', methods=['POST', ])
def authenticate():
    if request.form['user'] in users:
        user = users[request.form['user']]
        if user.password == request.form['password']:
            session['user_on'] = user.id
            flash(user.name + ' success!')
            nextt_page = request.form['nextt']
            return redirect(nextt_page)
    else:
        flash('Not logged !')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['user_on'] = None
    flash('No users logged in!')
    return redirect(url_for('login'))


app.run(debug=True)