from flask import Flask, render_template

app = Flask(__name__)

class game:
    def __init__(self, name, category, console):
        self.name = name
        self.category = category
        self.console = console




@app.route('/')
def hello():
    game1 = game('Super Mario', 'Acao', 'SNES')
    game2 = game('Pokemon Gold', 'RPG', 'GBA')
    listy = [game1, game2]
    return render_template('lista.html', title = 'Games', game = listy)
app.run()