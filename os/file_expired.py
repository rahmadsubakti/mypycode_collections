import os
import sys
import time
import datetime
from path_file import scan_file_path

today = datetime.datetime.today()
script, path = sys.argv

def file_expired(path):
	# expired date taken one year before today
	expired_date = today - datetime.timedelta(days=365.24)
	expired_time = time.mktime(expired_date.timetuple())
	
	for file in scan_file_path(path):
		if os.stat(file).st_ctime < expired_time:
			print(file)
	
if __name__ == '__main__':
	file_expired(path)