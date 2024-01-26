app = Flask(__name__)

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the computer catch a cold? It had a bad Windows!",
    # Add more jokes here
]

@app.route("/")
def index():
    return "Welcome to the funny app!"

@app.route("/random_joke")
def random_joke():
    import random
    return random.choice(jokes)

if __name__ == "__main__":
    app.run(debug=True)
