import os
from questions import Question

class QuizManager(Question):
    def __init__(self, file_name = "quiz.txt"):
        self.file_name = file_name
        super().__init__()
        
    def question_exists(self, question):
        if not os.path.exists(self.file_name):
            return False
        with open(self.file_name, 'r') as file:
            return any(question.lower() in line.lower() for line in file)
        
    def save_question(self):
        if not self.question_exists():    
            with open(self.file_name, "a") as file:
                file.write(self.format_question())  