from flask import Flask, request, jsonify
<<<<<<< HEAD
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
=======
from .models import User, Podcast, Guest
from .voice_replication import replicate_voice
from .podcast_editing import edit_podcast
from .podcast_publishing import publish_podcast
from .user_profile import get_user_profile, update_user_profile
from .podcast_sharing import share_podcast
from .podcast_discovery import search_podcast

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # loginUser function implementation goes here
    pass

@app.route('/signup', methods=['POST'])
def signup():
    # signupUser function implementation goes here
    pass

@app.route('/editPodcast', methods=['POST'])
def edit():
    podcast_id = request.json.get('podcast_id')
    new_data = request.json.get('new_data')
    return jsonify(edit_podcast(podcast_id, new_data))

@app.route('/publishPodcast', methods=['POST'])
def publish():
    podcast_id = request.json.get('podcast_id')
    return jsonify(publish_podcast(podcast_id))

@app.route('/sharePodcast', methods=['POST'])
def share():
    podcast_id = request.json.get('podcast_id')
    platform = request.json.get('platform')
    return jsonify(share_podcast(podcast_id, platform))

@app.route('/searchPodcast', methods=['GET'])
def search():
    query = request.args.get('query')
    return jsonify(search_podcast(query))

@app.route('/userProfile', methods=['GET', 'POST'])
def user_profile():
    if request.method == 'GET':
        user_id = request.args.get('user_id')
        return jsonify(get_user_profile(user_id))
    elif request.method == 'POST':
        user_id = request.json.get('user_id')
        new_data = request.json.get('new_data')
        return jsonify(update_user_profile(user_id, new_data))
>>>>>>> 94b59ec (Add changes)
