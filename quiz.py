def quiz():
    def quiz():

    print("Welcome!")
    play = input("Do you want to play a quiz? (yes/no): ").strip().lower()

    if play != "yes":
        print("Quitting. Goodbye!")
        return

    print("Ok, let´s start!")

    while True:
        with open('quiz.json', 'r') as tiedosto:
        sisalto = tiedosto.read()
        correct_ones = 0

        print(sisalto.kysymys)
        answer1 = int(input("What is? "))
        if answer1 == 2:
            correct_ones = correct_ones + 1
        print(sisalto.kysymys)
        answer2 = int(input("What is? "))
        if answer2 == 2:
            correct_ones = correct_ones + 1
        print(sisalto.kysymys)
        answer3 = int(input("What is? "))
        if answer3 == 2:
            correct_ones = correct_ones + 1

        print(f"You had {correct_ones} right answers out of 3. Goodbye!")
        break

if __name__ == "__main__":
    quiz()