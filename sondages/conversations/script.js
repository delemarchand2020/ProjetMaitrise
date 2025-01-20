// Charger les données JSON
fetch('conversation_1.json')
    .then(response => response.json())
    .then(data => generateQuestionAnswerPairs(data, 'conversation_1.json'));

// Fonction pour générer les paires question-réponse
function generateQuestionAnswerPairs(conversations, fileName) {
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
                    <p style="background-color: #fffacd; padding: 10px; border-radius: 5px;">
                        <strong>Question (Recruteur) :</strong> ${pair.question}
                    </p>
                    <label>Notez la pertinence de la question (1-5) :</label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="question-relevance-${index}" value="${num}"> ${num}
                        `).join(' ')}
                    </div>
                    <p><strong>Réponse (Candidat) :</strong> ${pair.answer}</p>
                    <label>Cette interaction semble-t-elle réaliste ?</label>
                    <div>
                        <input type="radio" name="realistic-${index}" value="Oui"> Oui
                        <input type="radio" name="realistic-${index}" value="Non"> Non
                    </div>
                    <label>Notez la pertinence de la réponse (1-5) :</label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="answer-relevance-${index}" value="${num}"> ${num}
                        `).join(' ')}
                    </div>
                </div>
            </div>`;
        container.insertAdjacentHTML('beforeend', questionAnswerHTML);
    });

    // Ajouter l'événement d'exportation des résultats
    document.getElementById('submit-button').addEventListener('click', () => {
        exportResults(pairs, fileName);
    });
}

// Fonction pour exporter les résultats en CSV
function exportResults(pairs, fileName) {
    const results = [];
    const dateTime = new Date().toISOString();

    document.querySelectorAll('.card').forEach((card, index) => {
        const realistic = document.querySelector(`input[name="realistic-${index}"]:checked`);
        const questionRelevance = document.querySelector(`input[name="question-relevance-${index}"]:checked`);
        const answerRelevance = document.querySelector(`input[name="answer-relevance-${index}"]:checked`);
        results.push({
            fileName: fileName,
            dateTime: dateTime,
            exchange: index + 1,
            realism: realistic ? realistic.value : 'Non répondu',
            questionRelevance: questionRelevance ? questionRelevance.value : 'Non répondu',
            answerRelevance: answerRelevance ? answerRelevance.value : 'Non répondu'
        });
    });

    // Convertir en CSV
    const csvHeader = "Nom du fichier JSON,Date et Heure,Numéro échange,Réalisme interaction,Note pertinence question,Note pertinence réponse\n";
    const csvContent = csvHeader + results.map(row =>
        `${row.fileName},${row.dateTime},${row.exchange},${row.realism},${row.questionRelevance},${row.answerRelevance}`
    ).join('\n');

    const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "results.csv");
    document.body.appendChild(link);
    link.click();
}
