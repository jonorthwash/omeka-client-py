#!/usr/bin/python

import json
from omekaclient import OmekaClient

import io
import base64

client = OmekaClient("http://www.indiana.edu/~srifias/omeka/api", "REPLACE WITH REAL KEY")

# GET /items/:id
#response, content = client.get("items", id=63)
#print(response,content)

# GET /items
#response, content = client.get("items")

# POST /items

response, content = client.post("items", data='{"public":true}')
#print(response,content)
ID = json.loads(content.decode('utf8'))['id'] 
#ID = 63
#YEAR = 1906
#id = 7

ALLDATA = {
	"item_type":
	{
		"html":False,
		"id": 18
	},
	"collection":
	{
		"html":False,
		"id": 2 
	},
	"element_texts":
	[
		{
			"html":False,
			"text": YEAR,
			"element_set":
			{
				"html":False,
				"id":3,
			},
			"element":
			{
				"html":False,
				"id":52,
				"name":"Year",
			}
		},

	]
} # Issues of Molla Nәsrәddin

#ALLDATA = '{"item_type": {"id": %s}, "collection": {"id": 2}, "element_texts":[{"text": 1906,	"element_set": { "id":3 },"element": {"id":52, "name":"Year"}}]}' % ID
#ALLDATA = '{"item_type": {"id": %s}}' % ID

# PUT /items/:id
#response, content = client.put("items", 1, data='{"public":false}')
#id = content['id']
print(json.dumps(ALLDATA))
response, content = client.put("items", ID, data=json.dumps(ALLDATA))
print(response,content)

# DELETE /items/:id
#response, content = client.delete("items", 1)

filename = "/Users/jonathan/Desktop/MN/1906/compressed/MN 1 (1906)—1_compressed_compressed.jpg"
#with open(filename, 'rb') as fn:
#	contents = fn.read()
file = open(filename, 'rb')
readfile = file.read()
#print(readfile)
#print(len(readfile))
contents = readfile

#contents = base64.b64encode(readfile).decode('ascii')
##contents = str(open(filename, 'rb').read())
#print(contents)
filename="MN 1 (1906)-1_compressed_compressed.jpg"
#n=70
#contents = '\r\n'.join([contents[i:i+n] for i in range(0, len(contents), n)])

#contents = str(contents)
#contents = contents.replace('"', '\\"')

fields = {"collection": {
			"html":False,
			"id":2,
			"resource":"collections"
		},
		"item": {
			"html":False,
			"id": ID
		}
	}
#data = fields
data = json.dumps(fields)
#data = "collection: 2"
response, content = client.post_file(data, filename, contents)

#{'status': '200', 'content-length': '2018', 'content-location': 'http://www.indiana.edu/~srifias/omeka/api/items/1?key=6daa92a0ebce6605f7eba1cbdb0ee7e3051cfbb7', 'transfer-encoding': 'chunked', 'set-cookie': 'X-Mapping-gbooldlg=D8E5A3D169E143C2241ED944B86D1D12;path=/', 'x-powered-by': 'PHP/5.3.26', 'vary': 'Accept-Encoding', 'server': 'Apache', '-content-encoding': 'gzip', 'date': 'Thu, 03 Apr 2014 15:07:05 GMT', 'content-type': 'application/json'} b'{"id":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/items\\/1","public":true,"featured":true,"added":"2014-03-31T18:28:00+00:00","modified":"2014-03-31T19:20:22+00:00","item_type":{"id":18,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/item_types\\/18","name":"Molla N\\u04d9sr\\u04d9ddin issue","resource":"item_types"},"collection":{"id":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/collections\\/1","resource":"collections"},"owner":{"id":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/users\\/1","resource":"users"},"files":{"count":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/files?item=1","resource":"files"},"tags":[],"element_texts":[{"html":false,"text":"Beating","element_set":{"id":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/element_sets\\/1","name":"Dublin Core","resource":"element_sets"},"element":{"id":50,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/elements\\/50","name":"Title","resource":"elements"}},{"html":false,"text":"Az\\u04d9rbaycanca","element_set":{"id":1,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/element_sets\\/1","name":"Dublin Core","resource":"element_sets"},"element":{"id":44,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/elements\\/44","name":"Language","resource":"elements"}},{"html":false,"text":"4","element_set":{"id":3,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/element_sets\\/3","name":"Item Type Metadata","resource":"element_sets"},"element":{"id":54,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/elements\\/54","name":"Issue","resource":"elements"}},{"html":false,"text":"Everyone is beating poor Hoca N\\u04d9sr\\u04d9ddin for reading a comic about himself.","element_set":{"id":3,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/element_sets\\/3","name":"Item Type Metadata","resource":"element_sets"},"element":{"id":56,"url":"http:\\/\\/www.indiana.edu\\/~srifias\\/omeka\\/api\\/elements\\/56","name":"Exposition","resource":"elements"}}],"extended_resources":[]}'

print(response, content)
