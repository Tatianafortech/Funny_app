import random

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
        "I wanted to buy some camo pants but couldn't find any.",
    # Add more jokes here
]

random_joke = random.choice(jokes)

with open("docs/index.html", "w") as f:
    f.write(f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="styles.css">
        <title>GitHub Pages Joke App</title>
    </head>
    <body>

        <h1>Hello, World!</h1>
        <p>{random_joke}</p> <!-- Display the random joke -->

        <script src="script.js"></script>
    </body>
    </html>
    """)
