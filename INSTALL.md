# Transcription Editor System - Installation Guide

A complete web application for managing AI-generated meeting transcriptions with speaker diarization support.

## System Requirements

- **Operating System**: macOS, Linux, or Windows
- **Python**: 3.7 or higher
- **Browser**: Modern browser (Chrome, Firefox, Safari, Edge)

## Installation Steps

### 1. Install Python (if not already installed)

**macOS**:
```bash
# Check if Python is installed
python3 --version

# If not installed, install via Homebrew
brew install python3
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip

# Fedora/RHEL
sudo dnf install python3 python3-pip
```

### 2. Install Required Python Packages

Navigate to the project directory and install Flask:

```bash
cd /path/to/transcriptionwebsite
pip3 install flask
```

Or install from requirements file:

```bash
pip3 install -r requirements.txt
```

### 3. Verify Directory Structure

Ensure your project has the following structure:

```
transcriptionwebsite/
├── app.py                      # Flask backend server
├── templates/                  # HTML templates
│   ├── index.html             # Landing page
│   ├── upload.html            # Meeting upload page
│   ├── meetings.html          # Meetings list page
│   └── editor.html            # Transcription editor
├── meetings/                   # Meeting data storage (auto-created)
├── transcription.json         # Sample transcription
├── transcription_diarized.json # Sample diarized transcription
├── output.txt                 # Sample output format
└── README.md                  # Documentation
```

## Starting the Application

### Method 1: Direct Python Execution

```bash
cd /path/to/transcriptionwebsite
python3 app.py
```

### Method 2: Using Flask CLI

```bash
cd /path/to/transcriptionwebsite
export FLASK_APP=app.py
flask run
```

### Method 3: Development Mode (with auto-reload)

```bash
cd /path/to/transcriptionwebsite
export FLASK_ENV=development
python3 app.py
```

The server will start and display:
```
Starting Transcription Editor Server...
Open http://localhost:5000 in your browser
 * Running on http://0.0.0.0:5000
```

## Accessing the Application

Open your web browser and navigate to:
```
http://localhost:5000
```

You should see the landing page with two main functions:
1. **Upload New Meeting** - Start a new transcription process
2. **Meetings List** - View and edit existing transcriptions

## Usage Workflow

### 1. Upload a New Meeting

1. Click "העלאת פגישה חדשה / Upload New Meeting"
2. Fill in the meeting details:
   - **Meeting Date**: Select the date of the meeting
   - **Audio File**: Upload WAV, MP3, M4A, OGG, or FLAC file
   - **Speakers**: Enter speaker names separated by commas (optional)
   - **Custom Words**: Add special terms to improve transcription (optional)
3. Click "שלח לתמלול / Submit for Transcription"
4. The meeting will be saved and appear in the meetings list with status "Submitted"

### 2. External Transcription Process

After uploading:
- The audio file and meeting info are saved in `meetings/[MEETING_ID]/`
- An external AI transcription service should process the audio
- The service should save the transcription as `transcription.json` in the same folder
- Once the transcription file appears, the status changes to "Transcribed"

**Expected transcription.json format**:
```json
[
  {
    "start": 0.88,
    "end": 17.14,
    "text": "Meeting transcript text here",
    "speaker": "SPEAKER_01",
    "confidence": 0.831
  }
]
```

### 3. View Meetings List

1. Click "רשימת פגישות / Meetings List" from the landing page
2. View all meetings with their status:
   - **Submitted** (הוגש): Waiting for transcription
   - **Transcribed** (תומלל): Ready to edit
   - **Edited** (נערך): Has been edited and saved
3. Click "ערוך תמלול / Edit" to open the transcription editor
4. Click "מחק / Delete" to remove a meeting

### 4. Edit Transcription

Once in the editor:

**RTL Support**: The editor fully supports Hebrew and other right-to-left languages

**Edit Speaker Names**:
- Click on speaker names in the sidebar to edit them
- Change "SPEAKER_01" to actual names like "Sarah" or "John"
- Names update throughout the entire transcription

**Edit Text**:
- Click on any text segment to edit it directly
- Make corrections to transcription errors
- Changes are saved when you click "שמור / Save"

**Reassign Speakers**:
- Click a speaker in the sidebar to select them
- Highlight text you want to reassign
- Click "Assign to Speaker" to change the speaker assignment

**Audio Playback**:
- Use the audio player (stays visible when scrolling)
- Click any text segment to jump to that timestamp
- Currently playing text is highlighted in yellow

**Save Your Work**:
- Click "שמור / Save" to save your edited transcription
- This creates `transcription_edited.json` in the meeting folder
- You can continue editing later

**Load Original**:
- Click "טען מקור / Load Original" to discard changes
- Reloads the original AI-generated transcription

**Export**:
- Click "Export Transcription" to download as text file
- Format: `[Speaker Name] (start-end): text`

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

## Troubleshooting

### Port Already in Use

If port 5000 is already in use:
```bash
# Change the port in app.py (last line)
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

### Flask Not Found

```bash
pip3 install --upgrade flask
```

### Permission Denied

```bash
chmod +x app.py
python3 app.py
```

### Cannot Access from Other Devices

The server is configured to listen on all interfaces (`0.0.0.0`). Access from other devices on your network using:
```
http://[YOUR_IP_ADDRESS]:5000
```

Find your IP address:
- macOS/Linux: `ifconfig | grep inet`
- Windows: `ipconfig`

## File Structure

### Meeting Folders

Each meeting creates a folder in `meetings/[MEETING_ID]/`:
- `meeting_info.json` - Meeting metadata
- `[audio_file].wav/mp3/m4a` - Original audio file
- `transcription.json` - AI-generated transcription (added by external process)
- `transcription_edited.json` - Your edited version (created when you save)

### Data Persistence

All data is stored locally in the `meetings/` folder. No external database required.

## Security Notes

- This application is designed for local use
- Do not expose to the internet without proper authentication
- All files are stored on your local machine
- No data is sent to external servers

## Support

For issues or questions, refer to the main README.md file or check the project documentation.
