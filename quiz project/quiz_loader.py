import os 
from questions import Question

class QuizLoader:
    def __init__(self, file_name="quiz.txt"):
        self.file_name = file_name
        
    def load_questions(self):
        if not os.path.exists(self.file_name):
            print(f"No quiz file found. Please create a quiz first.")
            return []
        