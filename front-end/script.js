function setMessage(text) {
  document.getElementById("message").value = text;
  document.getElementById("message").focus();
}

function clearChat() {
  document.getElementById("message").value = "";
  document.getElementById("response").textContent = "A resposta aparecerá aqui.";
  document.getElementById("loading").style.display = "none";
  document.getElementById("message").focus();
}

async function sendMessage() {
  const message = document.getElementById("message").value;
  const responseBox = document.getElementById("response");
  const loading = document.getElementById("loading");

  if (!message.trim()) return;

  loading.style.display = "block";
  responseBox.textContent = "";

  try {
    const res = await fetch("http://127.0.0.1:8000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        session_id: "1",
        message: message
      })
    });

    const data = await res.json();
    responseBox.textContent = data.answer || JSON.stringify(data, null, 2);

  } catch (err) {
    responseBox.textContent = "Erro ao conectar com a API.";
  }

  loading.style.display = "none";
}