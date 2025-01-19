// Charger les données JSON
fetch('conversation_1.json')
    .then(response => response.json())
    .then(data => generateQuestionAnswerPairs(data));

// Fonction pour générer les paires question-réponse
function generateQuestionAnswerPairs(conversations) {
    const container = document.getElementById('questions-container');
    const pairs = [];

    // Extraire les paires question-réponse
    for (let i = 0; i < conversations.length - 1; i++) {
        if (conversations[i].role === "Recruteur" && conversations[i + 1].role === "Candidat") {
            pairs.push({
                question: conversations[i].message,
                answer: conversations[i + 1].message
            });
        }
    }

    // Générer l'interface utilisateur
    pairs.forEach((pair, index) => {
        const questionAnswerHTML = `
            <div class="card mb-3">
                <div class="card-body">
                    <h5>Échange ${index + 1}</h5>
                    <p><strong>Question (Recruteur) :</strong> ${pair.question}</p>
                    <p><strong>Réponse (Candidat) :</strong> ${pair.answer}</p>
                    <label>Cette interaction semble-t-elle réaliste ?</label>
                    <div>
                        <input type="radio" name="realistic-${index}" value="Oui"> Oui
                        <input type="radio" name="realistic-${index}" value="Non"> Non
                    </div>
                    <label>Notez la pertinence de la réponse (1-5) :</label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="fluency-${index}" value="${num}"> ${num}
                        `).join(' ')}
                    </div>
                </div>
            </div>`;
        container.insertAdjacentHTML('beforeend', questionAnswerHTML);
    });
}

// Exporter les résultats
document.getElementById('submit-button').addEventListener('click', () => {
    const results = [];
    document.querySelectorAll('.card').forEach((card, index) => {
        const realistic = document.querySelector(`input[name="realistic-${index}"]:checked`);
        const fluency = document.querySelector(`input[name="fluency-${index}"]:checked`);
        results.push({
            exchange: index + 1,
            realistic: realistic ? realistic.value : 'Non répondu',
            fluency: fluency ? fluency.value : 'Non répondu'
        });
    });

    // Convertir en CSV
    const csvContent = "data:text/csv;charset=utf-8,"
        + results.map(row => Object.values(row).join(',')).join('\n');
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "results.csv");
    document.body.appendChild(link);
    link.click();
});
