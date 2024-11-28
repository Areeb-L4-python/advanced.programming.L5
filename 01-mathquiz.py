import random

# Function to display the difficulty menu
def displayMenu():
    print("\nDIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")

# Function to generate random integer based on difficulty level
def randomInt(level):
    if level == 1:  # Easy: Single-digit numbers
        return random.randint(1, 9)
    elif level == 2:  # Moderate: Double-digit numbers
        return random.randint(10, 99)
    elif level == 3:  # Advanced: Four-digit numbers
        return random.randint(1000, 9999)
    else:
        return None

# Function to randomly decide between addition and subtraction
def decideOperation():
    return random.choice(['+', '-'])

# Function to display the problem and get user's answer
def displayProblem(num1, num2, operation):
    if operation == '+':
        print(f"{num1} + {num2} = ", end="")
    else:
        print(f"{num1} - {num2} = ", end="")
    return int(input())

# Function to check if the answer is correct
def isCorrect(num1, num2, operation, user_answer):
    if operation == '+':
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2
    return correct_answer == user_answer

# Function to display the final results and rank
def displayResults(score):
    print(f"\nYour final score: {score}/100")
    if score >= 90:
        print("Rank: A+")
    elif score >= 80:
        print("Rank: A")
    elif score >= 70:
        print("Rank: B")
    elif score >= 60:
        print("Rank: C")
    else:
        print("Rank: F")

# Main quiz function
def playQuiz():
    displayMenu()
    
    # Getting the user's choice for difficulty level
    level = int(input("Choose your difficulty level (1-3): "))
    
    score = 0
    for _ in range(10):  # 10 questions per quiz
        num1 = randomInt(level)
        num2 = randomInt(level)
        operation = decideOperation()
        
        # First attempt
        user_answer = displayProblem(num1, num2, operation)
        if isCorrect(num1, num2, operation, user_answer):
            print("Correct! +10 points")
            score += 10
        else:
            print("Incorrect. Try again.")
            # Second attempt
            user_answer = displayProblem(num1, num2, operation)
            if isCorrect(num1, num2, operation, user_answer):
                print("Correct! +5 points")
                score += 5
            else:
                print(f"Wrong again. The correct answer was {num1 + num2 if operation == '+' else num1 - num2}.")
    
    # Display results
    displayResults(score)

# Main loop to ask if user wants to play again
def main():
    while True:
        playQuiz()
        replay = input("\nWould you like to play again? (yes/no): ").lower()
        if replay != 'yes':
            print("Thanks for playing!")
            break

# Run the quiz
if __name__ == "__main__":
    main()
