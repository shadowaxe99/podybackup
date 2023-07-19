from flask import Flask, request, jsonify
from models import db, User
from openai_function_call import stream_extract
from voice_replicator import replicate_voice

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data['name']
    age = data['age']
    user = User(name=name, age=age)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User created'}), 201

@app.route('/podcast', methods=['POST'])
def create_podcast():
    data = request.get_json()
    input_text = data['input_text']
    users = stream_extract(input_text)
    for user in users:
        voice = replicate_voice(user.name)
        # Add more functionality here to create the podcast
    return jsonify({'message': 'Podcast created'}), 201

if __name__ == "__main__":
    app.run(debug=True)