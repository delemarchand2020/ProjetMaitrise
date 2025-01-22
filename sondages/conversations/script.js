let selectedFile;
let remainingFiles = [];
let evaluatedFiles = new Set(); // Garde trace des fichiers évalués

// Fonction pour initialiser les fichiers disponibles
function initializeConversationFiles() {
    remainingFiles = [];
    let i = 1;

    // Rechercher les fichiers disponibles
    while (true) {
        const fileName = `conversation_${i}.json`;

        try {
            const request = new XMLHttpRequest();
            request.open('HEAD', fileName, false);
            request.send();

            if (request.status === 404) break; // Arrêter si le fichier n'existe pas
            remainingFiles.push(fileName);
            i++;
        } catch {
            break;
        }
    }

    evaluatedFiles.clear(); // Réinitialiser les fichiers évalués
}

// Tirer une conversation sans remise
function getNextConversationFile() {
    if (remainingFiles.length === 0) {
        alert("Toutes les entrevues ont été évaluées. Merci pour votre participation !");
        return null;
    }
    const randomIndex = Math.floor(Math.random() * remainingFiles.length);
    const selected = remainingFiles.splice(randomIndex, 1)[0]; // Retirer le fichier tiré
    return selected;
}

// Charger une nouvelle entrevue
function loadConversation() {
    selectedFile = getNextConversationFile();
    if (!selectedFile) return; // Arrêter si aucun fichier n'est disponible
    fetch(selectedFile)
        .then(response => response.json())
        .then(data => generateQuestionAnswerPairs(data, selectedFile));
}

// Réinitialiser le formulaire
function resetForm() {
    initializeConversationFiles();
    loadConversation();
}

// Fonction pour générer les paires question-réponse
function generateQuestionAnswerPairs(conversations, fileName) {
    const container = document.getElementById('questions-container');
    container.innerHTML = ""; // Réinitialiser le contenu
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
                    <p><strong>Question (recruteur) :</strong> ${pair.question}</p>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Notez la pertinence de la question (1-5) :
                    </label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="question-relevance-${index}" value="${num}" required> ${num}
                        `).join(' ')}
                    </div>
                    <p><strong>Réponse (candidat) :</strong> ${pair.answer}</p>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Notez la pertinence de la réponse (1-5) :
                    </label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="answer-relevance-${index}" value="${num}" required> ${num}
                        `).join(' ')}
                    </div>
                    <label style="background-color: #fffacd; padding: 5px; border-radius: 5px;">
                        Cette interaction semble-t-elle réaliste ?
                    </label>
                    <div>
                        <input type="radio" name="realistic-${index}" value="Oui" required> Oui
                        <input type="radio" name="realistic-${index}" value="Non" required> Non
                    </div>
                </div>
            </div>`;
        container.insertAdjacentHTML('beforeend', questionAnswerHTML);
    });

    document.getElementById('submit-button').addEventListener('click', () => {
        if (evaluatedFiles.has(fileName)) {
            alert("Cette entrevue a déjà été exportée. Veuillez changer d'entrevue.");
            return;
        }
        const results = collectResults(pairs, fileName);
        exportResultsToCSV(results);
        evaluatedFiles.add(fileName); // Marquer ce fichier comme évalué
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

// Fonction pour exporter les résultats en CSV avec le nom de la conversation
function exportResultsToCSV(results) {
    const csvHeader = "Nom du fichier JSON,Date et Heure,Numéro échange,Note pertinence question,Note pertinence réponse,Réalisme interaction\n";
    const csvContent = csvHeader + results.map(row =>
        `${row.fileName},${row.dateTime},${row.exchange},${row.questionRelevance},${row.answerRelevance},${row.realism}`
    ).join('\n');

    // Utiliser le nom du fichier de la conversation dans le nom du fichier CSV
    const fileName = results[0]?.fileName?.replace('.json', '') || 'resultats';
    const encodedUri = "data:text/csv;charset=utf-8," + encodeURIComponent(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `${fileName}_evaluation.csv`);
    document.body.appendChild(link);
    link.click();
}


// Initialisation
initializeConversationFiles();
document.getElementById('change-conversation').addEventListener('click', loadConversation);
document.getElementById('reset-form').addEventListener('click', resetForm);
loadConversation();
