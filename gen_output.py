import sys
import os
import subprocess

inputs = [
    'inputs/kittens.in',
    'inputs/me_at_the_zoo.in',
    'inputs/trending_today.in',
    'inputs/videos_worth_spreading.in',
]

main_file = sys.argv[1]

for in_file in inputs:
    out_file = in_file.split('/')[1][:-2] + 'out'
    command = ' '.join(["python3", main_file, "<", in_file, ">", out_file])
    print("Running:", command)
    return_code = subprocess.call([command], shell=True)
    print(in_file, "return code:", return_code)
    print("-------")


source_paths = []
for thing_in_dir in os.listdir('.'):
    if thing_in_dir.endswith('.py'):
        source_paths.append(thing_in_dir)

print("Zipping:", ', '.join(source_paths))
command = "zip source.zip " + ' '.join(source_paths)
subprocess.call([command], shell=True)
