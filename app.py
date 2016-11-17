# -*- coding: utf-8 -*-

from eve import Eve
app = Eve()

#delete the _created and _updated fields, we dont want those
def on_fetched_resource(resource, response):
    for document in response['_items']:
        del(document['_created'])
        del(document['_updated'])
        # etc.

app = Eve()
app.on_fetched_resource += on_fetched_resource

if __name__ == '__main__':
    app.run(port=8962, host='0.0.0.0')