import os

class QuizManager:
    def __init__(self, file_name = "quiz.txt"):
        self.file_name = file_name
        
    def question_exists(self, question):
        if not os.path.exists(self.file_name):
            return False
        with open(self.file_name, 'r') as file:
            return any(question.lower() in line.lower() for line in file)
        