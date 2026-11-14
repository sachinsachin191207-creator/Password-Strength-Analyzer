
import string
import math
import getpass

# Common password examples
common_passwords = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123"
}

# Predictable sequences
predictable_patterns = [
    "0123456789",
    "9876543210",
    "123456789",
    "abcdefgh",
    "hgfedcba",
    "qwerty",
    "asdf",
    "zxcv"
]

# Get password securely
password = getpass.getpass("Enter your password: ")

if not password:
    print("\nError: Password cannot be empty!")

else:
    # Character analysis
    lowercase = any(c in string.ascii_lowercase for c in password)
    uppercase = any(c in string.ascii_uppercase for c in password)
    digits = any(c in string.digits for c in password)
    special = any(c in string.punctuation for c in password)

    # Character pool
    character_pool = 0

    if lowercase:
        character_pool += 26
    if uppercase:
        character_pool += 26
    if digits:
        character_pool += 10
    if special:
        character_pool += 32

    # Password length
    length = len(password)

    if length < 8:
        length_status = "Too Short"
    elif length < 12:
        length_status = "Moderate"
    else:
        length_status = "Good"

    # Entropy calculation
    entropy = 0

    if character_pool > 0:
        entropy = length * math.log2(character_pool)

    entropy = round(entropy, 2)

    # Common password detection
    is_common = password.lower() in common_passwords

    # Repeated character detection
    repeated = any(
        password[i] == password[i + 1] ==
        password[i + 2] == password[i + 3]
        for i in range(length - 3)
    )

    # Predictable pattern detection
    normalized_password = password.lower()

    has_pattern = any(
        pattern in normalized_password
        for pattern in predictable_patterns
    )

    # Strength classification
    if is_common or repeated or has_pattern:
        strength = "Very Weak"
    elif entropy < 28:
        strength = "Very Weak"
    elif entropy < 36:
        strength = "Weak"
    elif entropy < 60:
        strength = "Medium"
    elif entropy < 80:
        strength = "Strong"
    else:
        strength = "Very Strong"

    # Recommendations
    recommendations = []

    if is_common:
        recommendations.append("Avoid common passwords.")

    if repeated:
        recommendations.append("Avoid repeating the same character.")

    if has_pattern:
        recommendations.append("Avoid predictable sequences and keyboard patterns.")

    if length < 12:
        recommendations.append("Increase password length to at least 12 characters.")

    if not lowercase:
        recommendations.append("Include lowercase letters.")

    if not uppercase:
        recommendations.append("Include uppercase letters.")

    if not digits:
        recommendations.append("Include numbers.")

    if not special:
        recommendations.append("Consider including special characters.")

    # Display results
    print("\n========== PASSWORD ANALYSIS ==========")

    print("Lowercase:", lowercase)
    print("Uppercase:", uppercase)
    print("Digits:", digits)
    print("Special Characters:", special)

    print("\nCharacter Pool:", character_pool)
    print("Password Length:", length)
    print("Length Status:", length_status)
    print("Estimated Entropy:", entropy, "bits")

    print("\nCommon Password:", "Yes" if is_common else "No")
    print("Repeated Characters:", "Yes" if repeated else "No")
    print("Predictable Pattern:", "Yes" if has_pattern else "No")

    print("\nPassword Strength:", strength)

    print("\n========== RECOMMENDATIONS ==========")

    if recommendations:
        for item in recommendations:
            print("-", item)
    else:
        print("Good character variety and length.")
        print("Avoid predictable password patterns.")

    print("\n====================================")
    print("       ANALYSIS COMPLETED")
    print("====================================")
