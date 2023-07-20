from flask import Blueprint, request, jsonify
from models import Podcast, db
from werkzeug.utils import secure_filename
import os

podcast_publishing = Blueprint('podcast_publishing', __name__)

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@podcast_publishing.route('/publishPodcast', methods=['POST'])
def publish_podcast():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        podcast = Podcast.query.filter_by(id=request.form['podcastId']).first()
        if podcast:
            podcast.artwork = os.path.join(UPLOAD_FOLDER, filename)
            podcast.title = request.form['title']
            podcast.description = request.form['description']
            db.session.commit()
            return jsonify({"message": "Podcast published successfully"}), 200
        else:
            return jsonify({"message": "Podcast not found"}), 404
    else:
        return jsonify({"message": "File not allowed"}), 400