from flask import Flask

app = Flask(__name__)

jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer catch a cold? It had a bad Windows!",
        "What falls, but never needs a bandage? The rain.",
        "I was going to tell you a joke about boxing but I forgot the punch line.",
        "I'm not a fan of spring cleaning. Let's be honest, I'm not into summer, fall, or winter cleaning either.",
        "Why did the egg hide? It was a little chicken.",
        "What did the dirt say to the rain? If you keep this up, my name will be mud!",
        "Why couldn't the sunflower ride its bike? It lost its petals.",
        "What's an egg's favorite vacation spot? New Yolk City.",
        "I ate a sock yesterday. It was very time-consuming.",
        "What kind of candy do astronauts like? Mars bars.",
        "I wanted to buy some camo pants but couldn't find any."
    # Add more jokes here
]

@app.route("/")
def index():
    return "Welcome to the funny app!"

@app.route("/random_joke")
# def random_joke():
#     import random
#     return random.choice(jokes)
def generate_random_joke():
    import random
    return random.choice(jokes)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
