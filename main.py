
import string
import math
import getpass


COMMON_PASSWORDS = {
    "password",
    "123456",
    "123456789",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123"
}


PREDICTABLE_PATTERNS = [
    "0123456789",
    "9876543210",
    "123456789",
    "12345678",
    "87654321",
    "abcdefgh",
    "hgfedcba",
    "qwerty",
    "asdf",
    "zxcv"
]


def contains_sequence(password):
    """Detect ascending or descending sequences of 4 characters."""

    allowed_characters = string.ascii_lowercase + string.digits

    for i in range(len(password) - 3):
        sequence = password[i:i + 4]

        if all(char in allowed_characters for char in sequence):

            ascending = all(
                ord(sequence[j + 1]) - ord(sequence[j]) == 1
                for j in range(3)
            )

            descending = all(
                ord(sequence[j]) - ord(sequence[j + 1]) == 1
                for j in range(3)
            )

            if ascending or descending:
                return True

    return False


def contains_repeated_pattern(password):
    """Detect repeated blocks such as 121212 or ababab."""

    for block_size in range(2, 5):

        for i in range(len(password) - (2 * block_size) + 1):

            first_block = password[i:i + block_size]
            second_block = password[i + block_size:i + (2 * block_size)]

            if (
                first_block == second_block
                and len(set(first_block)) > 1
            ):
                return True

    return False


def calculate_score(length, character_types, entropy,
                    is_common, repeated, has_pattern):
    """Calculate password score out of 100."""

    # Length points
    if length >= 16:
        length_points = 40
    elif length >= 12:
        length_points = 30
    elif length >= 8:
        length_points = 15
    else:
        length_points = 0

    # Character diversity points
    diversity_points = min(character_types * 8, 30)

    # Entropy points
    if entropy >= 80:
        entropy_points = 30
    elif entropy >= 60:
        entropy_points = 24
    elif entropy >= 36:
        entropy_points = 16
    elif entropy >= 28:
        entropy_points = 8
    else:
        entropy_points = 0

    # Calculate base score
    score = length_points + diversity_points + entropy_points

    # Apply penalties
    if is_common:
        score -= 50

    if repeated:
        score -= 20

    if has_pattern:
        score -= 25

    # Keep score between 0 and 100
    score = max(0, min(100, score))

    return score


def analyze_password(password):

    if not password:
        raise ValueError("Password cannot be empty")

    # Character analysis
    lowercase = any(c in string.ascii_lowercase for c in password)
    uppercase = any(c in string.ascii_uppercase for c in password)
    digits = any(c in string.digits for c in password)
    special = any(c in string.punctuation for c in password)

    # Character pool calculation
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
    entropy = (
        length * math.log2(character_pool)
        if character_pool > 0 else 0
    )

    entropy = round(entropy, 2)

    # Common password detection
    is_common = password.lower() in COMMON_PASSWORDS

    # Repeated character detection
    repeated = any(
        password[i] == password[i + 1] ==
        password[i + 2] == password[i + 3]
        for i in range(length - 3)
    )

    # Predictable pattern detection
    normalized_password = password.lower()

    listed_pattern = any(
        pattern in normalized_password
        for pattern in PREDICTABLE_PATTERNS
    )

    sequential_pattern = contains_sequence(normalized_password)

    repeated_pattern = contains_repeated_pattern(normalized_password)

    has_pattern = (
        listed_pattern
        or sequential_pattern
        or repeated_pattern
    )

    # Count character types
    character_types = sum([
        lowercase,
        uppercase,
        digits,
        special
    ])

    # Calculate score
    score = calculate_score(
        length,
        character_types,
        entropy,
        is_common,
        repeated,
        has_pattern
    )

    # Strength classification based on score
    if score < 25:
        strength = "Very Weak"
    elif score < 50:
        strength = "Weak"
    elif score < 70:
        strength = "Medium"
    elif score < 85:
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
        recommendations.append(
            "Avoid predictable sequences and repeated patterns."
        )

    if length < 12:
        recommendations.append(
            "Increase password length to at least 12 characters."
        )

    if not lowercase:
        recommendations.append("Include lowercase letters.")

    if not uppercase:
        recommendations.append("Include uppercase letters.")

    if not digits:
        recommendations.append("Include numbers.")

    if not special:
        recommendations.append("Consider including special characters.")

    return {
        "lowercase": lowercase,
        "uppercase": uppercase,
        "digits": digits,
        "special": special,
        "character_pool": character_pool,
        "character_types": character_types,
        "length": length,
        "length_status": length_status,
        "entropy": entropy,
        "is_common": is_common,
        "repeated": repeated,
        "has_pattern": has_pattern,
        "score": score,
        "strength": strength,
        "recommendations": recommendations
    }


def main():

    password = getpass.getpass("Enter your password: ")

    try:
        result = analyze_password(password)

    except ValueError as error:
        print("\nError:", error)
        return

    print("\n========== PASSWORD ANALYSIS ==========")

    print("Lowercase:", result["lowercase"])
    print("Uppercase:", result["uppercase"])
    print("Digits:", result["digits"])
    print("Special Characters:", result["special"])

    print("\nCharacter Pool:", result["character_pool"])
    print("Character Types:", result["character_types"])
    print("Password Length:", result["length"])
    print("Length Status:", result["length_status"])
    print("Estimated Entropy:", result["entropy"], "bits")

    print("\nCommon Password:", result["is_common"])
    print("Repeated Characters:", result["repeated"])
    print("Predictable Pattern:", result["has_pattern"])

    print("\n========== FINAL SCORE ==========")
    print("Password Score:", result["score"], "/ 100")
    print("Password Strength:", result["strength"])

    print("\n========== RECOMMENDATIONS ==========")

    if result["recommendations"]:
        for item in result["recommendations"]:
            print("-", item)
    else:
        print("No improvement suggestions from these basic checks.")

    print("\n====================================")
    print("       ANALYSIS COMPLETED")
    print("====================================")


if __name__ == "__main__":
    main()
