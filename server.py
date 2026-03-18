from flask import Flask,request,jsonify,render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_web():
    text = request.args.get("text") or request.args.get("textToAnalyze")

    if not text:
        return jsonify({"error" : "No Text Provided"}) , 400
    
    result = emotion_detector(text)

    response_text =(
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
    return render_template("index.html")


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port = 5000)