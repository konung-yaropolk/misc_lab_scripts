import pyautogui
import time
import sys
import json
from pathlib import Path

# ========================== SAFETY SETTINGS ==========================
pyautogui.FAILSAFE = True      # Move mouse to TOP-LEFT corner to emergency STOP
pyautogui.PAUSE = 0.1

# ======================= LOAD WORKFLOW FROM JSON =======================
def load_workflow():
    # 1. Try command line argument first
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
        if file_path.exists():
            return load_file(file_path)
        else:
            print(f"⚠️  File from argument not found: {file_path}")

    # 2. Try default workflow.json in the same folder
    default_path = Path(__file__).parent / "workflow.json"
    if default_path.exists():
        return load_file(default_path)

    # 3. If nothing found → ask user for path
    print("\n❌ Default workflow.json not found.")
    print("Please provide the full path to your workflow JSON file.\n")
    
    while True:
        user_input = input("Enter path to workflow.json (or press Enter to cancel): ").strip()
        
        if not user_input:
            print("Cancelled by user.")
            sys.exit(0)
        
        file_path = Path(user_input).resolve()
        
        if file_path.exists() and file_path.suffix.lower() == ".json":
            return load_file(file_path)
        else:
            print(f"❌ File not found or not a .json file: {file_path}")
            print("Please try again.\n")


def load_file(file_path: Path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        print(f"✅ Successfully loaded workflow: {file_path.name}")
        return data
    except Exception as e:
        print(f"❌ Error reading JSON file: {e}")
        sys.exit(1)


# Load the workflow
workflow = load_workflow()

actions = workflow.get("actions", [])
repetitions = workflow.get("repetitions", 1)

# =====================================================================

def execute_action(action, current_rep):
    if action["type"] == "click":
        pyautogui.click(action["x"], action["y"])
        print(f"✅ Clicked at ({action['x']}, {action['y']})")
    
    elif action["type"] == "type":
        final_text = action["text"].replace("{rep}", str(current_rep))
        pyautogui.typewrite(final_text)
        print(f"✅ Typed: {final_text}   (repetition {current_rep})")
    
    time.sleep(action.get("delay", 1.0))


def main():
    print(f"\n🚀 Autoclicker ready — {len(actions)} actions × {repetitions} repetitions")
    print("   → Move mouse to top-left corner of screen to stop anytime\n")
    
    try:
        input("Press ENTER to START the automation...")
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(0)

    for rep in range(1, repetitions + 1):
        print(f"\n🔄 Repetition {rep}/{repetitions}")
        for action in actions:
            try:
                execute_action(action, rep)
            except KeyboardInterrupt:
                print("\n⛔ Stopped by user.")
                sys.exit(0)
            except Exception as e:
                print(f"❌ Error during execution: {e}")
                sys.exit(1)
    
    print("\n✅ Automation completed successfully!")


if __name__ == "__main__":
    main()