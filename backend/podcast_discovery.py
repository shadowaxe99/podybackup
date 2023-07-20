from flask import request, jsonify
from models import Podcast, User
from database_config import db

@app.route('/searchPodcast', methods=['GET'])
def search_podcast():
    search_query = request.args.get('query')
    podcasts = Podcast.query.filter(Podcast.title.contains(search_query)).all()
    result = []
    for podcast in podcasts:
        result.append({
            'id': podcast.id,
            'title': podcast.title,
            'description': podcast.description,
            'host': User.query.get(podcast.host_id).username
        })
    return jsonify(result)

@app.route('/recommendPodcast', methods=['GET'])
def recommend_podcast():
    user_id = request.args.get('userId')
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    # For simplicity, recommend the most recent podcasts
    podcasts = Podcast.query.order_by(Podcast.created_at.desc()).limit(5).all()
    result = []
    for podcast in podcasts:
        result.append({
            'id': podcast.id,
            'title': podcast.title,
            'description': podcast.description,
            'host': User.query.get(podcast.host_id).username
        })
    return jsonify(result)