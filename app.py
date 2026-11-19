import os
from flask import Flask, render_template_string
from flask_socketio import SocketIO, emit, join_room

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this")
socketio = SocketIO(app, cors_allowed_origins=[])

PAGE = """
<h2>Видеосвязь</h2>
<p>Камера включается только после нажатия кнопки и разрешения браузера.</p>
<button onclick="start()">Включить камеру</button>
<video id="video" autoplay playsinline muted style="width:320px"></video>
<script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
<script>
const socket = io();
async function start() {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({video:true, audio:false});
    document.getElementById('video').srcObject = stream;
    alert('Камера включена. Сейчас это только локальный просмотр.');
  } catch(e) {
    alert('Доступ к камере не предоставлен.');
  }
}
</script>
"""

@app.route("/")
def home():
    return PAGE

@app.route("/owner")
def owner():
    return "<h2>Страница владельца</h2><p>Видеопередача ещё не настроена.</p>"

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
