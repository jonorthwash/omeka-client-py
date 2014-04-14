#!/usr/bin/env python3

import json
from omekaclient import OmekaClient
import os

dirBase = "/Users/jonathan/Desktop/MN/compressed/"
subDirSemantics = ("Year", 3, 52)
subDirMapping = {1906: 2, 1907: 3, 1908: 4, 1909: 5}

client = OmekaClient("http://www.indiana.edu/~srifias/omeka/api", "6daa92a0ebce6605f7eba1cbdb0ee7e3051cfbb7")



def newItem(fullPath, thisDir, filename):
	global subDirSemantics
	global subDirMapping
	global client

	ALLDATA = {
		"item_type":
		{
			"html":False,
			"id": 18                             # the item type ID
		},
		"collection":
		{
			"html":False,
			"id": subDirMapping[subDir]          # the collection ID
		},
		"element_texts":
		[
			{
				"html":False,
				"text": subDir,
				"element_set":
				{
					"html":False,
					"id":subDirSemantics[1],     # the group of metadata fields being used
				},
				"element":
				{
					"html":False,
					"id":subDirSemantics[2],     # the ID of the category
					"name":subDirSemantics[0],   # the name of the category
				}
			},
		]
	}
	
	# make an empty item, and get its item id
	response, content = client.post("items", data='{"public":true}')
	itemId = json.loads(content.decode('utf8'))['id'] 
	
	# give the item some metadata
	response, content = client.put("items", itemId, data=json.dumps(ALLDATA))

	# read file to add to item
	thisFile = open(fullPath, 'rb')
	contents = thisFile.read()

	# make sure we're posting the file to the right item
	fields = {"collection": {
				"html":False,
				"id":subDirMapping[subDir],      # the collection ID
				"resource":"collections"
			},
			"item": {
				"html":False,
				"id": itemId,                    # the item ID
			}
		}
	data = json.dumps(fields)
	
	# post the file
	response, content = client.post_file(data, filename, contents)
	print(response)
	

for subDir in subDirMapping:
	thisSubDir = os.path.join(dirBase, str(subDir))
	if os.path.exists(thisSubDir):
		files = os.listdir(thisSubDir)
		for filename in files:
			fullPath = os.path.join(thisSubDir, filename)
			if "image" in client.get_content_type(fullPath):
				newItem(fullPath, subDir, filename)