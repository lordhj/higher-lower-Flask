from flask import Flask
import random
random_num = random.randint(0,9)
print(random_num)

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>'\
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
def guess(num):
    if num>random_num:
        #TooHigh
        return '<h1 style="color:blue">Too High Try Again!</h1>'\
            '<img src="https://media.giphy.com/media/79eQOjPPrisR9B2zy6/giphy.gif">'

    elif num<random_num:
        #TooLow
        return '<h1 style="color:red">Too Low Try Again!</h1>'\
            '<img src="https://media.giphy.com/media/U52j0YphKRTEs/giphy.gif">'

    else:
        return '<h1 style="color:green">You Found Me!</h1>'\
            '<img src="https://media.giphy.com/media/28mj7bTsxXMH5bStdl/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)