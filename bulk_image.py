import os
import sys
import requests
mytoken = "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"

def download_images(url):
	index = 0
	img_name = 0
	list_img = []
	while i <=  969:
		endpoint = url + index
		response = requests.get(endpoint)
		img = open(f"img_name_{index}.png", "wb")
		img.write(response.content)
		img.close()
		list_img.append(img)
		index = index + 1
		i = i + 1
	return list_img

