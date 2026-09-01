"""Flask Server for Emotion Detection Application"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the main page"""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Handle emotion detection request"""
    text_to_analyze = request.args.get("textToAnalyze")

    # Task 7: Error handling for blank input
    if not text_to_analyze or text_to_analyze.strip() == "":
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # Task 7: Handle None response for invalid input
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
