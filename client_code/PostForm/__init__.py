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
    self.init_components(**properties)
    self.link_1.text = parameters['title']
    self.content.content = parameters['content']
    self.image_1.source = parameters['media']
    for i,v in parameters.items():
      print(i)
      print(v)
   

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    open_form("Form1")
