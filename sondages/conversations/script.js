// Configurer le mode d'envoi
const USE_GOOGLE_SHEETS = true; // true pour Google Sheets, false pour export CSV
const SHEET_ID = "1XnupnE_K4lFd3HK27vWZkGa4M9xHiC-nTKndki5k0EE"; // Remplacez par l'ID de votre Google Sheet
const API_URL = `https://sheets.googleapis.com/v4/spreadsheets/${SHEET_ID}/values/Sheet1!A1:append?valueInputOption=RAW`;
const API_KEY = "e7fd0eef23b53977fca0939924d886b9c7e19e34"; // Remplacez par votre clé API

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
                    <p><strong>Question (Recruteur) :</strong> ${pair.question}</p>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Notez la pertinence de la question (1-5) :
                    </label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="question-relevance-${index}" value="${num}"> ${num}
                        `).join(' ')}
                    </div>
                    <p><strong>Réponse (Candidat) :</strong> ${pair.answer}</p>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Cette interaction semble-t-elle réaliste ?
                    </label>
                    <div>
                        <input type="radio" name="realistic-${index}" value="Oui"> Oui
                        <input type="radio" name="realistic-${index}" value="Non"> Non
                    </div>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Notez la pertinence de la réponse (1-5) :
                    </label>
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
        const results = collectResults(pairs, fileName);
        if (USE_GOOGLE_SHEETS) {
            sendResultsToGoogleSheets(results);
        } else {
            exportResultsToCSV(results);
        }
    });
}

// Fonction pour collecter les résultats
function collectResults(pairs, fileName) {
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

    return results;
}

// Fonction pour envoyer les résultats à Google Sheets
function sendResultsToGoogleSheets(results) {
    const rows = results.map(row => [
        row.fileName,
        row.dateTime,
        row.exchange,
        row.realism,
        row.questionRelevance,
        row.answerRelevance
    ]);

    fetch(API_URL, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Authorization": `Bearer ${API_KEY}`
        },
        body: JSON.stringify({ values: rows })
    }).then(response => {
        if (response.ok) {
            alert("Résultats envoyés avec succès à Google Sheets !");
        } else {
            alert("Erreur lors de l'envoi des résultats à Google Sheets.");
        }
    });
}

// Fonction pour exporter les résultats en CSV
function exportResultsToCSV(results) {
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
