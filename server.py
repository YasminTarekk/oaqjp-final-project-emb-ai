"""
server.py
Flask web server for Emotion Detection application.
Provides an endpoint to analyze text and return dominant emotion.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_web():
    """
    Flask route for detecting emotions from user input.
    Accepts 'text' or 'textToAnalyze' as query parameters.
    Returns a formatted string with emotion scores or
    an error message for invalid input.
    """
    text = request.args.get("text") or request.args.get("textToAnalyze")
    result = emotion_detector(text)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text


@app.route("/")
def home():
    """
    Flask route to render the home page.
    Returns the index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Run the Flask server
    app.run(debug=True, host="0.0.0.0", port=5000)
