import cherrypy


class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
        <head></head>
        <body>
            <div><a href="getsorteddata?reverse=True&criteria=price">Get Sorted Data</a></div>
            <div><a href="getsorteddata?reverse=True&criteria=price">Any single item by id</a></div>
            <div><a href="getsorteddata?reverse=True&criteria=price">List of items by </a></div>
            <div><a href="getsorteddata?reverse=True&criteria=price">An array of items based on radius</a></div>
        </body>
        </html>
        
        """
    
    @cherrypy.expose
    def getsorteddata(self,reverse='False',criteria='price'):
        res= try1.getSortedData('True', criteria)
        l=[]
        s="""<html><head></head><body>"""
        for i in res:
            s+= """<div>"""+ i+ """</div>"""
        
        s+= """</body></html>""" 

        return s


import try1
if __name__ == '__main__':
    cherrypy.quickstart(HelloWorld())





=============================================





# import urllib library
from logging import NullHandler
from urllib.request import urlopen

# import json
import json
# store the URL in url as
# parameter for urlopen
url = "https://run.mocky.io/v3/65c043be-b3a3-40d5-bc17-e2746f5bdcf2"

# store the response of URL
response = urlopen(url)


# storing the JSON response
# from url in data
data_json = json.loads(response.read())
# print(data_json[0])
# for i in data_json[0]:
#     print(i,data_json[0]['id'])

from peewee import *

db= SqliteDatabase('salesDetails.db')

class itemDetails(Model):
    id= CharField(default='NA')
    latitude= DoubleField(default='NA')
    longitude= DoubleField(default='NA')
    userid= CharField(default='NA')
    description= TextField(null=True)
    price= FloatField(default='NA')
    status= CharField(default='NA')

    class Meta:
        database= db

db.connect()

db.create_tables([itemDetails])

itemid={}


for item in data_json:
    temp= item['id']
    itemid[temp]= 1
    #try:
    itemid[temp]= itemDetails.create(id=item['id'], latitude= item['loc'][0], longitude= item['loc'][1], userid= item['userId'], description= item['description'], price= item['price'], status= item['status'])
    # except:
    #     itemid[temp]= itemDetails.create(id=item['id'], latitude= item['loc'][0], longitude= item['loc'][1], userid= item['userId'], description= 'null', price= item['price'], status= item['status'])


def getSortedData(reverse,criteria):
    s=[]
    if criteria=='price' and reverse=='True':
        for item in itemDetails.select().order_by(itemDetails.price.desc()):
            s.append("\n".join([item.id,"("+str(item.latitude)+","+str(item.longitude)+")",item.userid,str(item.description),str(item.price),item.status]))
    else:
        for item in itemDetails.select().order_by(itemDetails.price):
            s.append("\n".join([item.id,"("+str(item.latitude)+","+str(item.longitude)+")",item.userid,str(item.description),str(item.price),item.status]))
    
    return s


