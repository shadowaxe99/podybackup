from flask import Flask, request, jsonify
<<<<<<< HEAD
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
=======
from flask_cors import CORS
import models
import routes
import voice_replication
import podcast_editing
import podcast_publishing
import user_profile
import podcast_sharing
import podcast_discovery
import database_config
import openai_api
import eleven_labs_api

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    return routes.loginUser(request)

@app.route('/signup', methods=['POST'])
def signup():
    return routes.signupUser(request)

@app.route('/editPodcast', methods=['POST'])
def edit_podcast():
    return podcast_editing.edit_podcast(request)

@app.route('/publishPodcast', methods=['POST'])
def publish_podcast():
    return podcast_publishing.publish_podcast(request)

@app.route('/sharePodcast', methods=['POST'])
def share_podcast():
    return podcast_sharing.share_podcast(request)

@app.route('/searchPodcast', methods=['GET'])
def search_podcast():
    return podcast_discovery.search_podcast(request)

if __name__ == '__main__':
>>>>>>> 94b59ec (Add changes)
    app.run(debug=True)