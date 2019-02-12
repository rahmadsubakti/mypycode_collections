from sys import argv
import os

script, path = argv

def scan_file_path(path):
	for root, dirs, files in os.walk(path):
		for filename in files:
			yield os.path.join(root, filename)
			
if __name__ == '__main__':
	scan_file_path(path)
