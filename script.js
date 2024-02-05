document.addEventListener('DOMContentLoaded', function() {
    // This script is executed when the DOM is fully loaded

    // Fetch dynamic content from your Python app (replace with your logic)
    fetch('path/to/dynamic-data') // Adjust the URL accordingly
        .then(response => response.json())
        .then(data => {
            // Manipulate the DOM to display dynamic content
            const dynamicContentDiv = document.getElementById('dynamicContent');
            dynamicContentDiv.innerHTML = `<p>${data.message}</p>`; // Adjust as per your data structure
        })
        .catch(error => console.error('Error fetching dynamic data:', error));
});
