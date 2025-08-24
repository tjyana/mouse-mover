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
