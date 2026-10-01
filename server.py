"""Flask web deployment of the Emotion Detection application."""

from flask import Flask, render_template, request

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def home():
    """Render the application interface."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detector_route():
    """Analyze text and return a formatted emotion response."""
    if request.method == "POST":
        text_to_analyze = request.form.get("textToAnalyze", "")
        if not text_to_analyze and request.is_json:
            payload = request.get_json(silent=True) or {}
            text_to_analyze = payload.get("textToAnalyze", "")
    else:
        text_to_analyze = request.args.get("textToAnalyze", "")

    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return "Invalid input! Try again.", 400

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid input! Try again.", 400

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is '{result['dominant_emotion']}'."
    )
    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
