import pyautogui
import random
import time
import math

def zigzag_pattern(min_x, min_y, max_x, max_y):
    """
    Performs a rapid zigzag movement pattern across the screen.
    Moves left-right repeatedly while going down the screen.
    Completes about 20 iterations in 5 seconds.
    Coordinates passed should already have margins applied to avoid PyAutoGUI fail-safe.
    """
    print("Performing zigzag pattern...")
    
    # Calculate the step size for moving down
    screen_height = max_y - min_y
    step_size = screen_height // 20  # Divide screen into 20 horizontal bands
    
    start_time = time.time()
    target_duration = 5.0  # 5 seconds total
    iterations = 20
    
    for i in range(iterations):
        current_y = min_y + (i * step_size)
        
        # Ensure we don't go beyond screen bounds
        if current_y >= max_y:
            current_y = max_y - 1
            
        # Calculate timing for this iteration
        iteration_duration = target_duration / (iterations * 2)  # 2 moves per iteration
        
        # Move to left side
        pyautogui.moveTo(min_x, current_y, duration=iteration_duration)
        
        # Move to right side  
        pyautogui.moveTo(max_x, current_y, duration=iteration_duration)
        
        # Check if we've exceeded our target time
        if time.time() - start_time >= target_duration:
            break
    
    elapsed_time = time.time() - start_time
    print(f"Zigzag pattern completed in {elapsed_time:.2f} seconds")

def s_curve_movement(min_x, min_y, max_x, max_y):
    """
    Performs a gentle S-curve movement across the screen with variable speeds.
    """
    print("Performing S-curve movement...")
    
    # Calculate center point and start/end positions
    center_y = (min_y + max_y) // 2
    start_x, start_y = min_x + 50, center_y - 100
    end_x, end_y = max_x - 50, center_y + 100
    
    # Create S-curve with multiple waypoints
    waypoints = []
    steps = 8
    for i in range(steps + 1):
        progress = i / steps
        # S-curve formula
        x = start_x + (end_x - start_x) * progress
        y_offset = 80 * (2 * progress - 1) * (1 - progress) * progress  # Creates S shape
        y = start_y + (end_y - start_y) * progress + y_offset
        waypoints.append((int(x), int(y)))
    
    # Move through S-curve with varying speeds
    for i, (x, y) in enumerate(waypoints):
        # Vary duration to simulate human acceleration/deceleration
        if i == 0:
            duration = 0.3  # Start slow
        elif i < len(waypoints) // 2:
            duration = 0.15  # Speed up
        else:
            duration = 0.25  # Slow down at end
            
        pyautogui.moveTo(x, y, duration=duration)
        time.sleep(random.uniform(0.05, 0.15))  # Small random pauses

