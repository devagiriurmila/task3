import re

def assess_password_strength(password):
    # Initialize score
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    # Check for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    # Check for digit
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    # Check for special character
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (e.g., !, @, #, etc.).")

    # Determine strength based on score
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback

def main():
    while True:
        password = input("Enter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            break

        strength, feedback = assess_password_strength(password)
        print(f"Password strength: {strength}")

        if feedback:
            print("Feedback:")
            for item in feedback:
                print(f" - {item}")

        print()

if __name__ == "__main__":
    main()
