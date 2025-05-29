#make a class for Questions
class Question:
    def __init__(self, question, choices, correct_label):
        self.question = question
        self.choices = choices
        self.correct_label = correct_label
    