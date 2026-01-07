# User Workflow - Transcription Editor System

## Overview

This document describes the complete user workflow for secretaries using the AI Transcription Editor System.

## User Personas

**Primary User**: Secretary/Administrative Assistant
- Manages meeting recordings
- Edits AI-generated transcriptions
- Assigns speakers and corrects errors
- Exports finalized transcriptions for distribution

## Complete Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────┐
│                     START: New Meeting                           │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
            ┌────────────────────────┐
            │  1. LANDING PAGE       │
            │  http://localhost:5000 │
            └────────┬───────────────┘
                     │
                     │ Click "Upload New Meeting"
                     ▼
            ┌────────────────────────┐
            │  2. MEETING UPLOAD     │
            │  /upload               │
            │                        │
            │  • Enter meeting date  │
            │  • Upload audio file   │
            │  • Add speaker names   │
            │  • Add custom words    │
            └────────┬───────────────┘
                     │
                     │ Click "Submit"
                     ▼
            ┌────────────────────────┐
            │  Files Saved           │
            │  meetings/YYYYMMDD/    │
            │  • meeting_info.json   │
            │  • audio.wav           │
            └────────┬───────────────┘
                     │
                     │ Redirect to Meetings List
                     ▼
            ┌────────────────────────┐
            │  3. MEETINGS LIST      │
            │  /meetings             │
            │                        │
            │  Status: Submitted ⏳  │
            └────────┬───────────────┘
                     │
                     │ External AI Process
                     ▼
            ┌────────────────────────┐
            │  EXTERNAL AI           │
            │  Transcription Service │
            │                        │
            │  Reads: audio.wav      │
            │  Writes:               │
            │  transcription.json    │
            └────────┬───────────────┘
                     │
                     │ File appears
                     ▼
            ┌────────────────────────┐
            │  3. MEETINGS LIST      │
            │  /meetings             │
            │                        │
            │  Status: Transcribed ✓ │
            └────────┬───────────────┘
                     │
                     │ Click "Edit"
                     ▼
            ┌────────────────────────┐
            │  4. TRANSCRIPTION      │
            │     EDITOR             │
            │  /editor/[MEETING_ID]  │
            │                        │
            │  • Auto-load trans.    │
            │  • Auto-load audio     │
            │  • Edit speakers       │
            │  • Correct text        │
            │  • Reassign speakers   │
            └────────┬───────────────┘
                     │
                     │ Click "Save"
                     ▼
            ┌────────────────────────┐
            │  Edits Saved           │
            │  transcription_        │
            │  edited.json           │
            └────────┬───────────────┘
                     │
                     │ Back to meetings
                     ▼
            ┌────────────────────────┐
            │  3. MEETINGS LIST      │
            │  /meetings             │
            │                        │
            │  Status: Edited ✅     │
            └────────┬───────────────┘
                     │
                     │ Click "Edit" again
                     ▼
            ┌────────────────────────┐
            │  4. TRANSCRIPTION      │
            │     EDITOR             │
            │                        │
            │  Click "Export"        │
            └────────┬───────────────┘
                     │
                     │ Download
                     ▼
            ┌────────────────────────┐
            │  edited_transcription  │
            │  .txt                  │
            │                        │
            │  Ready to distribute   │
            └────────────────────────┘
