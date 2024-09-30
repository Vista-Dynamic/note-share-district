import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import pybase64
import uuid

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def addPost(postDict,user):
  postID = str(uuid.uuid4())
  app_tables.uploads.add_row(created=datetime.now(),UserID=user,**postDict,Upvotes=0,postID=postID)
  
@anvil.server.callable
def getPosts():
  return app_tables.uploads.search(tables.order_by("created",ascending=False))
  app_tables

@anvil.server.callable
def getUUID(email):
  encodedEmail = email.encode("utf-8")
  uuid = pybase64.b64encode(encodedEmail)
  encodedEmailString = uuid.decode("utf-8")
  print(encodedEmailString)
  print(uuid)
  return encodedEmailString

@anvil.server.callable
def addComment(comment,user):
  print("Sercer Recieved")
  app_tables.comments.add_row(Likes=0,Dislikes=0,CommentText=comment,UserCommented=user,DateCommented=datetime.now())

