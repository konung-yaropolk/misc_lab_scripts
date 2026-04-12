echo on
cd /d "%~dp0"
pyinstaller --name="autoclicker" --onefile --clean autoclicker.py
pyinstaller --name="recorder" --onefile --clean recorder.py
pyinstaller --name="get_mouse_position" --onefile --clean get_mouse_position.py

@REM dont use optimization, it causes ignoring assertions in python code
@REM dont use upx, it uses twice more RAM [--upx-dir upx] flag
pause