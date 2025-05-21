import string
import math
import re


class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password
        self.length = len(password)
        self.feedback = []
        self.entropy = 0
        self.strength_label = ""

    def calculate_entropy(self):
        charset_size = 0
        if re.search(r'[a-z]', self.password):
            charset_size += 26
        if re.search(r'[A-Z]', self.password):
            charset_size += 26
        if re.search(r'[0-9]', self.password):
            charset_size += 10
        if re.search(r'[^a-zA-Z0-9]', self.password):
            charset_size += len(string.punctuation)

        if charset_size == 0:
            self.entropy = 0
        else:
            self.entropy = round(self.length * math.log2(charset_size), 2)

        return self.entropy

    def analyze_password(self):
        if self.length < 8:
            self.feedback.append("Password is too short. Minimum 8 characters recommended.")

        if not re.search(r'[A-Z]', self.password):
            self.feedback.append("Add at least one uppercase letter.")

        if not re.search(r'[a-z]', self.password):
            self.feedback.append("Add at least one lowercase letter.")

        if not re.search(r'[0-9]', self.password):
            self.feedback.append("Add at least one digit.")

        if not re.search(r'[^a-zA-Z0-9]', self.password):
            self.feedback.append("Add at least one special character (e.g., !, @, #, $).")

        self.calculate_entropy()
        self.strength_label = self.get_strength_label()

        return {
            "password": self.password,
            "length": self.length,
            "entropy": self.entropy,
            "strength": self.strength_label,
            "feedback": self.feedback
        }

    def get_strength_label(self):
        if self.entropy < 28:
            return "Very Weak"
        elif 28 <= self.entropy < 36:
            return "Weak"
        elif 36 <= self.entropy < 60:
            return "Moderate"
        elif 60 <= self.entropy < 128:
            return "Strong"
        else:
            return "Very Strong"


# Optional integration with breach checker
def check_with_breach_database(password):
    from pwned_checker import check_password_breach
    return check_password_breach(password)


if __name__ == "__main__":
    user_input = input("🔐 Enter your password: ").strip()
    checker = PasswordStrengthChecker(user_input)
    result = checker.analyze_password()

    print("\n🔍 Password Analysis:")
    print(f"Password Length  : {result['length']}")
    print(f"Password Entropy : {result['entropy']} bits")
    print(f"Strength Level   : {result['strength']}")
    
    if result["feedback"]:
        print("\n📌 Suggestions to improve:")
        for fb in result["feedback"]:
            print(f"- {fb}")
    else:
        print("\n✅ Your password is very strong!")

    # Optional: Uncomment below to check for breaches
    # breached = check_with_breach_database(user_input)
    # if breached:
    #     print(f"\n⚠️ Your password has been found in {breached} data breaches!")
    # else:
    #     print("\n✅ Your password has not been found in any known breach.")

