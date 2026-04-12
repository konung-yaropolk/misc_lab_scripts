import pyautogui
import time

print("🖱️  Move your mouse over each button/field.")
print("   Coordinates will update live. Press Ctrl+C when done.\n")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Current mouse position → X: {x:4} | Y: {y:4}", end="\r")
        time.sleep(0.2)
except KeyboardInterrupt:
    print("\n\nCaptured last position:", pyautogui.position())