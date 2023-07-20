import requests
from flask import request, jsonify


@app.route('/replicate_voice', methods=['POST'])
def replicate_voice():
    data = request.get_json()
    text = data.get('text')
    voice_id = data.get('voice_id')

    if not text or not voice_id:
        return jsonify({'error': 'Missing text or voice_id'}), 400

    try:
        audio_data = generate(text, voice_id)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'audio_data': audio_data}), 200
