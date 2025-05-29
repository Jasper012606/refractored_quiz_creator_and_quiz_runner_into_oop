#make a class for Questions
class Question:
    def __init__(self, question, choices, correct_label):
        self.question = question
        self.choices = choices
        self.correct_label = correct_label
    
    def is_valid(self):
        return self.question.strip() != "" and len(self.question) >= 10 and self.correct_label in self.choices
    
    def is_correct(self, answer):
        return answer == self.correct_label
    
    def get_correct_answer_text(self):
        return f"{self.correct_label}. {self.choices[self.correct_label]}"
    