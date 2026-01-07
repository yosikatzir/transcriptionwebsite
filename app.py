#!/usr/bin/env python3
"""
Flask backend for Transcription Editor
Handles file operations and meeting management
"""

from flask import Flask, render_template, request, jsonify, send_file
from werkzeug.utils import secure_filename
import os
import json
import datetime
from pathlib import Path
import shutil

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max file size
app.config['MEETINGS_FOLDER'] = os.path.join(os.path.dirname(__file__), 'meetings')

# Ensure meetings folder exists
os.makedirs(app.config['MEETINGS_FOLDER'], exist_ok=True)

ALLOWED_AUDIO_EXTENSIONS = {'wav', 'mp3', 'm4a', 'ogg', 'flac'}

def allowed_audio_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_AUDIO_EXTENSIONS

def get_meeting_status(meeting_folder):
    """Determine meeting status based on files present"""
    has_audio = any(f.endswith(('.wav', '.mp3', '.m4a', '.ogg', '.flac'))
                    for f in os.listdir(meeting_folder))
    has_transcription = os.path.exists(os.path.join(meeting_folder, 'transcription.json'))
    has_edited = os.path.exists(os.path.join(meeting_folder, 'transcription_edited.json'))

    if has_edited:
        return 'edited'
    elif has_transcription:
        return 'transcribed'
    elif has_audio:
        return 'submitted'
    else:
        return 'unknown'

@app.route('/')
def index():
    """Landing page"""
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    """Meeting upload page"""
    return render_template('upload.html')

@app.route('/meetings')
def meetings_page():
    """Meeting list page"""
    return render_template('meetings.html')

@app.route('/editor/<meeting_id>')
def editor_page(meeting_id):
    """Transcription editor page"""
    return render_template('editor.html', meeting_id=meeting_id)

@app.route('/api/meetings', methods=['GET'])
def get_meetings():
    """Get list of all meetings"""
    meetings = []
    meetings_folder = app.config['MEETINGS_FOLDER']

    if os.path.exists(meetings_folder):
        for folder_name in os.listdir(meetings_folder):
            folder_path = os.path.join(meetings_folder, folder_name)
            if os.path.isdir(folder_path):
                info_file = os.path.join(folder_path, 'meeting_info.json')
                if os.path.exists(info_file):
                    with open(info_file, 'r', encoding='utf-8') as f:
                        meeting_info = json.load(f)
                        meeting_info['id'] = folder_name
                        meeting_info['status'] = get_meeting_status(folder_path)
                        meetings.append(meeting_info)

    # Sort by date, most recent first
    meetings.sort(key=lambda x: x.get('date', ''), reverse=True)
    return jsonify(meetings)

@app.route('/api/meeting/<meeting_id>', methods=['GET'])
def get_meeting(meeting_id):
    """Get specific meeting details"""
    meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))

    if not os.path.exists(meeting_folder):
        return jsonify({'error': 'Meeting not found'}), 404

    info_file = os.path.join(meeting_folder, 'meeting_info.json')
    if not os.path.exists(info_file):
        return jsonify({'error': 'Meeting info not found'}), 404

    with open(info_file, 'r', encoding='utf-8') as f:
        meeting_info = json.load(f)

    meeting_info['id'] = meeting_id
    meeting_info['status'] = get_meeting_status(meeting_folder)

    # Check for transcription files
    transcription_file = os.path.join(meeting_folder, 'transcription.json')
    edited_file = os.path.join(meeting_folder, 'transcription_edited.json')

    meeting_info['has_transcription'] = os.path.exists(transcription_file)
    meeting_info['has_edited'] = os.path.exists(edited_file)

    # Get audio file name
    audio_files = [f for f in os.listdir(meeting_folder)
                   if f.endswith(('.wav', '.mp3', '.m4a', '.ogg', '.flac'))]
    meeting_info['audio_file'] = audio_files[0] if audio_files else None

    return jsonify(meeting_info)

