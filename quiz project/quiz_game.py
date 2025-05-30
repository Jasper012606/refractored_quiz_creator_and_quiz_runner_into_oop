from questions import Question

class QuizGame(Question):
    def __init__(self, file_path="quiz.txt"):
        self.file_path = file_path
        self.score = 0
    
    def run(self):
        print("Welcome to the Quiz Game!")
        for idx, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {idx}: {question.question}")
            for label, choice in question.choices.items():
                print(f"{label}. {choice}")
                
            while True:
                answer = input("Enter your answer (a/b/c/d): ").strip().lower()
                if answer not in question.choices:
                    print("Invalid choice. Please choose a/b/c/d only.")
                else:
                    break

            if question.is_correct(answer):
                print("Correct! ✅")
                self.score += 1
            else:
                print(f"Wrong! ❌ The correct answer is {question.get_correct_answer_text()}")
            
        self.show_score()
    
    def show_score(self):
        total = len(self.questions)
        print(f"\nQUIZ RESULTS")
        if self.score == 0:
            print(f"Your score is {self.score} out of {total}. Better luck next time!")
        elif self.score == total:
            print(f"You got a perfect score of {self.score} out of {total}! Hooray! 🎉")
        else:
            print(f"Your score is {self.score} out of {total}. Good job!")