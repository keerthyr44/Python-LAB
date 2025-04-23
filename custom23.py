# Custom exception class
class InvalidScoreError(Exception):
    pass

# Function to validate the score
def validate_score(score):
    if score < 0 or score > 100:
        raise InvalidScoreError("Score must be between 0 and 100.")
    return "Score is valid."

# Main program with try-except
try:
    score = int(input("Enter exam score: "))
    print(validate_score(score))
except InvalidScoreError as e:
    print("InvalidScoreError:", e)
except ValueError:
    print("ValueError: Please enter a valid number.")
