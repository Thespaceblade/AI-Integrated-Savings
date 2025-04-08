// ...existing code...

// Fetch analysis data from the backend
async function fetchAnalysis() {
    const response = await fetch('https://capital-one-cc.onrender.com/api/analyze');
    const data = await response.json();

    if (data.analysis) {
        // Update summary
        document.getElementById('summary').textContent = data.analysis.summary;

        // Update advice list
        const adviceList = document.getElementById('advice-list');
        adviceList.innerHTML = ''; // Clear existing items
        data.analysis.advice.forEach((tip) => {
            const listItem = document.createElement('li');
            listItem.textContent = tip;
            adviceList.appendChild(listItem);
        });
    } else {
        console.error('Analysis data is missing:', data);
    }
}

// Trigger analysis on button click
document.getElementById('analyze-button').addEventListener('click', fetchAnalysis);

// ...existing code...