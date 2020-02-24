import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO,
#                         format='%(asctime)s - %(message)s',
#                         datefmt='%Y-%m-%d %H:%M:%S')
#     path = sys.argv[1] if len(sys.argv) > 1 else '.'
#     event_handler = LoggingEventHandler()
#     observer = Observer()
#     observer.schedule(event_handler, path, recursive=True)
#     observer.start()
#     try:
#         while True:
#             time.sleep(1)
#     except KeyboardInterrupt:
#         observer.stop()
#     observer.join()
	
	
	
	
	
	
	
	
	
# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import os, shutil, time, json

# class MyHandler(FileSystemEventHandler):
# 	i = 1
# 	def on_modifier(self, event):
# 		for fn in os.listdir(ftt):
# 			src = ftt + '/' + fn
# 			nd = fd + '/' + fn
# 			os.rename(src, nd)

# ftt = 'C:\\Users\\wikyprash\\Desktop\\mf\\a'
# fd = 'C:\\Users\\wikyprash\\Desktop\\mf\\b'
# e_h = MyHandler()
# observer = Observer()
# observer.schedule(e_h, ftt, recursive = True)
# observer.start()

# try:
# 	while True:
# 		time.sleep(10)
# except KeyboardInterrupt:
# 	observer.stop()
# observer.join()
