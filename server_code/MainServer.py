import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from datetime import datetime
import pybase64

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
  app_tables.uploads.add_row(created=datetime.now(),UserID=user,**postDict,Upvotes=0)
  
@anvil.server.callable
def getPosts():
  return app_tables.uploads.search(tables.order_by("created",ascending=False))

@anvil.server.callable
def getUUID(email):
  encodedEmail = email.encode("utf-8")
  uuid = pybase64.b64encode(encodedEmail)
  encodedEmailString = uuid.decode("utf-8")
  return encodedEmailString