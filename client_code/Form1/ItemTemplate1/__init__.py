from ._anvil_designer import ItemTemplate1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class ItemTemplate1(ItemTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    title = self.link_1.text
    content = self.content.content
#    if self.item['media']:
#      image = self.item['media']
    comments = {}
    open_form('PostForm',parameters = {
      "title": title,
      "content": content,
#     "media": image,
      "upvotes": self.item['Upvotes'],
      "comments": comments})

  def Upvote_click(self, **event_args):
    self.users = [
      (user["email"], user) for user in app_tables.users.search()
    ]
    userID = anvil.server.call('getUUID',user['email'])
    existing_upvote = app_tables.upvote_data.get(postID_UV=self.item["postID"],userID_UV=userID)
    if existing_upvote:
      print("Un-Upvoting")
      self.item['Upvotes'] = self.item['Upvotes'] - 1
      Upvotes = self.item['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = ""
      self.Upvote.bold = False
      postID = self.item['postID']
      DelRow = app_tables.upvote_data.get(postID_UV=postID,userID_UV=userID)
      DelRow.delete()
      
    else:
      print("Upvoting...")
      self.item['Upvotes'] = self.item['Upvotes'] + 1
      Upvotes = self.item['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = "theme:Secondary Container"
      self.Upvote.bold = True
      postID = self.item['postID']
      app_tables.upvote_data.add_row(postID_UV=postID,userID_UV=userID,upvotes_UV = Upvotes)
      