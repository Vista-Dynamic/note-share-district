import anvil.server
from ..CreatePost import CreatePost
from ._anvil_designer import Form1Template
from anvil import *
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import time


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.users = [
      (user['email'], user) for user in app_tables.users.search()
    ]
    print(self.users)

    # Any code you write here will run before the form opens.

  def repeating_panel_show(self, **event_args):
    self.repeating_panel.items = (
      {"name": "Name", "image": "ImageID"},
      {"name": "Name2", "image": "ImageID2"}
    )
    time.sleep(5)
    print(f"self.item = {self.item}")
    #alert((f"self.item = {self.item}"))


  def button_1_click(self, **event_args):
    #open_form('CreatePost')
    newPost = {}
    postCreate = alert(
      content =CreatePost(),
      title="Create Post",
      large=True,
      buttons=[("Create Post", True), ("Cancel", False)]
    )
    if postCreate:
      print(newPost)
  def button_3_click(self, **event_args):
    user = anvil.users.login_with_form()
    if user:
      print(user)
      self.LogIn.visible = False


