// Helper function to update card content
function updateCard(cardType, content) {
    const cardBack = document.getElementById(`${cardType}-card-back`);
    cardBack.innerHTML = `<p>${content}</p>`;
}

// Fetch and update Event Card content
function drawEventCard() {
    fetch('/draw-event-card')
        .then(response => response.json())
        .then(data => {
            updateCard('event', data.card);
            flipCard('.event-card');
        })
        .catch(error => console.error('Error fetching event card:', error));
}

// Fetch and update Supply Card content
function drawSupplyCard() {
    fetch('/draw-supply-card')
        .then(response => response.json())
        .then(data => {
            updateCard('supply', data.card);
            flipCard('.supply-card');
        })
        .catch(error => console.error('Error fetching supply card:', error));
}

// Fetch and update Disease Card content
function drawDiseaseCard() {
    fetch('/draw-disease-card')
        .then(response => response.json())
        .then(data => {
            updateCard('disease', data.card);
            flipCard('.disease-card');
        })
        .catch(error => console.error('Error fetching disease card:', error));
}

// Flip card on click
function flipCard(cardSelector) {
    const card = document.querySelector(cardSelector);
    card.classList.toggle('is-flipped');
}

// Add click event listeners to cards
document.querySelector('.event-card').addEventListener('click', drawEventCard);
document.querySelector('.supply-card').addEventListener('click', drawSupplyCard);
document.querySelector('.disease-card').addEventListener('click', drawDiseaseCard);
