from flask import Flask, jsonify
import random
import os

app = Flask(__name__)

@app.route('/quote', methods=['GET'])
def get_quote():
    quotes = [
        "Stay positive and you'll see obstacles as stepping stones to greatness.",
        "The only limit to your impact is your imagination and commitment.",
        "Success is a journey filled with continuous learning and improvement.",
        "Your potential is endless. Go do what you were created to do.",
        "Small daily improvements lead to stunning results over time."
    ]
    return jsonify({"quote": random.choice(quotes)})

# Health check endpoint
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

# RunPod handler - this is crucial for serverless integration
@app.route('/', methods=['POST'])
def handler():
    """
    Main handler for RunPod serverless requests.
    RunPod serverless sends requests to the root path ('/'), not '/runsync'.
    """
    return jsonify({"output": get_quote().json})

# For backward compatibility with direct testing
@app.route('/runsync', methods=['POST'])
def runsync_handler():
    return handler()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
