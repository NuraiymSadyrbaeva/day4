import random

number = random.randint(1, 100)
guess = None
attempts = 0

print("Willkommen beim Zahlenraten!")

while guess != number:
    guess = int(input("Rate die Zahl zwischen 1 und 100: "))
    attempts += 1

    if guess < number:
        print("Zu niedrig! Versuche es erneut.")
    elif guess > number:
        print("Zu hoch! Versuche es erneut.")

print(f"Glückwunsch! Du hast die Zahl {number} erraten!")
print(f"Du hast {attempts} Versuche gebraucht.")
