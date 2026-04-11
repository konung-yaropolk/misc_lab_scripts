import pyautogui
import keyboard  # pip install keyboard
import time
import sys

print("🎥 Mouse Click Recorder for Autoclicker")
print("=" * 55)
print("Instructions:")
print("   • Move mouse to desired position")
print("   • Press 'r'          → Record click at current position")
print("   • Press 't'          → Record a text field (you will type the text later)")
print("   • Press 'q' or ESC   → Quit and print ready-to-paste actions")
print("\nMake sure your legacy window is open and in the same position!\n")

actions = []
start_time = time.time()

def record_click():
    x, y = pyautogui.position()
    # Ask for delay after this click
    try:
        delay = float(input(f"   Click at ({x}, {y}) → Delay after (seconds, e.g. 1.5): ") or "1.0")
    except:
        delay = 1.0
    
    actions.append({
        "type": "click",
        "x": x,
        "y": y,
        "delay": delay
    })
    print(f"   ✅ Recorded CLICK at ({x}, {y}) | delay = {delay}s\n")


def record_text():
    x, y = pyautogui.position()
    print(f"   Text field at ({x}, {y})")
    text = input("   Enter the base text (use {{rep}} for repetition number): ") or "Text {rep}"
    
    try:
        delay = float(input("   Delay after typing (seconds): ") or "2.0")
    except:
        delay = 2.0
    
    actions.append({
        "type": "type",
        "text": text,
        "delay": delay
    })
    print(f"   ✅ Recorded TYPE '{text}' | delay = {delay}s\n")


print("Waiting for keys... (r = click, t = text, q = quit)\n")

try:
    while True:
        if keyboard.is_pressed('r'):
            record_click()
            time.sleep(0.3)   # prevent multiple triggers
        
        elif keyboard.is_pressed('t'):
            record_text()
            time.sleep(0.3)
        
        elif keyboard.is_pressed('q') or keyboard.is_pressed('esc'):
            break
        
        time.sleep(0.05)

except KeyboardInterrupt:
    pass

# ====================== PRINT READY-TO-PASTE CODE ======================
print("\n" + "="*60)
print("✅ RECORDING FINISHED!")
print("Copy the code below and paste it into your autoclicker.py\n")

print("actions = [")

for i, action in enumerate(actions):
    if action["type"] == "click":
        print(f'    {{"type": "click",  "x": {action["x"]}, "y": {action["y"]}, "delay": {action["delay"]}}},')
    else:
        print(f'    {{"type": "type",   "text": "{action["text"]}", "delay": {action["delay"]}}},')

print("]")

print(f"\n# Total actions recorded: {len(actions)}")
print(f"# Recording time: {time.time() - start_time:.1f} seconds")

print("\nNow paste this into your main autoclicker script!")