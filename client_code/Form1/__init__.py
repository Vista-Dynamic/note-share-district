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

    if anvil.users.get_user():
      self.LogIn.visible = False
      self.logOut.visible = True
    #print(user['email'])
    self.refreshPosts() #May Cause Issues


    # Any code you write here will run before the form opens.

  """def repeating_panel_show(self, **event_args):
    self.repeating_panel.items = (
      {"name": "Name", "image": "ImageID"},
      {"name": "Name2", "image": "ImageID2"}
    )
    time.sleep(5)
    print(f"self.item = {self.item}")"""
    #alert((f"self.item = {self.item}"))


  def button_1_click(self, **event_args):
    #open_form('CreatePost')
    newPost = {}
    postCreate = alert(
      content = CreatePost(item=newPost),
      title="Create Post",
      large=True,
      buttons=[("Create Post", True), ("Cancel", False)]
    )

    self.users = [
      (user['email'], user) for user in app_tables.users.search()
    ]
    if anvil.users.get_user():
      uuid = anvil.server.call('getUUID',user['email'])
      print(uuid)
    if postCreate:
      if anvil.users.get_user():
        print(newPost)
        print(uuid)
        anvil.server.call('addPost',newPost,uuid)
        self.refreshPosts()
      else:
        alert("Please login before posting!")
  def button_3_click(self, **event_args):
    user = anvil.users.login_with_form()
    if user:
      print(user)
      self.LogIn.visible = False
      self.logOut.visible = True
  def refreshPosts(self):
    self.repeating_panel.items = anvil.server.call('getPosts')

  def logOut_click(self, **event_args):
    anvil.users.logout()
    self.logOut.visible = False
    self.LogIn.visible = True
    self.refresh_data_bindings()