```

## Detailed Step-by-Step Process

### Phase 1: Meeting Upload

**Location**: Upload Page (`/upload`)

**User Actions**:
1. Secretary accesses the landing page
2. Clicks "העלאת פגישה חדשה / Upload New Meeting"
3. Fills in meeting information:
   - **Date**: Selects meeting date from calendar
   - **Audio File**: Drags or clicks to upload WAV/MP3/M4A file
   - **Speakers**: Types speaker names: "שרה כהן, דוד לוי, רחל אברהם"
   - **Custom Words**: Adds special terms: "מדיניות, סיכונים, קו-פיילוט"
4. Clicks "שלח לתמלול / Submit for Transcription"

**System Actions**:
- Creates unique folder: `meetings/20260107_143022/`
- Saves `meeting_info.json` with metadata
- Saves audio file
- Redirects to meetings list
- Shows status: "Submitted"

**Time**: 2-3 minutes

---

### Phase 2: AI Transcription (External)

**Location**: External AI Service

**Process**:
1. External AI service monitors `meetings/` folder
2. Detects new audio files with "Submitted" status
3. Processes audio file:
   - Speech-to-text transcription
   - Speaker diarization (identifies different speakers)
   - Timestamp alignment
   - Confidence scoring
4. Saves result as `transcription.json` in meeting folder

**System Actions**:
- Meeting status automatically changes to "Transcribed"
- "Edit" button becomes active in meetings list

**Time**: 10-30 minutes (depending on audio length and AI service)

**Note**: This phase is handled by your external AI transcription service, not by this application.

---

### Phase 3: Review Meetings List

**Location**: Meetings List (`/meetings`)

**User Actions**:
1. Secretary accesses meetings list
2. Sees all meetings with color-coded status:
   - 🟡 **Submitted**: Waiting for transcription
   - 🔵 **Transcribed**: Ready to edit
   - 🟢 **Edited**: Has been edited and saved
3. Reviews meeting details:
   - Meeting date
   - Speaker names
   - Custom words
   - Status
4. Clicks "ערוך תמלול / Edit" for a transcribed meeting

**System Actions**:
- Loads editor with meeting ID
- Prepares to load transcription and audio

**Time**: 30 seconds

---

### Phase 4: Edit Transcription

**Location**: Transcription Editor (`/editor/[MEETING_ID]`)

**User Actions**:

#### 4.1 Initial Review
- Editor automatically loads transcription and audio
- Text appears in Hebrew (RTL), grouped by speaker
- Speakers labeled as SPEAKER_01, SPEAKER_02, etc.
- Each speaker has a different color

#### 4.2 Rename Speakers
1. Clicks on "SPEAKER_01" in sidebar
2. Types actual name: "שרה כהן"
3. Presses Enter
4. Name updates throughout the entire transcription

Repeats for all speakers:
- SPEAKER_01 → שרה כהן
- SPEAKER_02 → דוד לוי
- SPEAKER_03 → רחל אברהם

**Time**: 1-2 minutes

#### 4.3 Correct Text Errors
1. Reads through transcription while listening to audio
2. Clicks on text with errors
3. Types corrections directly
4. Fixes:
   - Misspelled words
   - Incorrect terms
   - Punctuation
   - Grammar

**Time**: 5-15 minutes (depending on accuracy)

#### 4.4 Reassign Speakers
When AI misidentifies a speaker:
1. Selects correct speaker from sidebar
2. Highlights misidentified text
3. Clicks "Assign to Speaker"
4. Text changes color and moves to correct speaker

**Time**: 2-5 minutes

#### 4.5 Listen and Verify
1. Clicks on any text segment
2. Audio jumps to that timestamp
3. Verifies text matches audio
4. Currently playing text highlights in yellow
5. Scrolls through long transcriptions (controls stay visible)

#### 4.6 Save Progress
1. Clicks "שמור / Save" button
2. System saves as `transcription_edited.json`
3. Can close editor and return later
4. Changes are preserved

**System Actions**:
- Saves edited transcription to server
- Updates meeting status to "Edited"
- Preserves original transcription (can reload if needed)

**Total Editing Time**: 10-30 minutes (depending on meeting length and accuracy)

---

### Phase 5: Export Final Transcription

**Location**: Transcription Editor

**User Actions**:
1. Reviews final transcription
2. Clicks "Export Transcription" button

**System Actions**:
- Generates formatted text file
- Format: `[Speaker Name] (timestamp): text`
- Example:
  ```
  [שרה כהן] (0.88-17.14): מדיניות סיכונים כפולים...
  [דוד לוי] (17.14-20.64): ממי שיתנו כבר בתוכו...
  ```
- Downloads as `edited_transcription.txt`

**Output Use**:
- Distribute to meeting participants
- Archive with meeting records
- Share with management
- Include in meeting minutes

**Time**: 10 seconds

---

## Status Flow Diagram

```
┌─────────────┐     Upload     ┌──────────────┐     AI Process    ┌──────────────┐
│   No Data   │ ──────────────>│  Submitted   │ ─────────────────>│ Transcribed  │
│             │                 │      ⏳      │                    │      ✓       │
└─────────────┘                 └──────────────┘                    └──────┬───────┘
                                                                           │
                                                                           │ Edit & Save
                                                                           ▼
                                                                    ┌──────────────┐
                                                                    │   Edited     │
                                                                    │      ✅      │
                                                                    └──────────────┘
