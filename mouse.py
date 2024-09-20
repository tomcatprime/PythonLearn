import pyautogui
import time
import keyboard

def keep_active():
    print("Press 'q' to stop the script.")
    while True:
        # Check if the 'q' key is pressed
        if keyboard.is_pressed('q'):
            print("Stopping the script...")
            break

        # Get the current position of the mouse
        current_mouse_position = pyautogui.position()

        # Move the mouse by a small amount and then move it back
        pyautogui.move(10, 0)  # Move mouse 1 pixel to the right
        time.sleep(0.5)       # Small delay
        pyautogui.move(-10, 0) # Move mouse back to original position

        # Wait for a few seconds before repeating the movement
        time.sleep(30)

if __name__ == "__main__":
    print("Running the script to keep your status active...")
    keep_active()