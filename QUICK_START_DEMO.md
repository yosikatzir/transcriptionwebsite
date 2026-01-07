# Quick Start - Get Screenshots in 10 Minutes

## Step 1: Generate Demo Data (1 minute)

```bash
cd /path/to/transcriptionwebsite
python3 create_demo_data.py
```

✅ Creates 3 sample meetings with Hebrew content

## Step 2: Start Server (30 seconds)

```bash
python3 app.py
```

Wait for: "Running on http://0.0.0.0:5000"

## Step 3: Take Screenshots (5 minutes)

Open browser to: **http://localhost:5000**

### Screenshot 1: Landing Page
- **URL**: `http://localhost:5000`
- **Action**: Just screenshot as-is
- **Save as**: `01_landing.png`

### Screenshot 2: Upload Page
- **URL**: `http://localhost:5000/upload`
- **Action**: Screenshot the form
- **Save as**: `02_upload.png`

### Screenshot 3: Meetings List
- **URL**: `http://localhost:5000/meetings`
- **Action**: Wait for meetings to load, then screenshot
- **Save as**: `03_meetings_list.png`
- Shows 3 meetings with different statuses!

### Screenshot 4: Editor - Full View
- **URL**: Click "Edit" on a "Transcribed" meeting
- **Action**: Screenshot full editor interface
- **Save as**: `04_editor_full.png`

### Screenshot 5: Editor - Text Highlighting
- **URL**: Same editor page
- **Action**:
  1. Click on any Hebrew text
  2. Wait 1 second for yellow highlight
  3. Screenshot
- **Save as**: `05_editor_highlighting.png`

### Screenshot 6: Exported File
- **URL**: Same editor page
- **Action**:
  1. Click "Export Transcription" button
  2. Open the downloaded .txt file
  3. Screenshot the file content
- **Save as**: `06_exported_output.png`

## Screenshot Shortcuts

**macOS**:
- `Cmd + Shift + 4` then `Space` then click window

**Windows**:
- `Win + Shift + S` for snipping tool

## Done!

You now have 6 professional screenshots showing:
1. Landing page with navigation
2. Upload interface
3. Meetings list with status tracking
4. Full editor interface
5. Audio synchronization (highlighting)
6. Professional export format

## Next Steps

See **PRESENTATION_OUTLINE.md** for:
- Complete presentation structure
- Talking points for each slide
- ROI calculations
- Implementation plan

See **WORKFLOW.md** for:
- Detailed user workflow
- Process diagrams
- Time estimates

See **SCREENSHOT_GUIDE.md** for:
- More detailed screenshot instructions
- Additional optional screenshots
- Presentation tips
