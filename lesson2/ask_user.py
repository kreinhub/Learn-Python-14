dialog = {"How are you?": "Fine", "What are you doing?": "Programming", "What the language are you aplying?": "Python"}
def ask_user():
    questions = " ".join(list(dialog.keys()))
    print(f"Hello! These are the possible questions to me: {questions}")
    # answer = input("Hello!\n")
    while True:
        question = input("Enter the question to me: ")
        if question in dialog.keys():
            print(dialog[question])
        else:
            print("Sorry. I didn't get it. Bye")
            break
        

ask_user()