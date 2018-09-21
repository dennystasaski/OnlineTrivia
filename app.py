from TriviaRequest import main
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    questions = main()
    return questions[0].question