@app.route('/api/meeting/<meeting_id>/transcription', methods=['GET'])
def get_transcription(meeting_id):
    """Get transcription for a meeting"""
    meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))

    # Try edited version first, then original
    edited_file = os.path.join(meeting_folder, 'transcription_edited.json')
    original_file = os.path.join(meeting_folder, 'transcription.json')

    transcription_file = edited_file if os.path.exists(edited_file) else original_file

    if not os.path.exists(transcription_file):
        return jsonify({'error': 'Transcription not found'}), 404

    with open(transcription_file, 'r', encoding='utf-8') as f:
        transcription = json.load(f)

    return jsonify({
        'transcription': transcription,
        'is_edited': os.path.exists(edited_file)
    })

@app.route('/api/meeting/<meeting_id>/transcription/original', methods=['GET'])
def get_original_transcription(meeting_id):
    """Get original transcription for a meeting"""
    meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))
    original_file = os.path.join(meeting_folder, 'transcription.json')

    if not os.path.exists(original_file):
        return jsonify({'error': 'Original transcription not found'}), 404

    with open(original_file, 'r', encoding='utf-8') as f:
        transcription = json.load(f)

    return jsonify({'transcription': transcription})

@app.route('/api/meeting/<meeting_id>/audio', methods=['GET'])
def get_audio(meeting_id):
    """Get audio file for a meeting"""
    meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))

    audio_files = [f for f in os.listdir(meeting_folder)
                   if f.endswith(('.wav', '.mp3', '.m4a', '.ogg', '.flac'))]

    if not audio_files:
        return jsonify({'error': 'Audio file not found'}), 404

    audio_path = os.path.join(meeting_folder, audio_files[0])
    return send_file(audio_path)

@app.route('/api/meeting', methods=['POST'])
def create_meeting():
    """Create a new meeting"""
    try:
        # Get form data
        meeting_date = request.form.get('date')
        speakers = request.form.get('speakers', '')
        custom_words = request.form.get('custom_words', '')

        if not meeting_date:
            return jsonify({'error': 'Meeting date is required'}), 400

        # Get audio file
        if 'audio' not in request.files:
            return jsonify({'error': 'Audio file is required'}), 400

        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No audio file selected'}), 400

        if not allowed_audio_file(audio_file.filename):
            return jsonify({'error': 'Invalid audio file format'}), 400

        # Create meeting folder
        meeting_id = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], meeting_id)
        os.makedirs(meeting_folder, exist_ok=True)

        # Save audio file
        filename = secure_filename(audio_file.filename)
        audio_path = os.path.join(meeting_folder, filename)
        audio_file.save(audio_path)

        # Save meeting info
        meeting_info = {
            'date': meeting_date,
            'speakers': [s.strip() for s in speakers.split(',') if s.strip()],
            'custom_words': [w.strip() for w in custom_words.split(',') if w.strip()],
            'created_at': datetime.datetime.now().isoformat(),
            'audio_filename': filename
        }

        info_path = os.path.join(meeting_folder, 'meeting_info.json')
        with open(info_path, 'w', encoding='utf-8') as f:
            json.dump(meeting_info, f, indent=2, ensure_ascii=False)

        return jsonify({
            'success': True,
            'meeting_id': meeting_id,
            'message': 'Meeting created successfully'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/meeting/<meeting_id>/save', methods=['POST'])
def save_transcription(meeting_id):
    """Save edited transcription"""
    try:
        data = request.get_json()
        transcription = data.get('transcription')

        if not transcription:
            return jsonify({'error': 'Transcription data is required'}), 400

        meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))

        if not os.path.exists(meeting_folder):
            return jsonify({'error': 'Meeting not found'}), 404

        # Save edited transcription
        edited_file = os.path.join(meeting_folder, 'transcription_edited.json')
        with open(edited_file, 'w', encoding='utf-8') as f:
            json.dump(transcription, f, indent=2, ensure_ascii=False)

        return jsonify({
            'success': True,
            'message': 'Transcription saved successfully'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/meeting/<meeting_id>', methods=['DELETE'])
def delete_meeting(meeting_id):
    """Delete a meeting"""
    try:
        meeting_folder = os.path.join(app.config['MEETINGS_FOLDER'], secure_filename(meeting_id))

        if not os.path.exists(meeting_folder):
            return jsonify({'error': 'Meeting not found'}), 404

        shutil.rmtree(meeting_folder)

        return jsonify({
            'success': True,
            'message': 'Meeting deleted successfully'
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    print("Starting Transcription Editor Server...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, host='0.0.0.0', port=5000)
