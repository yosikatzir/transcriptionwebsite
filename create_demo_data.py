#!/usr/bin/env python3
"""
Demo Data Generator for Transcription Editor
Creates sample meetings for demonstration purposes
"""

import os
import json
import shutil
from datetime import datetime, timedelta

# Create meetings directory
meetings_dir = 'meetings'
os.makedirs(meetings_dir, exist_ok=True)

# Sample meeting data
sample_meetings = [
    {
        'date': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d'),
        'speakers': ['שרה כהן', 'דוד לוי', 'רחל אברהם'],
        'custom_words': ['מדיניות', 'סיכונים', 'קו-פיילוט'],
        'status': 'edited'
    },
    {
        'date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
        'speakers': ['יוסי ישראלי', 'מיכל דוד', 'אבי שטרן'],
        'custom_words': ['תקציב', 'פרויקט', 'יעדים'],
        'status': 'transcribed'
    },
    {
        'date': (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
        'speakers': ['רונית פרידמן', 'עמית כץ'],
        'custom_words': ['אסטרטגיה', 'שיווק', 'מכירות'],
        'status': 'submitted'
    }
]

# Sample transcription data (shortened version of real transcription)
sample_transcription = [
    {
        "start": 0.88,
        "end": 17.14,
        "text": "מדיניות סיכונים כפולים מובאת לאישור פעם בשנה, המדיניות הקודמת אושרה בנובמבר 24.",
        "speaker": "SPEAKER_01",
        "confidence": 0.831
    },
    {
        "start": 17.14,
        "end": 20.64,
        "text": "ממי שיתנו כבר בתוכו וזה לא יצא החוצה? כן, שנמצא פה.",
        "speaker": "SPEAKER_02",
        "confidence": 0.85
    },
    {
        "start": 20.64,
        "end": 25.28,
        "text": "שנמצא בפיילוט בנסיבות. תסבירי קצת מה זה.",
        "speaker": "SPEAKER_01",
        "confidence": 0.82
    },
    {
        "start": 25.28,
        "end": 45.30,
        "text": "קו-פיילוט כמו צ'אט GPT, שנמצא בבדיקה באזורים מסוימים בארגון.",
        "speaker": "SPEAKER_03",
        "confidence": 0.86
    }
]

print("Creating demo meetings...")

for i, meeting in enumerate(sample_meetings):
    # Create meeting ID
    meeting_id = (datetime.now() - timedelta(days=len(sample_meetings)-i)).strftime('%Y%m%d_%H%M%S')
    meeting_folder = os.path.join(meetings_dir, meeting_id)

    os.makedirs(meeting_folder, exist_ok=True)

    # Create meeting_info.json
    meeting_info = {
        'date': meeting['date'],
        'speakers': meeting['speakers'],
        'custom_words': meeting['custom_words'],
        'created_at': datetime.now().isoformat(),
        'audio_filename': f'meeting_{i+1}.wav'
    }

    with open(os.path.join(meeting_folder, 'meeting_info.json'), 'w', encoding='utf-8') as f:
        json.dump(meeting_info, f, indent=2, ensure_ascii=False)

    # Create dummy audio file marker
    with open(os.path.join(meeting_folder, meeting_info['audio_filename']), 'w') as f:
        f.write('# Dummy audio file for demo purposes')

    # Create transcription based on status
    if meeting['status'] in ['transcribed', 'edited']:
        with open(os.path.join(meeting_folder, 'transcription.json'), 'w', encoding='utf-8') as f:
            json.dump(sample_transcription, f, indent=2, ensure_ascii=False)

    # Create edited transcription if status is edited
    if meeting['status'] == 'edited':
        # Modify speaker names in edited version
        edited_transcription = []
        for segment in sample_transcription:
            segment_copy = segment.copy()
            if segment['speaker'] == 'SPEAKER_01':
                segment_copy['speaker'] = meeting['speakers'][0] if len(meeting['speakers']) > 0 else 'SPEAKER_01'
            elif segment['speaker'] == 'SPEAKER_02':
                segment_copy['speaker'] = meeting['speakers'][1] if len(meeting['speakers']) > 1 else 'SPEAKER_02'
            elif segment['speaker'] == 'SPEAKER_03':
                segment_copy['speaker'] = meeting['speakers'][2] if len(meeting['speakers']) > 2 else 'SPEAKER_03'
            edited_transcription.append(segment_copy)

        with open(os.path.join(meeting_folder, 'transcription_edited.json'), 'w', encoding='utf-8') as f:
            json.dump(edited_transcription, f, indent=2, ensure_ascii=False)

    print(f"✓ Created meeting {meeting_id} - Status: {meeting['status']}")

print("\n✅ Demo data created successfully!")
print(f"Created {len(sample_meetings)} sample meetings in the '{meetings_dir}' folder")
print("\nYou can now:")
print("1. Run 'python3 app.py' to start the server")
print("2. Open http://localhost:5000 to see the meetings")
print("3. Take screenshots of each page for your presentation")
