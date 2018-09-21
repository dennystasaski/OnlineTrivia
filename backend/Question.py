import urllib.parse


class Question:
    def __init__(self, raw_question):
        self.q = raw_question
        self.category = urllib.parse.unquote_plus(self.q['category'])
        self.type = urllib.parse.unquote_plus(self.q['type'])
        self.difficulty = urllib.parse.unquote_plus(self.q['difficulty'])
        self.question = urllib.parse.unquote_plus(self.q['question'])
        self.correct = urllib.parse.unquote_plus(self.q['correct_answer'])
        self.incorrect = []
        for ans in self.q['incorrect_answers']:
            self.incorrect.append(urllib.parse.unquote_plus(ans))
