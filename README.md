# 🖱️ Mouse Mover

An intelligent, mood-based mouse movement simulator that keeps your computer active while mimicking natural human behavior patterns.

## ✨ Features

### 🎭 **Mood System**
- **🚀 Hyperactive**: Aggressive, fast movements with frantic patterns
- **😌 Normal**: Balanced, natural human-like movements  
- **😴 Drowsy**: Slow, deliberate movements with longer pauses

### 🖱️ **Smart Movement Detection**
- Detects when you manually move the mouse
- Responds with a specific sequence when interrupted
- Seamlessly resumes previous mood after interruption

### 🛡️ **Safety Features**
- PyAutoGUI fail-safe protection (stays away from screen corners)
- Multi-monitor support with safe boundaries
- Configurable movement tolerance

### 🎨 **Rich Movement Library**
- **Aggressive movements**: Frustrated scribbling, angry shaking, frantic searching
- **Natural movements**: S-curves, figure-8 patterns, circular motions
- **Utility movements**: Random points, breaks, jiggling

## 🔧 Requirements

- Python 3.6+
- macOS, Windows, or Linux

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd mouse-mover
   ```

2. **Install dependencies**
   ```bash
   pip install pyautogui screeninfo
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

## 🚀 Usage

### Basic Usage
```bash
python app.py
```

The script will:
1. Auto-detect your screen configuration
2. Start with a random mood (1-minute cycles)
3. Continuously cycle through different moods
4. Respond to manual mouse movement when detected

### Console Output Example
```
Starting multi-monitor mouse mover. Press Ctrl+C to stop.
Mouse movement detection enabled (tolerance: 5 pixels)

🎭 Switching to mood: 🚀 HYPERACTIVE for 1 minute(s)
Performing frantic corner search...
Performing aggressive zigzag...
🖱️ External mouse movement detected! Responding...
Pausing for 4 seconds...
First response jiggle...
Waiting 3 seconds...
Second response jiggle...
Final pause for 2 seconds...
Resuming normal mood behavior...
✅ Mood 🚀 HYPERACTIVE completed after 1.0 minutes

🎭 Switching to mood: 😴 DROWSY for 1 minute(s)
Performing big slow move...
Long lazy break for 8.3 seconds
```

### Stopping the Application
Press `Ctrl+C` to safely stop the script.

## 📁 Project Structure

```
mouse-mover/
├── app.py          # Main orchestrator with mood system
├── movements.py    # Movement function library
└── README.md       # This file
```

### `app.py`
- Mood definitions and weighted selections
- Mouse movement detection system
- Main execution loop
- Screen boundary calculation

### `movements.py`
- Individual movement functions
- Aggressive movements (hyperactive mood)
- Natural movements (normal mood)
- Calm movements (drowsy mood)

## ⚙️ Configuration

### Mood Weights
Edit the `MOODS` dictionary in `app.py` to adjust movement probabilities:

```python
"hyperactive": {
    "name": "🚀 HYPERACTIVE",
    "movements": {
        movements.frantic_corner_search: 20,  # 20% chance
        movements.aggressive_zigzag: 18,      # 18% chance
        # ... more movements
    }
}
```

### Movement Detection
Adjust sensitivity in `app.py`:

```python
movement_detection_tolerance = 5  # pixels (default: 5)
```

### Screen Margins
Modify safe boundaries in `app.py`:

```python
margin = 100  # pixels from screen edges (default: 100)
```

## 🎯 Movement Types

### Hyperactive Mood (🚀)
- `frantic_corner_search` - Rapidly searches screen corners
- `aggressive_zigzag` - Fast, erratic zigzag patterns
- `big_fast_sweeping` - Dramatic full-screen sweeps
- `angry_shaking` - Rapid back-and-forth shaking
- `upward_jabbing` - Quick upward jab motions
- `frustrated_scribbling` - Frantic scribbling in small area

### Normal Mood (😌)
- `s_curve_movement` - Gentle S-shaped curves
- `circular_movement` - Smooth circular motions
- `natural_drift_movement` - Natural drift with micro-corrections
- `figure8_movement` - Figure-8 patterns
- `random_point_movement` - Random screen movements

### Drowsy Mood (😴)
- `big_slow_move` - Slow cross-screen movements
- `s_curve_movement` - Gentle curves
- `natural_drift_movement` - Slow drifting
- `take_a_break` - Regular pauses (3-7 seconds)
- `long_lazy_break` - Extended breaks (5-12 seconds)

## 🛠️ Troubleshooting

### PyAutoGUI Fail-Safe Error
If you get a fail-safe error:
- The script is designed to avoid this with 100px margins
- Ensure you don't manually move the mouse to screen corners while testing
- The fail-safe is intentionally left enabled for safety

### Permission Issues (macOS)
If you get security prompts:
- Go to System Preferences > Security & Privacy > Privacy
- Add your terminal app to "Accessibility" permissions
- May need to restart terminal after granting permissions

### No Mouse Movement
If the script isn't moving the mouse:
- Check that PyAutoGUI is properly installed
- Verify screen detection is working (check console output)
- Try running with `python3` instead of `python`

### High CPU Usage
- This is normal - the script continuously monitors mouse position
- Polling happens every 100ms during pauses
- You can increase sleep durations in movements if needed

## 🔧 Customization

### Adding New Movements
1. Add your function to `movements.py`:
   ```python
   def my_custom_movement(min_x, min_y, max_x, max_y):
       print("Performing custom movement...")
       # Your movement logic here
   ```

2. Add it to a mood in `app.py`:
   ```python
   "normal": {
       "movements": {
           movements.my_custom_movement: 10,  # 10% weight
           # ... other movements
       }
   }
   ```

### Creating New Moods
Add a new mood to the `MOODS` dictionary:

```python
"excited": {
    "name": "🎉 EXCITED", 
    "movements": {
        movements.zigzag_pattern: 30,
        movements.circular_movement: 20,
        # ... define movement weights
    }
}
```

## 📄 License

This project is open source. Feel free to modify and distribute.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## ⚠️ Disclaimer

This tool is designed for legitimate purposes like preventing screen savers or maintaining system activity. Use responsibly and in accordance with your organization's policies.