```

## Time Estimates

| Phase | Task | Estimated Time |
|-------|------|---------------|
| 1 | Upload Meeting | 2-3 minutes |
| 2 | AI Transcription (External) | 10-30 minutes |
| 3 | Review Meetings List | 30 seconds |
| 4 | Edit Transcription | 10-30 minutes |
|   | - Rename Speakers | 1-2 minutes |
|   | - Correct Text | 5-15 minutes |
|   | - Reassign Speakers | 2-5 minutes |
|   | - Verify | 2-8 minutes |
| 5 | Export | 10 seconds |

**Total Active Time**: 15-35 minutes per meeting
**Total Elapsed Time**: 25-65 minutes (including AI processing)

## Key Features for Secretaries

### 1. Bilingual Interface
- Hebrew and English labels throughout
- RTL text support for Hebrew content
- Familiar interface for Israeli users

### 2. Audio Synchronization
- Click any text to hear that part of the recording
- Currently playing text highlights automatically
- Easy verification of transcription accuracy

### 3. Speaker Management
- Visual color coding for each speaker
- Easy speaker reassignment
- Editable speaker names
- Handles multiple speakers seamlessly

### 4. Efficiency Features
- Sticky controls (stay visible when scrolling)
- Save and resume editing
- Load original transcription if needed
- Fast export to distributable format

### 5. Error Prevention
- Can't delete meetings by accident (confirmation required)
- Original transcription preserved
- Save frequently to prevent data loss
- Visual feedback for all actions

## Common Scenarios

### Scenario 1: Quick Review
**When**: High-quality AI transcription, minimal errors

**Steps**:
1. Upload meeting (2 min)
2. Wait for AI (15 min)
3. Rename speakers (1 min)
4. Quick text review (5 min)
5. Export (10 sec)

**Total**: ~23 minutes

---

### Scenario 2: Detailed Editing
**When**: Lower quality audio, technical terms, multiple speakers

**Steps**:
1. Upload meeting (3 min)
2. Wait for AI (30 min)
3. Rename speakers (2 min)
4. Thorough text corrections (15 min)
5. Reassign misidentified speakers (5 min)
6. Verify with audio (8 min)
7. Export (10 sec)

**Total**: ~63 minutes

---

### Scenario 3: Multiple Meetings
**When**: Processing several meetings in one session

**Steps**:
1. Upload all meetings (10 min for 5 meetings)
2. Wait for AI processing (parallel processing)
3. Edit meetings one by one as they complete
4. Can work on meeting #1 while #2-5 are transcribing

**Efficiency**: Parallel processing reduces total time

## Technical Requirements

**For Secretaries**:
- Modern web browser (Chrome, Safari, Firefox, Edge)
- Audio playback capability
- Basic computer skills
- Hebrew keyboard (for Hebrew meetings)

**For IT Department**:
- Python 3.7+
- Flask web server
- External AI transcription service integration
- Local network access (or internet for remote access)

## Security & Privacy

- All data stored locally on server
- No external data transmission (except to your AI service)
- Meeting files isolated in separate folders
- Automatic file organization
- Can be deployed on internal network only

## Benefits Summary

**For Secretaries**:
- ✅ Faster transcription process (AI does bulk work)
- ✅ Easy editing interface
- ✅ Audio verification built-in
- ✅ Professional output format
- ✅ Handles Hebrew seamlessly

**For Management**:
- ✅ Consistent transcription quality
- ✅ Faster turnaround time
- ✅ Centralized meeting archive
- ✅ Audit trail (original vs edited)
- ✅ Cost-effective (reduced manual transcription)

## Support

For questions or issues:
- See INSTALL.md for technical setup
- See README.md for feature documentation
- Contact IT department for server issues
- Contact AI service provider for transcription quality issues
