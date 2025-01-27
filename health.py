import random

def health_check():
    return random.choice([True] * 7 + [False] * 3)

def status_message():

    if health_check():
        return "Everything is good."
    else:
        error_messages = [
            "Aurora is down, please try again later.",
            "Aurora is unavailable, check back soon.",
            "Error: Aurora system is currently offline."
        ]
        return random.choice(error_messages)


print(status_message())
