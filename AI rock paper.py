import random
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
choices = ["rock", "paper", "scissors"]
Human_choices = []
Human_score = 0
AI_score = 0

def determine_winner(AI_choice, human_choice):
    if human_choice == AI_choice:
        return "tie"
    elif (human_choice == "rock" and AI_choice == "scissors") or (human_choice == "paper" and AI_choice == "rock") or (human_choice == "scissors" and AI_choice == "paper"):
        return "human"
    else:
        return "AI"

while True:
    human_choice = input("Enter your choice (rock, paper, scissors) for exit (q): ").lower()

    if human_choice == "q":
        print(f"Final scores: Human: {Human_score}, AI: {AI_score}")
        break

    if human_choice in choices:
        Human_choices.append(human_choice)

        if len(Human_choices) > 6:
            mapping = {"rock": 0, "paper": 1, "scissors": 2}
            human_choices_map = [mapping[choice] for choice in Human_choices]
            X = np.array(human_choices_map[:-1]).reshape(-1, 1) 
            y = np.array(human_choices_map[1:])  
            model.fit(X, y)
            
            last_choice = np.array([human_choices_map[-1]]).reshape(-1, 1)
            prediction = model.predict(last_choice)
            prediction = int(round(prediction[0]))  
            AI_choice_for_counter = choices[prediction] 
            if AI_choice_for_counter == "rock":
                AI_choice = "paper"
            elif AI_choice_for_counter == "paper":
                AI_choice = "scissors"
            else:
                AI_choice = "rock"

            print(f"AI chose: {AI_choice}")
            winner = determine_winner(AI_choice, human_choice)

            if winner == "human":
                Human_score += 1
                print("You win!")
            elif winner == "AI":
                AI_score += 1
                print("AI wins!")
            else:
                print("It's a tie!")

        else:
            AI_choice = random.choice(choices) 
            print(f"AI chose: {AI_choice}")
            winner = determine_winner(AI_choice, human_choice)

            if winner == "human":
                Human_score += 1
                print("You win!")
            elif winner == "AI":
                AI_score += 1
                print("AI wins!")

    else:
        print("Invalid choice! Please choose rock, paper, or scissors.")
