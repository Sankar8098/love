import os
from mongoengine import connect, Document, IntField

# Load config based on environment
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# Connect to MongoDB
connect(db="sankar", host=Config.DB_URI)

# Define the Thumbnail model
class Thumbnail(Document):
    id = IntField(primary_key=True)
    msg_id = IntField()

# Function to add/update a thumbnail
async def df_thumb(id, msg_id):
    thumb = Thumbnail.objects(id=id).first()
    if thumb:
        thumb.msg_id = msg_id
    else:
        thumb = Thumbnail(id=id, msg_id=msg_id)
    thumb.save()

# Function to delete a thumbnail
async def del_thumb(id):
    Thumbnail.objects(id=id).delete()

# Function to retrieve a thumbnail
async def thumb(id):
    return Thumbnail.objects(id=id).first()
    
