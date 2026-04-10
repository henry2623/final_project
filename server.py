"""
Emotion Detection Web Application using Flask
This module provides a web interface for emotion analysis using IBM Watson NLP.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page.

    Returns:
        str: Rendered HTML template for the index page
    """
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    """
    Process the text input and return emotion analysis results.

    Retrieves the 'textToAnalyze' parameter from the request,
    calls the emotion detection function, and formats the response.

    Returns:
        str: Formatted emotion analysis results or error message
    """
    # Get the text from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Call the emotion detector function
    result = emotion_detector(text_to_analyze)

    # Error handling for blank input or invalid text
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format the response as required
    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    