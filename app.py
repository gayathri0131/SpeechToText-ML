from flask import Flask, render_template, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("tiny")

UPLOAD_FOLDER = os.path.join(os.getcwd(), "uploads")
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert_audio():
    if "audio_file" not in request.files:
        return jsonify({"error": "No file"}), 400

    file = request.files["audio_file"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    result = model.transcribe(filepath)
    return jsonify({"text": result["text"]})


if __name__ == "__main__":
    app.run(debug=True)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
