def get_student_score() -> float:
    """Prompts the user to enter their score and returns it as a float."""
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid input. Please enter a score between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def calculate_grade(score: float) -> str:
    """Determines the letter grade based on the given score."""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Main Program
score = get_student_score()
grade = calculate_grade(score)
print(f"Your Grade is: {grade}")
