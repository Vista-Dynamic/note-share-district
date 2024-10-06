from ._anvil_designer import PostFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from time import sleep


class PostForm(PostFormTemplate):
  def __init__(self, parameters, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.link_1.text = parameters['title']
    self.content.content = parameters['content']
    if parameters["media"]:
      self.image_1.source = parameters['media']
    self.Upvote.text = parameters['upvotes']
    print(parameters['postID'])
    global postIDG
    postIDG = parameters['postID']
    self.refreshComments()
    for i,v in parameters.items():
      print(i)
      print(v)
  

  def refreshComments(self):
    self.repeating_panel_1.items = anvil.server.call('getComments',postIDG)
  
  def getUUID(self):
    self.users = [
    (user['email'], user) for user in app_tables.users.search()
    ]
    if anvil.users.get_user():
      uuid = anvil.server.call('getUUID',user['email'])
      print(uuid)
      print("38")
      return uuid
      

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form("Form1")

  def button_1_click(self, **event_args):
    if anvil.users.get_user():
      print(f"Commenting {self.comment.text}")
    else:
      alert("Please log in!")
    if self.comment.text == "":
      print("No comment given")
    else:
      print("Commenting...")
      #self.comment.text = self.comment.placeholder
      content = self.comment.text
      image = self.file_loader_1.file
      #{"CommentText": self.comment.text}
      print(content)
      self.users = [
      (user['email'], user) for user in app_tables.users.search()
      ]
      uuid = anvil.server.call('getUUID',user['email'])
      print(postIDG)
      print(self.tag)
      print(self.label_1.text)
      postID = postIDG
      anvil.server.call("addComment",content,image,uuid,postID)
      sleep(.8)
      self.comment.text = ""
      self.file_loader_1.clear()
      self.refreshComments()

  def file_loader_1_change(self, file, **event_args):
    self.item['Comment_Image'] = file