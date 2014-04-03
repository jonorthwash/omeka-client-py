#!/usr/bin/python

from omekaclient import OmekaClient

client = OmekaClient("http://www.indiana.edu/~srifias/omeka/api", "6daa92a0ebce6605f7eba1cbdb0ee7e3051cfbb7")

# GET /items/:id
response, content = client.get("items", id=1)

# GET /items
#response, content = client.get("items")

# POST /items
#response, content = client.post("items", data='{"public":true}')

# PUT /items/:id
#response, content = client.put("items", 1, data='{"public":false}')

# DELETE /items/:id
#response, content = client.delete("items", 1)

print(response, content)
