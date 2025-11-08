async function sendMessage() {
  const msg = document.getElementById('message').value.trim();
  if (!msg) return;

  const chatBox = document.getElementById('chat');
  chatBox.innerHTML += `<p><b>You:</b> ${msg}</p>`;

  const res = await fetch('/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: msg })
  });

  const data = await res.json();
  chatBox.innerHTML += `<p><b>Bot:</b> ${data.reply}</p>`;
  chatBox.scrollTop = chatBox.scrollHeight;

  document.getElementById('message').value = '';
}

