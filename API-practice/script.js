document.addEventListener("DOMContentLoaded", () => {
    const apiKey = "GRbfPn6KZjX4CH2h3NIltQyUm8i4r0Oidxd4SjyF";
    const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;

    // use fetch()
    fetch(apiUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            // Process the data and update the DOM
            displayAPOD(data);
        })
        .catch(error => {
            console.error("Fetch error:", error);
        });
});

function displayAPOD(data) {
    const apodImage = document.getElementById("apod-image");
    const apodTitle = document.getElementById("apod-title");
    const apodExplanation = document.getElementById("apod-explanation");

    // Update DOM with APOD data
    apodImage.src = data.url;
    apodTitle.textContent = data.title;
    apodExplanation.textContent = data.explanation;
}