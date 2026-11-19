from flask import Flask, render_template_string
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Пранк 😈</h2>
    <p>Нажми кнопку и разреши доступ к камере. Видео будет передаваться только с твоего согласия.</p>
    <button onclick="startCamera()">Включить камеру</button>
    <video id="video" autoplay playsinline></video>
    <script>
    async function startCamera() {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({video: true});
            document.getElementById("video").srcObject = stream;
        } catch (e) {
            alert("Камера не разрешена");
        }
    }
    </script>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
