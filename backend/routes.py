from flask import Flask, request, jsonify
from models import User
from openai_function_call import stream_extract
from voice_replicator import replicate_voice

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(name=data['name'], age=data['age'])
    user.save()
    return jsonify(user.to_dict()), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users]), 200

@app.route('/podcast/start', methods=['POST'])
def start_podcast():
    data = request.get_json()
    users = stream_extract(data['users'])
    for user in users:
        replicate_voice(user.name)
    return jsonify({'message': 'Podcast started'}), 200

if __name__ == "__main__":
    app.run(debug=True)