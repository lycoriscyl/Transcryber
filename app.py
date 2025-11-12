from flask import Flask, request, jsonify
from transcriber import transcribe_audio
import os

app = Flask(__name__)

@app.route('/transcribe', methods=['POST'])
def transcribe_endpoint():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file:
        # Save the file to a temporary location
        # In a production environment, you'd want a more robust solution
        # for handling temporary files.
        temp_path = os.path.join('/tmp', file.filename)
        file.save(temp_path)
        try:
            transcription = transcribe_audio(temp_path)
            return jsonify({'transcription': transcription})
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Clean up the temporary file
            if os.path.exists(temp_path):
                os.remove(temp_path)

if __name__ == '__main__':
    app.run(debug=True)
