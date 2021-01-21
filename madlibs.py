"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return """<html>
                    <body>
                        Hi! This is the home page.
                        <a href="http://localhost:5000/hello">Go to Greeting Page</a>
                    </body>
            </html>"""


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_madlib_form():
    """Show a form to fill in to create a madlib game based on player response"""

    player_response = request.args.get("play-game")

    if player_response == "yes":
        return render_template("game.html")
    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():
    """Show a madlib game"""

    person = request.args.get("game_person")
    color = request.args.get("game_color")
    noun = request.args.get("game_noun")
    adjective = request.args.get("game_adjective")

    return render_template("madlib.html", 
                            game_person=person,
                            game_color=color,
                            game_noun=noun,
                            game_adjective=adjective)


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
