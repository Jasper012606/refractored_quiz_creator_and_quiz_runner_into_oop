import os 
from questions import Question

class QuizLoader:
    def __init__(self, file_name="quiz.txt"):
        self.file_name = file_name
        
    def load_questions(self):
        if not os.path.exists(self.file_name):
            print(f"No quiz file found. Please create a quiz first.")
            return []
        
        with open(self.file_name, "r") as file:
            lines = [lines.strip() for lines in file.readlines() if lines.strip()]
            
        questions = []
        number_of_line = 0
        
        while number_of_line < len(lines):
            if lines[number_of_line].startswith("Question:"):
                question = lines[number_of_line].replace("Question: ", "").strip()
                choices = {}
                for j in range(1, 5):
                    label, choice = lines[number_of_line + j].split(". ", 1)
                    choices[label.strip()] = choice.strip()
                correct_line = lines[number_of_line + 5]
                correct_label = correct_line.split(":")[1].split(".")[0].strip()
                questions.append(Question(question, choices, correct_label))
                number_of_line += 6
            else:
                number_of_line += 1
        return questions