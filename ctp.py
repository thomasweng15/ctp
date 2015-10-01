
# To Do
# Timer functionality using cron
# Plaintext file of pictures/indices already uploaded
#   On launch, check file 
# Log file
# Tumblr API

import sys
import argparse

class CTP():
	def __init__(self, logf, indexf):
		self.logf = open(logf, 'a')
		self.indexf = open(indexf, 'a')	
		# call function to init Tumblr API access	

	def cleanup(self):
		self.logf.close()
		self.indexf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tumblr photo poster')
	parser.add_argument('-l', help='log file', default='log.txt')
	parser.add_argument('-i', help='index file', default='index.txt')
	args = parser.parse_args()

	ctp = CTP(args.l, args.i)
	ctp.cleanup()

