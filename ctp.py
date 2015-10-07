#! /usr/bin/env python

from os import listdir
import sys
import argparse
import pytumblr
import random

class CTP():
	def __init__(self, indexf, photodir):
		# TODO check that indexf exists
		self.indexf = indexf
		self.photodir = photodir
		with open(self.indexf, 'r') as f:
			uploaded = [l.strip() for l in f]
		all_photos = listdir(self.photodir)
		self.photos_list = list(set(all_photos) - set(uploaded))

		self.api_key = 'VABuQIpKd3HPGJlXUVtA4nLOjAkgfzfzhGAIvrh5AYH15b1lLK'
		self.api_secret = 'eTCnWarGzAyn5oIIZUkSHt7JdIUpYzS5lq7oZTx7zz4TjVTiH8'
		self.oauth_token = 'tHZItSfPprgbXHsDDx1MgzGolv0IMwc6ccfd3MrAiH3ZTbqRGR'
		self.oauth_secret = 'OlvCCgAwwtSiIJTHcE6nMINORFcenDx92D6X8u1sSAfwdE3xa9'

		self.client = pytumblr.TumblrRestClient(
			self.api_key,
			self.api_secret,
			self.oauth_token,
			self.oauth_secret)

		self.random = random
		self.random.seed()

	def post_random_photo(self):
		count = len(self.photos_list)
		if count == 0:
			print "No more photos to post!"
			return

		i = 0
		if count > 1:
			i = self.random.randint(0, count - 1)
		self.post(self.photos_list[i])

	def post(self, name):
		resp = self.client.create_photo(
			"chihiroandthomas",
			state="published",
			tags=["photobot"],
			data=self.photodir + name)

		print "Posted " + name + " as id " + str(resp["id"])

		with open(self.indexf, "a") as f:
			f.write(name + '\n')

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Tumblr photo poster')
	parser.add_argument('-i', help='index file', default='index.txt')
	parser.add_argument('-p', help='photos dir', default='photos/')
	args = parser.parse_args()

	ctp = CTP(args.i, args.p)
	ctp.post_random_photo()
