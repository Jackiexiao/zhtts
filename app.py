from pathlib import Path
from zhtts import TTS

tts = TTS(text2mel_name="FASTSPEECH2")
#tts = TTS(text2mel_name="TACOTRON")

import io
import time
from pathlib import Path
import scipy
from scipy.io import wavfile

from flask import Flask, Response, render_template, request
# from flask_cors import CORS

app = Flask("__name__")
# CORS(app)

@app.route("/api/tts")
def api_tts():
    text = request.args.get("text", "").strip()
    audio = tts.synthesis(text)

    with io.BytesIO() as out:
        wavfile.write(out, 24000, audio)
        return Response(out.getvalue(), mimetype="audio/wav")

@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
