# 2. write  a function to fetch a data from mongodb table

from flask import Flask, request, jsonify
import pymongo
app = Flask(__name__)


@app.route("/conn_mongo",  methods=["GET", "POST"])

def home():

    if request.method == "POST":
        client = pymongo.MongoClient("mongodb+srv://mongodb:mongodb@cluster0.qjmki.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = client.sudh
        files = db.ineuron_collection.find()
        return jsonify(str([file for file in files]))

if __name__ == '__main__':
    app.run()
