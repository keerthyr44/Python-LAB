# Get feedback input from the user
feedback = input("Enter your feedback: ")

# Convert the feedback to lowercase for case-insensitive comparison
feedback_lower = feedback.lower()

# Count how many times the word 'good' appears
count_good = feedback_lower.split().count("good")

# Display the result
print(f"The word 'good' appears {count_good} time(s).")
