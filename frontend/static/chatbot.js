function toggleChat() {
    const bot = document.getElementById("chatbot");
    bot.style.display = bot.style.display === "flex" ? "none" : "flex";
}

function sendMessage() {
    const input = document.getElementById("chatInput");
    const message = input.value.trim();
    if (!message) return;

    addMessage(message, "user");
    input.value = "";

    fetch("/chatbot/chat/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message }),
    })
    .then(res => res.json())
    .then(data => {
        addMessage(data.reply, "bot");
    });
}

function addMessage(text, sender) {
    const body = document.getElementById("chatBody");
    const msg = document.createElement("div");
    msg.className = sender === "user" ? "user-msg" : "bot-msg";
    msg.innerText = text;
    body.appendChild(msg);
    body.scrollTop = body.scrollHeight;
}
