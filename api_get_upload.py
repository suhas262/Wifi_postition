from flask import Flask, jsonify, request
from flaskTest import *
import flaskTest
import xml.etree.ElementTree as ET
import requests

from suhas import *
app = Flask(__name__)

# @app.route("/")
# def testJSON():
#         x = "Test1"
#         y = "Test2"
#         r = requests.get("http://thecatapi.com/api/images/get?format=xml");
#         dict = {x:y}
#         return jsonify(dict)

@app.route("/uploadlog/",methods = ['GET', 'POST', 'DELETE'])
def getPostDataUploadLog():
    if request.method == 'POST':
        content = request.data
        return "OK"


#
# @app.route("/cat")
# def testCat():
#         x = "cat 1"
#         y = "Test2"
#         cat_copy,cat_list = call_cat_api()
#         insert_mongo(cat_list)
#         return jsonify(cat_copy)
#
#
# @app.route("/history")
# def testHistory():
#         x = "history"
#         y = "Test2"
#         endpoint_list = get_data_from_mongo()
#         return jsonify(image=endpoint_list)
if __name__ == "__main__":
        app.debug = True
        app.run()
