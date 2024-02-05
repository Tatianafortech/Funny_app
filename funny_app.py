from flask import Flask
import time
import random

app = Flask(__name__)

# jokes = [
#     "Why don't scientists trust atoms? Because they make up everything!",
#     "Why did the computer catch a cold? It had a bad Windows!",
#     # Add more jokes here
# ]

# @app.route("/")
# def index():
#     return "Welcome to the funny app!"

# @app.route("/random_joke")
# def random_joke():
#     import random
#     return random.choice(jokes)


def generate_random_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Did you hear about the mathematician who's afraid of negative numbers? He will stop at nothing to avoid them!",
        # Add more jokes to the list
    ]
    return random.choice(jokes)

while True:
    # Generate a random joke and write it to a file (e.g., data.json)
    with open('data.json', 'w') as file:
        file.write(f'{{"message": "{generate_random_joke()}"}}')

    # Sleep for a period (adjust as needed)
    time.sleep(60)  # Sleep for 60 seconds before generating the next joke
    
if __name__ == "__main__":
    app.run(debug=True)
