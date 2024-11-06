from ._anvil_designer import CreateChatTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class CreateChat(CreateChatTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.code_chat.text = anvil.server.call('getChatID')
    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    nameChat = self.chat_name.text
    max = self.max.text
    save = self.save.checked
    username = self.username_a.text
    id = self.code_chat.text
    user = anvil.users.get_user()

    if max.isdigit():
      max2 = int(max)
    Test = anvil.server.call('chatData',nameChat,max2,save,username,id,user)
    
    print(Test)
    
