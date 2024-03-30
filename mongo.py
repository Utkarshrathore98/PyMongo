from pymongo import MongoClient
import datetime

client = MongoClient()

app_db = client.Test_Database
app_col = app_db.utkarsh_collection

data = {
    "author": "Utkarsh",
    "text": "Hi, I am utkarsh rathore",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc),
}

app_col.insert_one(data)