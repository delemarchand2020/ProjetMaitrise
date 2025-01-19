// Charger les données JSON
fetch('conversation_1.json')
    .then(response => response.json())
    .then(data => generateQuestions(data));

// Générer les questions
function generateQuestions(conversations) {
    const container = document.getElementById('questions-container');
    conversations.forEach((conv, index) => {
        const questionHTML = `
            <div class="card mb-3">
                <div class="card-body">
                    <h5>Conversation ${index + 1}</h5>
                    <p><strong>Question :</strong> ${conv.role === 'Recruteur' ? conv.message : ''}</p>
                    <label>Cette conversation semble-t-elle réaliste ?</label>
                    <div>
                        <input type="radio" name="realistic-${index}" value="Oui"> Oui
                        <input type="radio" name="realistic-${index}" value="Non"> Non
                    </div>
                    <label>Notez la fluidité des échanges (1-5) :</label>
                    <div>
                        ${[1, 2, 3, 4, 5].map(num => `
                            <input type="radio" name="fluency-${index}" value="${num}"> ${num}
                        `).join(' ')}
                    </div>
                </div>
            </div>`;
        container.insertAdjacentHTML('beforeend', questionHTML);
    });
}

// Exporter les résultats
document.getElementById('submit-button').addEventListener('click', () => {
    const results = [];
    document.querySelectorAll('.card').forEach((card, index) => {
        const realistic = document.querySelector(`input[name="realistic-${index}"]:checked`);
        const fluency = document.querySelector(`input[name="fluency-${index}"]:checked`);
        results.push({
            conversation: index + 1,
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
