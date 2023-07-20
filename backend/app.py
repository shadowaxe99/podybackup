from flask import Flask, request, jsonify
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
    app.run(debug=True)