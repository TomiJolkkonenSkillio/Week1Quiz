import json
def quiz():
    print("Welcome!")
    while True:
        play = input("Do you want to play a quiz? (yes/no): ").strip().lower()

        if play != "yes":
            print("Quitting. Goodbye!")
            break

        print("Ok, let´s start!")

        with open('quiz.json', 'r') as tiedosto:
            sisalto = json.load(tiedosto)
            correct_ones = 0
            q_num = 1
            for question in sisalto:
                print(f"Question {q_num}: {question['kysymys']}")
                print(f"   1) {question['vaihtoehto1']}")
                print(f"   2) {question['vaihtoehto2']}")
                print(f"   3) {question['vaihtoehto3']}")
                answer = int(input("Answer: "))
                if answer == question["oikea_vastaus"]:
                    correct_ones = correct_ones + 1
                    print("Correct!")
                else:
                    print(f"Wrong! The correct answer was {question['oikea_vastaus']}")
                print()
            print(f"You had {correct_ones} right answers out of 3. Goodbye!")

if __name__ == "__main__":
    quiz()