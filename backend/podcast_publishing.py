from flask import Blueprint, request, jsonify
from flask_uploads import UploadSet, configure_uploads, IMAGES
from models import Podcast, db
from werkzeug.utils import secure_filename
import os

podcast_publishing = Blueprint('podcast_publishing', __name__)

photos = UploadSet('photos', IMAGES)
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app, photos)

@app.route('/publishPodcast', methods=['POST'])
def publish_podcast():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400
    if file and photos.file_allowed(file, file.filename):
        filename = photos.save(file)
        podcast = Podcast.query.filter_by(id=request.form['podcastId']).first()
        if podcast:
            podcast.artwork = photos.url(filename)
            podcast.title = request.form['title']
            podcast.description = request.form['description']
            db.session.commit()
            return jsonify({"message": "Podcast published successfully"}), 200
        else:
            return jsonify({"message": "Podcast not found"}), 404
    else:
        return jsonify({"message": "File not allowed"}), 400