def circular_movement(min_x, min_y, max_x, max_y):
    """
    Performs smooth circular motion around the center of the screen.
    """
    print("Performing circular movement...")
    
    # Calculate center point for circular movements
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    
    radius = min(200, (max_x - min_x) // 6)  # Adjust radius to screen size
    circle_steps = 16
    
    for i in range(circle_steps):
        angle = (i / circle_steps) * 2 * math.pi
        x = center_x + int(radius * math.cos(angle))
        y = center_y + int(radius * math.sin(angle))
        
        # Ensure coordinates are within safe bounds
        x = max(min_x, min(max_x, x))
        y = max(min_y, min(max_y, y))
        
        duration = random.uniform(0.1, 0.25)
        pyautogui.moveTo(x, y, duration=duration)
        time.sleep(random.uniform(0.02, 0.08))

def figure8_movement(min_x, min_y, max_x, max_y):
    """
    Performs a figure-8 pattern using parametric equations.
    """
    print("Performing figure-8 movement...")
    
    # Calculate center point
    center_x = (min_x + max_x) // 2
    center_y = (min_y + max_y) // 2
    
    figure8_steps = 20
    scale = min(150, (max_x - min_x) // 8)
    
    for i in range(figure8_steps):
        t = (i / figure8_steps) * 4 * math.pi  # Two complete loops
        # Figure-8 parametric equations
        x = center_x + int(scale * math.sin(t))
        y = center_y + int(scale * math.sin(t) * math.cos(t))
        
        # Ensure coordinates are within safe bounds
        x = max(min_x, min(max_x, x))
        y = max(min_y, min(max_y, y))
        
        duration = random.uniform(0.08, 0.2)
        pyautogui.moveTo(x, y, duration=duration)
        time.sleep(random.uniform(0.01, 0.05))

def natural_drift_movement(min_x, min_y, max_x, max_y):
    """
    Performs random natural drift movements with micro-corrections,
    simulating natural human hand movement and adjustments.
    """
    print("Performing natural drift movements...")
    
    current_x, current_y = pyautogui.position()
    
    for _ in range(8):
        # Small drift movement
        drift_x = random.randint(-100, 100)
        drift_y = random.randint(-80, 80)
        
        target_x = max(min_x, min(max_x, current_x + drift_x))
        target_y = max(min_y, min(max_y, current_y + drift_y))
        
        # Main movement
        pyautogui.moveTo(target_x, target_y, duration=random.uniform(0.3, 0.8))
        current_x, current_y = target_x, target_y
        
        # Micro-correction (like humans do)
        micro_x = random.randint(-15, 15)
        micro_y = random.randint(-15, 15)
        
        final_x = max(min_x, min(max_x, current_x + micro_x))
        final_y = max(min_y, min(max_y, current_y + micro_y))
        
        pyautogui.moveTo(final_x, final_y, duration=random.uniform(0.1, 0.3))
        current_x, current_y = final_x, final_y
        
        time.sleep(random.uniform(0.2, 0.6))

def big_slow_move(min_x, min_y, max_x, max_y):
    """Moves the mouse across a long distance over a few seconds."""
    print("Performing big slow move...")
    random_x = random.randint(min_x, max_x - 1)
    random_y = random.randint(min_y, max_y - 1)
    pyautogui.moveTo(random_x, random_y, duration=random.uniform(1.5, 4.0))

def short_fast_jiggle(min_x, min_y, max_x, max_y):
    """Moves the mouse a short distance very quickly."""
    print("Performing short fast jiggle...")
    # Get current mouse position
    current_x, current_y = pyautogui.position()
    # Calculate a small jiggle range, ensuring it stays within bounds
    jiggle_x = max(min_x, min(max_x - 1, random.randint(current_x - 50, current_x + 50)))
    jiggle_y = max(min_y, min(max_y - 1, random.randint(current_y - 50, current_y + 50)))
    pyautogui.moveTo(jiggle_x, jiggle_y, duration=random.uniform(0.1, 0.4))

def take_a_break():
    """Do nothing for a while."""
    sleep_time = random.uniform(3, 7)
    print(f"Taking a break for {sleep_time:.2f} seconds")
    time.sleep(sleep_time)

def quick_short_break():
    """Take a very short break."""
    sleep_time = random.uniform(0.5, 2.0)
    print(f"Quick break for {sleep_time:.2f} seconds")
    time.sleep(sleep_time)

def long_lazy_break():
    """Take a longer, lazy break."""
    sleep_time = random.uniform(5, 12)
    print(f"Long lazy break for {sleep_time:.2f} seconds")
    time.sleep(sleep_time)

def random_point_movement(min_x, min_y, max_x, max_y):
    """Move to a random point on screen with random duration."""
    print("Moving to random point...")
    random_x = random.randint(min_x, max_x - 1)
    random_y = random.randint(min_y, max_y - 1)
    duration = random.uniform(0.3, 1.2)
    pyautogui.moveTo(random_x, random_y, duration=duration)

# === AGGRESSIVE MOVEMENT FUNCTIONS ===

def big_fast_sweeping(min_x, min_y, max_x, max_y):
    """
    Performs large, fast sweeping movements across the entire screen - aggressive and dramatic.
    """
    print("Performing big fast sweeping movements...")
    
    # Define different types of sweeping patterns
    sweep_patterns = [
        # Diagonal sweeps
        [(min_x, min_y), (max_x - 1, max_y - 1)],  # Top-left to bottom-right
        [(max_x - 1, min_y), (min_x, max_y - 1)],  # Top-right to bottom-left
        [(min_x, max_y - 1), (max_x - 1, min_y)],  # Bottom-left to top-right
        [(max_x - 1, max_y - 1), (min_x, min_y)],  # Bottom-right to top-left
        
        # Horizontal sweeps
        [(min_x, (min_y + max_y) // 2), (max_x - 1, (min_y + max_y) // 2)],  # Left to right
        [(max_x - 1, (min_y + max_y) // 2), (min_x, (min_y + max_y) // 2)],  # Right to left
        
        # Vertical sweeps
        [((min_x + max_x) // 2, min_y), ((min_x + max_x) // 2, max_y - 1)],  # Top to bottom
        [((min_x + max_x) // 2, max_y - 1), ((min_x + max_x) // 2, min_y)],  # Bottom to top
        
        # Arc sweeps
        [(min_x, min_y), ((min_x + max_x) // 2, max_y - 1), (max_x - 1, min_y)],  # Arc sweep
        [(max_x - 1, max_y - 1), ((min_x + max_x) // 2, min_y), (min_x, max_y - 1)],  # Reverse arc
    ]
    
    # Perform 3-5 random sweeping movements
    num_sweeps = random.randint(3, 5)
    
    for _ in range(num_sweeps):
        pattern = random.choice(sweep_patterns)
        
        # If it's a multi-point pattern (like arcs), move through all points
        for i, (x, y) in enumerate(pattern):
            if i == 0:
                # First point - move there quickly but not instantly
                duration = random.uniform(0.15, 0.25)
            else:
                # Subsequent points - very fast sweeping motion
                duration = random.uniform(0.08, 0.15)
            
            pyautogui.moveTo(x, y, duration=duration)
            
            # Very brief pause between sweep segments
            if i < len(pattern) - 1:
                time.sleep(random.uniform(0.02, 0.05))
        
        # Brief pause between complete sweeps
        time.sleep(random.uniform(0.1, 0.2))

def frustrated_scribbling(min_x, min_y, max_x, max_y):
    """
    Rapid back-and-forth scribbling movements as if frantically searching for the cursor.
    """
    print("Performing frustrated scribbling...")
    
    # Get current position or pick a random starting point
    current_x, current_y = pyautogui.position()
    
    # Define a scribble area around current position
    scribble_size = 150
    center_x = max(min_x + scribble_size//2, min(max_x - scribble_size//2, current_x))
    center_y = max(min_y + scribble_size//2, min(max_y - scribble_size//2, current_y))
    
    # Perform rapid scribbling motions
    for _ in range(15):  # 15 rapid movements
        # Random point within scribble area
        scribble_x = center_x + random.randint(-scribble_size//2, scribble_size//2)
        scribble_y = center_y + random.randint(-scribble_size//2, scribble_size//2)
        
        # Ensure within bounds
        scribble_x = max(min_x, min(max_x - 1, scribble_x))
        scribble_y = max(min_y, min(max_y - 1, scribble_y))
        
        # Very fast, erratic movement
        duration = random.uniform(0.03, 0.08)
        pyautogui.moveTo(scribble_x, scribble_y, duration=duration)
        time.sleep(random.uniform(0.01, 0.02))

def upward_jabbing(min_x, min_y, max_x, max_y):
    """
    Series of rapid upward jabbing movements, like angry pointing or clicking.
    """
    print("Performing upward jabbing movements...")
    
    current_x, current_y = pyautogui.position()
    
    # Perform 8-12 jabbing motions
    num_jabs = random.randint(8, 12)
    
    for i in range(num_jabs):
        # Start from current or slightly varied x position
        start_x = max(min_x, min(max_x - 1, current_x + random.randint(-30, 30)))
        start_y = max(min_y + 100, min(max_y - 50, current_y + random.randint(-20, 20)))
        
        # Jab upward
        jab_distance = random.randint(40, 80)
        end_y = max(min_y, start_y - jab_distance)
        
        # Quick upward movement
        pyautogui.moveTo(start_x, start_y, duration=random.uniform(0.05, 0.1))
        pyautogui.moveTo(start_x, end_y, duration=random.uniform(0.03, 0.06))
        
        # Brief pause between jabs
        time.sleep(random.uniform(0.02, 0.05))
        
        current_x = start_x

def angry_shaking(min_x, min_y, max_x, max_y):
    """
    Rapid shaking movement back and forth, like an angry gesture.
    """
    print("Performing angry shaking...")
    
    current_x, current_y = pyautogui.position()
    
    # Ensure we're in a safe area for shaking
    shake_x = max(min_x + 50, min(max_x - 50, current_x))
    shake_y = max(min_y + 50, min(max_y - 50, current_y))
    
    # Perform rapid shaking motions
    for _ in range(20):  # 20 rapid shakes
        # Shake left and right
        offset_x = random.randint(-40, 40)
        offset_y = random.randint(-15, 15)  # Mostly horizontal shaking
        
        target_x = max(min_x, min(max_x - 1, shake_x + offset_x))
        target_y = max(min_y, min(max_y - 1, shake_y + offset_y))
        
        # Very fast movement
        duration = random.uniform(0.02, 0.05)
        pyautogui.moveTo(target_x, target_y, duration=duration)
        time.sleep(random.uniform(0.01, 0.02))

def frantic_corner_search(min_x, min_y, max_x, max_y):
    """
    Frantically moves to different corners and edges of the screen, 
    like searching for something urgently.
    """
    print("Performing frantic corner search...")
    
    # Define corner and edge positions with some margin
    margin = 50
    positions = [
        (min_x + margin, min_y + margin),  # Top-left
        (max_x - margin, min_y + margin),  # Top-right  
        (min_x + margin, max_y - margin),  # Bottom-left
        (max_x - margin, max_y - margin),  # Bottom-right
        ((min_x + max_x) // 2, min_y + margin),  # Top-center
        ((min_x + max_x) // 2, max_y - margin),  # Bottom-center
        (min_x + margin, (min_y + max_y) // 2),  # Left-center
        (max_x - margin, (min_y + max_y) // 2)   # Right-center
    ]
    
    # Randomly visit 5-7 positions very quickly
    num_searches = random.randint(5, 7)
    selected_positions = random.sample(positions, num_searches)
    
    for x, y in selected_positions:
        # Fast movement to position
        duration = random.uniform(0.08, 0.15)
        pyautogui.moveTo(x, y, duration=duration)
        
        # Brief pause as if "looking"
        time.sleep(random.uniform(0.05, 0.12))

def aggressive_zigzag(min_x, min_y, max_x, max_y):
    """
    Like the normal zigzag but much faster and more erratic - aggressive version.
    """
    print("Performing aggressive zigzag...")
    
    # Calculate the step size for moving down (larger steps = faster)
    screen_height = max_y - min_y
    step_size = screen_height // 8  # Fewer bands = bigger jumps
    
    start_time = time.time()
    target_duration = 3.0  # Faster than normal zigzag
    iterations = 8  # Fewer iterations but more aggressive
    
    for i in range(iterations):
        current_y = min_y + (i * step_size)
        
        # Ensure we don't go beyond screen bounds
        if current_y >= max_y:
            current_y = max_y - 1
            
        # Much faster timing
        iteration_duration = target_duration / (iterations * 2)
        
        # Add some randomness to x positions for more erratic movement
        left_x = min_x + random.randint(0, 30)
        right_x = max_x - random.randint(0, 30)
        
        # Move to left side (with variation)
        pyautogui.moveTo(left_x, current_y, duration=iteration_duration * 0.7)
        
        # Move to right side (with variation)
        pyautogui.moveTo(right_x, current_y, duration=iteration_duration * 0.7)
        
        # Check if we've exceeded our target time
        if time.time() - start_time >= target_duration:
            break
    
    elapsed_time = time.time() - start_time
    print(f"Aggressive zigzag completed in {elapsed_time:.2f} seconds")
