# AI Transcription Editor

A web-based tool for secretaries to edit AI-generated meeting transcriptions with synchronized audio playback.

## Features

- **File Upload**: Load JSON transcriptions and audio files (WAV, MP3, M4A)
- **Synchronized Playback**: Audio highlights the current phrase being played
- **Click to Play**: Click any phrase to jump to that timestamp in the audio
- **Text Editing**: Edit transcription text directly in the browser
- **Speaker Management**:
  - Add speaker names
  - Assign speakers to text segments
  - Color-coded speaker turns
  - Condense multiple phrases into single speaker turns
- **Export**: Export edited transcription to text file matching the output.txt format

## How to Use on macOS

### Opening the Application

1. Locate the `index.html` file in this folder
2. Double-click `index.html` to open it in your default browser
   - Or right-click and choose "Open With" → Safari/Chrome/Firefox

### Step-by-Step Workflow

#### 1. Upload Files
- **Upload Transcription JSON**: Click or drag your `transcription.json` file
- **Upload Audio File**: Click or drag your meeting audio (WAV, MP3, or M4A)

#### 2. Add Speakers
- In the left sidebar, enter speaker names
- Click "Add Speaker" or press Enter
- Each speaker gets a unique color automatically

#### 3. Assign Speakers to Text
- Click on a speaker in the sidebar to select them
- Highlight the text you want to assign (can be one or multiple phrases)
- Click "Assign to Speaker" button
- The text will be color-coded and condensed into a single turn

#### 4. Edit Text
- Click on any text to edit it directly
- Changes are saved automatically
- Editing doesn't affect the audio file

#### 5. Play Audio
- Use the audio player controls at the top
- Click any phrase to jump to that point in the audio
- The currently playing phrase will be highlighted in yellow

#### 6. Export
- Click "Export Transcription" when done
- Downloads a text file in the format: `[SPEAKER_ID] (start-end): text`

## Browser Recommendations

- **Best**: Chrome, Edge, or Safari (latest versions)
- Ensure JavaScript is enabled
- For best audio format compatibility, use Chrome or Edge

## Sample Files

- `transcription.json` - Sample JSON transcription
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
