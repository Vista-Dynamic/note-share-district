from ._anvil_designer import PostFormTemplate
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class PostForm(PostFormTemplate):
  def __init__(self, parameters, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties,**parameters)
    
    print("Testing Error")
    self.link_1.text = parameters['title']
    self.content.content = parameters['content']
    if parameters["media"] is not None:
      print(parameters["media"])
      self.image_1.source = parameters['media']
    self.Upvote.text = parameters['upvotes']
    for i, v in parameters.items():
      print(i)
      print(v)

  def getUUID(self):
    self.users = [
      (user['email'], user) for user in app_tables.users.search()
    ]
    if anvil.users.get_user():
      uuid = anvil.server.call('getUUID', user['email'])
      print(uuid)
      return uuid

  def button_2_click(self, **event_args):
    open_form("Form1")

  def button_1_click(self, **event_args):
    if anvil.users.get_user():
      print(f"Commenting {self.comment.text}")
    if self.comment.text == "":
      print("No comment given")
    else:
      print("Commenting...")
      content = {"CommentText": self.comment.text, "CommentImage": self.file_loader_1.file}
      print(content["CommentText"])
      anvil.server.call("addComment", content)
      self.comment.text = ""

  def file_loader_1_change(self, file, **event_args):
    # Handle file upload here
    print(f"File uploaded: {file.name}")
    self.file_loader_1.file = file


