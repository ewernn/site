document.addEventListener('DOMContentLoaded', function() {
    const sendButton = document.querySelector('.send-button');
    const chatInput = document.querySelector('.chat-input');
    const chatMessages = document.querySelector('.chat-messages');

    sendButton.addEventListener('click', function() {
        const message = chatInput.value;
        if (message.trim() !== '') {
            const messageElement = document.createElement('div');
            messageElement.textContent = message;
            chatMessages.appendChild(messageElement);
            chatInput.value = '';
        }
    });
});