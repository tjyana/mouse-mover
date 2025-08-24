import random
import time
import pyautogui
from screeninfo import get_monitors
import movements

# Global variables for mouse movement detection
last_script_position = None
movement_detection_tolerance = 5  # pixels tolerance for movement detection
movement_detection_enabled = True  # Flag to temporarily disable detection

def update_script_position():
    """Update the last known position that our script set the mouse to."""
    global last_script_position
    last_script_position = pyautogui.position()

def detect_external_movement():
    """
    Detect if the mouse has been moved by something other than our script.
    Returns True if external movement is detected.
    """
    global last_script_position, movement_detection_enabled
    
    # If detection is disabled, return False
    if not movement_detection_enabled:
        return False
    
    if last_script_position is None:
        update_script_position()
        return False
    
    current_pos = pyautogui.position()
    
    # Check if current position differs significantly from last script position
    distance = ((current_pos[0] - last_script_position[0]) ** 2 + 
                (current_pos[1] - last_script_position[1]) ** 2) ** 0.5
    
    return distance > movement_detection_tolerance

def disable_movement_detection():
    """Temporarily disable movement detection during script movements."""
    global movement_detection_enabled
    movement_detection_enabled = False

def enable_movement_detection():
    """Re-enable movement detection after script movements."""
    global movement_detection_enabled
    movement_detection_enabled = True

def handle_movement_interruption(min_x, min_y, max_x, max_y):
    """
    Handle the sequence when external mouse movement is detected:
    1. Stop for 4 seconds
    2. Short fast jiggle
    3. Wait 3 seconds
    4. Short fast jiggle again
    5. Wait 2 seconds
    6. Resume
    """
    print("🖱️  External mouse movement detected! Responding...")
    
    # Disable detection during our response sequence
    disable_movement_detection()
    
    # Stop for 4 seconds
    print("Pausing for 4 seconds...")
    time.sleep(4)
    
    # First jiggle
    print("First response jiggle...")
    movements.short_fast_jiggle(min_x, min_y, max_x, max_y)
    update_script_position()  # Update our tracking
    
    # Wait 3 seconds
    print("Waiting 3 seconds...")
    time.sleep(3)
    
    # Second jiggle
    print("Second response jiggle...")
    movements.short_fast_jiggle(min_x, min_y, max_x, max_y)
    update_script_position()  # Update our tracking
    
    # Wait 2 seconds before resuming
    print("Final pause for 2 seconds...")
    time.sleep(2)
    
    # Re-enable detection after our response
    enable_movement_detection()
    
    print("Resuming normal mood behavior...")

# Mood definitions with weighted movement selections
MOODS = {
    "hyperactive": {
        "name": "🚀 HYPERACTIVE",
        "movements": {
            movements.frantic_corner_search: 20,
            movements.aggressive_zigzag: 18,
            movements.big_fast_sweeping: 15,
            movements.angry_shaking: 12,
            movements.upward_jabbing: 10,
            movements.frustrated_scribbling: 10,
            movements.short_fast_jiggle: 8,
            movements.zigzag_pattern: 5,
            movements.quick_short_break: 2
        }
    },
    "normal": {
        "name": "😌 NORMAL",
        "movements": {
            movements.s_curve_movement: 15,
            movements.circular_movement: 15,
            movements.natural_drift_movement: 15,
            movements.random_point_movement: 12,
            movements.figure8_movement: 10,
            movements.big_slow_move: 10,
            movements.zigzag_pattern: 8,
            movements.short_fast_jiggle: 8,
            movements.take_a_break: 7
        }
    },
    "drowsy": {
        "name": "😴 DROWSY",
        "movements": {
            movements.big_slow_move: 25,
            movements.s_curve_movement: 20,
            movements.natural_drift_movement: 15,
            movements.take_a_break: 15,
            movements.long_lazy_break: 10,
            movements.circular_movement: 8,
            movements.random_point_movement: 5,
            movements.figure8_movement: 2
        }
    }
}

def weighted_choice(choices):
    """Select a random choice based on weights."""
    total = sum(choices.values())
    r = random.uniform(0, total)
    upto = 0
    for choice, weight in choices.items():
        if upto + weight >= r:
            return choice
        upto += weight
    return list(choices.keys())[-1]  # fallback

def select_random_mood():
    """Select a random mood."""
    mood_name = random.choice(list(MOODS.keys()))
    return mood_name, MOODS[mood_name]

def run_mood_cycle(mood_name, mood_config, min_x, min_y, max_x, max_y, duration_minutes=1):
    """Run a specific mood for the given duration."""
    print(f"\n🎭 Switching to mood: {mood_config['name']} for {duration_minutes} minute(s)")
    
    start_time = time.time()
    end_time = start_time + (duration_minutes * 60)  # Convert minutes to seconds
    
    while time.time() < end_time:
        # Check for external mouse movement before each action
        if detect_external_movement():
            handle_movement_interruption(min_x, min_y, max_x, max_y)
            # Continue with the same mood after interruption
            continue
        
        # Select a movement based on mood weights
        selected_movement = weighted_choice(mood_config["movements"])
        
        # Execute the movement
        if selected_movement in [movements.take_a_break, movements.quick_short_break, movements.long_lazy_break]:
            # Break functions don't need screen boundaries
            selected_movement()
            # For break functions, just update position after the break
            update_script_position()
        else:
            # Disable movement detection during script movements
            disable_movement_detection()
            
            # Movement functions need screen boundaries
            selected_movement(min_x, min_y, max_x, max_y)
            
            # Update our tracking of where the script moved the mouse
            update_script_position()
            
            # Re-enable movement detection
            enable_movement_detection()
        
        # Small pause between actions (also check for movement during pause)
        pause_duration = random.uniform(0.1, 0.5)
        pause_start = time.time()
        
        while time.time() - pause_start < pause_duration:
            if detect_external_movement():
                handle_movement_interruption(min_x, min_y, max_x, max_y)
                break  # Exit pause loop and continue mood
            time.sleep(0.1)  # Check every 100ms during pause
    
    elapsed = time.time() - start_time
    print(f"✅ Mood {mood_config['name']} completed after {elapsed/60:.1f} minutes")

print("Starting multi-monitor mouse mover. Press Ctrl+C to stop.")

# --- NEW SECTION: Calculate total screen area ---
# We'll find the edges of the entire virtual screen space.
all_monitors = get_monitors()
screen_min_x = min(m.x for m in all_monitors)
screen_min_y = min(m.y for m in all_monitors)
screen_max_x = max(m.x + m.width for m in all_monitors)
screen_max_y = max(m.y + m.height for m in all_monitors)

# Add margins to avoid PyAutoGUI fail-safe triggers at screen corners/edges
margin = 100  # 100 pixels margin from edges
min_x = screen_min_x + margin
min_y = screen_min_y + margin
max_x = screen_max_x - margin
max_y = screen_max_y - margin
# -----------------------------------------------

# Initialize mouse position tracking
update_script_position()
print(f"Mouse movement detection enabled (tolerance: {movement_detection_tolerance} pixels)")

try:
    while True:
        # Select a random mood and run it for 1 minute
        mood_name, mood_config = select_random_mood()
        run_mood_cycle(mood_name, mood_config, min_x, min_y, max_x, max_y, duration_minutes=1)
        
        # Brief pause between mood switches
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    print("\n🛑 Script stopped by user.")