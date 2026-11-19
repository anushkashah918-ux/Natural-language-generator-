# INTELLIWRITE - NATURAL LANGUAGE GENERATOR

import random

print("=" * 55)
print("          INTELLIWRITE - SMART WRITING AI")
print("=" * 55)

print("\nWelcome to IntelliWrite!")

print("\nChoose your writing task:")
print("1. Professional Paragraph")
print("2. Business Email")
print("3. Motivational Message")

choice = input("\nEnter your choice (1-3): ")

print("\nChoose your writing tone:")
print("1. Professional")
print("2. Friendly")
print("3. Formal")
print("4. Creative")

tone_choice = input("\nSelect tone (1-4): ")

tones = {
    "1": "professional",
    "2": "friendly",
    "3": "formal",
    "4": "creative"
}

if tone_choice not in tones:
    print("Invalid tone selection!")
    exit()

tone = tones[tone_choice]

if choice == "1":

    topic = input("\nEnter your topic: ")

    templates = {
        "professional": [

            f"{topic} plays a significant role in achieving organizational growth and improving productivity.",
            f"{topic} offers valuable opportunities for innovation, development, and long-term success."
        ],
        "friendly": [
            f"Let's talk about {topic}! It can make a real difference and open up exciting opportunities.",
            f"{topic} is something worth exploring. It can help us learn, grow, and achieve more."
        ],
        "formal": [
            f"{topic} is an important subject that contributes significantly to development and progress.",
            f"The importance of {topic} can be observed across various areas of professional and personal development."
        ],
        "creative": [
            f"Imagine a world shaped by {topic}, where every new idea opens a door to endless possibilities!",
            f"{topic} is more than just an idea; it is an opportunity to transform possibilities into achievements."
        ]
    }

    print("\nGENERATED PARAGRAPH:")
    print(random.choice(templates[tone]))

elif choice == "2":

    name = input("\nEnter recipient's name: ")
    purpose = input("Enter email purpose: ")

    greetings = {
        "professional": "I hope this message finds you well.",
        "friendly": "Hope you're having a wonderful day!",
        "formal": "I trust this correspondence finds you in good health.",
        "creative": "I am delighted to connect with you today."
    }

    print("\nGENERATED EMAIL:")
    print("Subject:", purpose)
    print("\nDear", name + ",")
    print("\n" + greetings[tone])
    print(f"I am writing to you regarding {purpose}.")
    print("I look forward to your response.")
    print("\nBest regards,")
    print("Your Name")

elif choice == "3":

    messages = {
        "professional": [
            "Consistency and dedication are the foundations of success.",
            "Every challenge is an opportunity to demonstrate your capabilities."
        ],
        "friendly": [
            "Keep smiling! You're doing better than you think.",
            "Believe in yourself. You've got this!"
        ],
        "formal": [
            "Persistence and determination are essential qualities for achievement.",
            "Every meaningful accomplishment begins with commitment and effort."
        ],
        "creative": [
            "Be the author of your dreams and the hero of your journey!",
            "Let your courage shine brighter than your fears."
        ]
    }

    print("\nYOUR MOTIVATIONAL MESSAGE:")
    print(random.choice(messages[tone]))

else:
    print("\nInvalid task selection!")

print("\nThank you for using IntelliWrite!")