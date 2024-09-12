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
    image = self.image_1.source
    comments = {}
    open_form('PostForm',parameters = {
      "title": title,
      "content": content,
      "media": image,
      "upvotes": self.item['Upvotes'],
      "comments": comments})

  def Upvote_click(self, **event_args):
    self.item['Upvotes'] = self.item['Upvotes'] + 1
    Upvotes = self.item['Upvotes'] + 1
    self.Upvote.bold = True
    postID = self.item['postID']
    self.users = [
      (user["email"], user) for user in app_tables.users.search()
    ]
    userID = anvil.server.call('getUUID',user['email'])
    print(postID,anvil.users.get_user())
    app_tables.upvote_data.add_row(postID_UV=postID,userID_UV=userID,upvotes_UV = Upvotes)


    
    
