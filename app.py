from flask import Flask, render_template, request, jsonify
import speech_recognition as sr

# Initialize Flask app
app = Flask(__name__)

# Command mapping for actcion
COMMANDS = {
    "move forward": "FORWARD",
    "move backward": "BACKWARD",
    "turn left": "LEFT",
    "turn right": "RIGHT",
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/process_command', methods=['POST'])
def process_command():
    data = request.get_json()
    command_text = data.get("command", "").lower()
    
    for key in COMMANDS:
        if key in command_text:
            return jsonify({"action": COMMANDS[key]})
    
    return jsonify({"action": "UNKNOWN"})

if __name__ == '__main__':
    app.run(debug=True)
