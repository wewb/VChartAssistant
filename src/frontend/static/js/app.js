let chatHistory = [];

async function sendMessage() {
    const input = document.getElementById('user-input');
    const message = input.value.trim();
    if (!message) return;

    appendMessage('user', message);
    input.value = '';

    try {
        const response = await fetch('/api/ask', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                text: message,
                chat_history: chatHistory
            })
        });

        const data = await response.json();
        if (response.ok) {
            appendMessage('assistant', data.answer);
            updateSources(data.sources);
            
            chatHistory.push(
                { role: 'user', content: message },
                { role: 'assistant', content: data.answer }
            );
        } else {
            throw new Error(data.error || 'Failed to get response');
        }
    } catch (error) {
        console.error('Error:', error);
        appendMessage('system', 'Error: ' + error.message);
    }
}

function appendMessage(role, content) {
    const messagesDiv = document.getElementById('chat-messages');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${role}`;
    messageDiv.textContent = content;
    messagesDiv.appendChild(messageDiv);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function updateSources(sources) {
    const sourcesDiv = document.getElementById('sources-container');
    sourcesDiv.innerHTML = '<h3>Related Sources:</h3>';
    sources.forEach((source, index) => {
        const sourceDiv = document.createElement('div');
        sourceDiv.className = 'source';
        sourceDiv.innerHTML = `<p>${source}</p>`;
        sourcesDiv.appendChild(sourceDiv);
    });
}

document.getElementById('user-input').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
}); 