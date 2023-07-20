from flask import Blueprint, request, jsonify
from .models import Podcast, db

podcast_editing = Blueprint('podcast_editing', __name__)

@podcast_editing.route('/editPodcast', methods=['POST'])
def edit_podcast():
    data = request.get_json()
    podcast_id = data.get('podcastId')
    new_title = data.get('newTitle')
    new_description = data.get('newDescription')

    podcast = Podcast.query.get(podcast_id)
    if not podcast:
        return jsonify({"error": "Podcast not found"}), 404

    podcast.title = new_title
    podcast.description = new_description
    db.session.commit()

    return jsonify({"message": "Podcast updated successfully"}), 200