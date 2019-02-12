from sys import argv
import os

script, path = argv

total_size = 0

for root, dirs, files in os.walk(path):
	for file in files:
		file_path = os.path.join(root, file)
		total_size += os.stat(file_path).st_size

if total_size > 10**9: # GB
	msg = str(total_size/10**9) + ' GB'
elif total_size > 10**6: # MB
	msg = str(total_size/10**6) + ' MB'
elif total_size > 10**3: # KB
	msg = str(total_size/10**3) + ' KB'
else: # Bytes
	msg = str(total_size) + ' Bytes'
print(msg)