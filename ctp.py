#!/usr/bin/python

import sys
import argparse
import pytumblr

class CTP():
	def __init__(self, indexf):
		self.indexf = open(indexf, 'a')

		self.api_key = 'VABuQIpKd3HPGJlXUVtA4nLOjAkgfzfzhGAIvrh5AYH15b1lLK'
		self.api_secret = 'eTCnWarGzAyn5oIIZUkSHt7JdIUpYzS5lq7oZTx7zz4TjVTiH8'
		self.oauth_token = 'tHZItSfPprgbXHsDDx1MgzGolv0IMwc6ccfd3MrAiH3ZTbqRGR'
		self.oauth_secret = 'OlvCCgAwwtSiIJTHcE6nMINORFcenDx92D6X8u1sSAfwdE3xa9'

		self.client = pytumblr.TumblrRestClient(
			self.api_key,
			self.api_secret,
			self.oauth_token,
			self.oauth_secret)

	def post(self):
		print self.client.create_photo(
			"chihiroandthomas",
			state="published",
			tags=["photos-in-review"],
			data="./test.jpg")

	def cleanup(self):
		self.indexf.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tumblr photo poster')
	parser.add_argument('-i', help='index file', default='index.txt')
	args = parser.parse_args()

	ctp = CTP(args.i)
	ctp.post()
	ctp.cleanup()
