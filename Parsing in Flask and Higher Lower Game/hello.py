import random

random_number = random.randint(0, 9)
print(random_number)

from flask import Flask
app = Flask(__name__)

@app.route('/')
def guess_num():
    return '<h1>Guess a number between 0 to 9</h1>' \
           '<img src="https://media.giphy.com/media/h4wTo632mUgN6ObJrc/giphy.gif">'

@app.route('/<int:number>')
def guessing(number):
    if(number > random_number):
        return '<h1>Too high</h1>'\
               '<img src="https://media.giphy.com/media/3orieS5oO8DqAF9a8w/giphy.gif">'

    elif(number < random_number):
        return '<h1>Too low</h1>' \
               '<img src="https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif">'

    else:
        return '<h1>Correct</h1>' \
               '<img src="https://media.giphy.com/media/26tknCqiJrBQG6bxC/giphy.gif">'

if __name__ == '__main__':
    app.run(debug=True)