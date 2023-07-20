from flask import Flask, request, jsonify
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
