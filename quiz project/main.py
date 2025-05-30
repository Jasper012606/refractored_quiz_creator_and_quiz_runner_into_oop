from quiz_creator import QuizCreator
from quiz_loader import QuizLoader
from quiz_game import QuizGame

def main():
    print("Welcome to the Quiz Application!\n 1. Create a Quiz\n 2. Load a Quiz\n 3. Exit")
    
    choice = input("Please select an option (1/2/3): ").strip()
    if choice == '1':
        creator = QuizCreator()
        creator.run()
    elif choice == '2':
        loader = QuizLoader()
        questions = loader.load_questions()
        if questions:
            game = QuizGame(questions)
            game.run()
    elif choice == '3':
        print("Exiting the application. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")