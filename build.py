# build.py
import PyInstaller.__main__

PyInstaller.__main__.run([
    'Realtime_victoria_dam_Simulaion.py',    # Replace with your actual script
    '--onefile',              # Create a single executable file
    '--noconsole',            # Do not display a console window
    '--icon=icon.ico',
    '--name=VicDamSimu'    # Replace with your game name
])
