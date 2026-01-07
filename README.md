# AI Transcription Editor System

A complete web application for managing and editing AI-generated meeting transcriptions with speaker diarization support.

## Quick Start

```bash
cd transcriptionwebsite
pip3 install -r requirements.txt
python3 app.py
```

Then open http://localhost:5000 in your browser.

**For detailed installation instructions, see [INSTALL.md](INSTALL.md)**

## Overview

This system provides a complete workflow for managing meeting transcriptions:
1. **Upload meetings** with audio files
2. **Process** with external AI transcription service
3. **Edit** transcriptions with an intuitive interface
4. **Export** finalized transcriptions

## Features

- **File Upload**: Load diarized JSON transcriptions and audio files (WAV, MP3, M4A)
- **Pre-diarized Display**: Automatically displays existing speaker assignments from JSON
- **Synchronized Playback**: Audio highlights the current phrase being played in real-time
- **Sticky Controls**: Audio player and assignment buttons stay visible when scrolling through long transcriptions
- **RTL Support**: Full right-to-left text support for Hebrew and other RTL languages
- **Click to Play**: Click any phrase to jump to that timestamp in the audio
- **Text Editing**: Edit transcription text directly in the browser (changes don't affect audio)
- **Speaker Management**:
  - Auto-populates speakers from diarized JSON
  - Add new speaker names
  - Edit existing speaker names by clicking them
  - Reassign speakers to text segments (overrides JSON diarization)
  - Select partial text within speaker turns for reassignment
  - Color-coded speaker turns for easy identification
  - Condense multiple segments into single speaker turns
- **Export**: Export edited transcription with speaker names to text file matching the output.txt format

## Application Structure

This is a Flask-based web application with multiple pages:

- **Landing Page** (`/`) - Main entry point with navigation
- **Meeting Upload** (`/upload`) - Create new meeting and upload audio
- **Meetings List** (`/meetings`) - View all meetings and their status
- **Transcription Editor** (`/editor/<meeting_id>`) - Edit transcriptions with audio sync

## System Architecture

```
┌─────────────────┐
│  Landing Page   │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
┌───▼──┐  ┌──▼────┐
│Upload│  │ List  │
└───┬──┘  └──┬────┘
    │        │
    │    ┌───▼───┐
    │    │Editor │
    │    └───────┘
    │
┌───▼────────────┐
│External AI     │
│Transcription   │
└────────────────┘
```

## How to Use

### Step-by-Step Workflow

#### 1. Upload Files
- **Upload Transcription JSON**: Click or drag your diarized `transcription_diarized.json` file
- **Upload Audio File**: Click or drag your meeting audio (WAV, MP3, or M4A)
- The transcription will automatically display with existing speaker assignments

#### 2. Review Auto-populated Speakers
- Speakers from the JSON are automatically added to the sidebar
- Each speaker gets a unique color for easy identification
- Default names will be the speaker IDs (e.g., "SPEAKER_01")

#### 3. Edit Speaker Names
- Click on any speaker name in the sidebar to edit it
- Type the actual name (e.g., change "SPEAKER_01" to "John Smith")
- Press Enter or click outside to save
- Names will update throughout the transcription

#### 4. Add New Speakers (Optional)
- Enter a new speaker name in the input field
- Click "Add Speaker" or press Enter
- Use this for speakers not in the original diarization

#### 5. Reassign Speakers (Override Diarization)
- Click on a speaker in the sidebar to select them
- Highlight the text you want to reassign (can span multiple turns)
- Click "Assign to Speaker" button
- The text will be reassigned to the new speaker with their color
- This overrides the original JSON diarization

#### 6. Edit Transcription Text
- Click on any text to edit it directly
- Make corrections to transcription errors
- Changes are saved in the editor
- Editing doesn't affect the audio file
- Text is displayed right-to-left for Hebrew and other RTL languages
- You can select partial text within a speaker turn to create a new turn

#### 7. Play Audio
- Use the audio player controls at the top (stays visible while scrolling)
- Click any text segment to jump to that timestamp in the audio
- The currently playing phrase will be highlighted in yellow
- Audio automatically scrolls to keep current phrase visible
- Controls remain accessible even when viewing long transcriptions

#### 8. Export
- Click "Export Transcription" when done editing
- Downloads a text file with format: `[Speaker Name] (start-end): text`
- Uses your edited speaker names, not the original IDs
- Includes all your text edits

## Browser Recommendations

- **Best**: Chrome, Edge, or Safari (latest versions)
- Ensure JavaScript is enabled
- For best audio format compatibility, use Chrome or Edge

## Sample Files

- `transcription.json` - Sample JSON transcription (without speaker diarization)
- `transcription_diarized.json` - Sample diarized JSON with speaker assignments
- `output.txt` - Example of expected export format

## Keyboard Shortcuts

- **Enter** in speaker name field: Add speaker
- **Click** on phrase: Jump to timestamp
- **Select text** + Assign button: Assign to speaker

## Troubleshooting

**Audio won't play:**
- Ensure audio file is in WAV, MP3, or M4A format
- Try using Chrome or Safari
- Check browser console for errors (View → Developer → JavaScript Console)

**JSON won't load:**
- Verify JSON file is valid
- Check that it contains an array of segments with `start`, `end`, and `text` fields
- For diarized JSON, each segment should also have a `speaker` field (e.g., "SPEAKER_01")
- Example segment format:
  ```json
  {
    "start": 0.88,
    "end": 17.14,
    "text": "Meeting transcript text here",
    "speaker": "SPEAKER_01"
  }
  ```

**Export not working:**
- Ensure you've loaded the transcription JSON first
- Check that browser allows downloads (may need to allow pop-ups)

## Technical Details

- Single HTML file with embedded CSS and JavaScript
- No server required - runs entirely in your browser
- No data is sent to external servers - all processing is local
- Compatible with modern browsers (Chrome 90+, Safari 14+, Firefox 88+, Edge 90+)

## Privacy

All processing happens locally in your browser. Your transcription files and audio never leave your computer.
