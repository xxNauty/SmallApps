import os
import subprocess

directory = "./tests"

files_ran = 0

for root, dirs, files in os.walk(directory):
    print(root, dirs, files)
    for filename in files:
        if filename.endswith('.py') and filename != 'run_all.py':
            filepath = os.path.join(root, filename)
            print(f'Running {filepath}...')
            subprocess.run(['python', filepath])
            files_ran += 1
print(f"Script ran {files_ran} files")
