import anvil.server
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
    open_form('CreatePost')

  def button_3_click(self, **event_args):
    user = anvil.users.login_with_form()
    if user:
      print(user)
      self.LogIn.visible = False


