// script.js

document.addEventListener("DOMContentLoaded", function() {
    // Array of jokes
    var jokes = [
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
        // Add more jokes here
    ];

    // Function to display a random joke
    function displayRandomJoke() {
        var jokeContainer = document.getElementById("joke-container");
        var randomJoke = jokes[Math.floor(Math.random() * jokes.length)];
        jokeContainer.textContent = randomJoke;
    }

    // Display a random joke when the page loads
    displayRandomJoke();
});
