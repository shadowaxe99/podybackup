from flask import Blueprint, request, jsonify
from .models import Podcast
from .user_profile import userProfile
import requests

podcast_sharing = Blueprint('podcast_sharing', __name__)

@podcast_sharing.route('/sharePodcast', methods=['POST'])
def share_podcast():
    data = request.get_json()
    podcast_id = data.get('podcastId')
    platform = data.get('platform')

    podcast = Podcast.query.get(podcast_id)
    if not podcast:
        return jsonify({'message': 'Podcast not found'}), 404

    user = userProfile.query.get(podcast.user_id)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    if platform == 'facebook':
        url = 'https://graph.facebook.com/v12.0/me/feed'
        params = {
            'message': f'Check out this podcast: {podcast.title}',
            'link': podcast.link,
            'access_token': user.authToken
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return jsonify({'message': 'Podcast shared successfully'}), 200
        else:
            return jsonify({'message': 'Failed to share podcast'}), 400

    elif platform == 'twitter':
        url = 'https://api.twitter.com/1.1/statuses/update.json'
        params = {
            'status': f'Check out this podcast: {podcast.title} {podcast.link}',
            'access_token': user.authToken
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            return jsonify({'message': 'Podcast shared successfully'}), 200
        else:
            return jsonify({'message': 'Failed to share podcast'}), 400

    else:
        return jsonify({'message': 'Unsupported platform'}), 400