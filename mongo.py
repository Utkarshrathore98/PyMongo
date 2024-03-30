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
# Inserting one data to the collection
app_col.insert_one(data)

many_data = [
    {
        "author": "Urvashi",
        "text": "Hi, I am urvashi rathore",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc)
    },
    {
        "author": "Prapti",
        "text": "Hi, I am prapti rathore",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.now(tz=datetime.timezone.utc)
    },
]
#Inserting many data to the collection 
app_col.insert_many(many_data)