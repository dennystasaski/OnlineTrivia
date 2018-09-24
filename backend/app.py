from TriviaRequest import main
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/question')
def giveQuestion():
    questions = main()
    return questions
