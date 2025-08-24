import random
import time
from screeninfo import get_monitors
import movements

# Mood definitions with weighted movement selections
MOODS = {
    "hyperactive": {
        "name": "🚀 HYPERACTIVE",
        "movements": {
            movements.frustrated_scribbling: 20,
            movements.aggressive_zigzag: 18,
            movements.big_fast_circle: 15,
            movements.angry_shaking: 12,
            movements.upward_jabbing: 10,
            movements.frantic_corner_search: 10,
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
        # Select a movement based on mood weights
        selected_movement = weighted_choice(mood_config["movements"])
        
        # Execute the movement
        if selected_movement in [movements.take_a_break, movements.quick_short_break, movements.long_lazy_break]:
            # Break functions don't need screen boundaries
            selected_movement()
        else:
            # Movement functions need screen boundaries
            selected_movement(min_x, min_y, max_x, max_y)
        
        # Small pause between actions
        time.sleep(random.uniform(0.1, 0.5))
    
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

try:
    while True:
        # Select a random mood and run it for 1 minute
        mood_name, mood_config = select_random_mood()
        run_mood_cycle(mood_name, mood_config, min_x, min_y, max_x, max_y, duration_minutes=1)
        
        # Brief pause between mood switches
        time.sleep(random.uniform(1, 3))

except KeyboardInterrupt:
    print("\n🛑 Script stopped by user.")