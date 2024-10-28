from ._anvil_designer import PostFormTemplate
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from time import sleep


class PostForm(PostFormTemplate):
  def __init__(self, parameters, **properties):
    print(self.item)
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    uploadsPostRow = app_tables.uploads.get(postID=parameters['postID'])
    self.uploads = uploadsPostRow
    self.link_1.text = parameters['title']
    self.content.content = parameters['content']
    if parameters["media"]:
      self.image_1.source = parameters['media']
    self.Upvote.text = parameters['upvotes']
    self.Downvote.text = self.uploads["Downvotes"]
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
    if not anvil.users.get_user():
      alert("Please log in!")
    elif self.comment.text == "":
      alert("No comment given")
    else:
      print(f"Commenting {self.comment.text}")
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

  
  
  def Upvote_click(self, **event_args):
    self.users = [
      (user["email"], user) for user in app_tables.users.search()
    ]
    userID = anvil.server.call('getUUID',user['email'])
    existing_upvote = app_tables.upvote_data.get(postID_UV=postIDG,userID_UV=userID)
    existing_downvote = app_tables.downvote_data.get(postID_DV=postIDG,userID_DV=userID)

    if not anvil.users.get_user():
      alert("Must log in to upvote!")
    elif existing_downvote:
      print("Un-Downvoting")
      self.uploads['Downvotes'] = self.uploads['Downvotes'] - 1
      Downvotes = self.uploads['Downvotes']
      self.Downvote.text = Downvotes
      self.Downvote.background = ""
      self.Downvote.bold = False
      postID = postIDG
      DelRow = app_tables.downvote_data.get(postID_DV=postID,userID_DV=userID)
      DelRow.delete()

      #Upvoting:
      print("Upvoting...")
      self.uploads['Upvotes'] = self.uploads['Upvotes'] + 1
      Upvotes = self.uploads['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = "theme:Secondary Container"
      self.Upvote.bold = True
      postID = postIDG
      app_tables.upvote_data.add_row(postID_UV=postID,userID_UV=userID,upvotes_UV=Upvotes)
    elif existing_upvote:
      print("Un-Upvoting")
      self.uploads['Upvotes'] = self.uploads['Upvotes'] - 1
      Upvotes = self.uploads['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = ""
      self.Upvote.bold = False
      postID = postIDG
      DelRow = app_tables.upvote_data.get(postID_UV=postID,userID_UV=userID)
      DelRow.delete()

    else:
      print("Upvoting...")
      self.uploads['Upvotes'] = self.uploads['Upvotes'] + 1
      Upvotes = self.uploads['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = "theme:Secondary Container"
      self.Upvote.bold = True
      postID = postIDG
      app_tables.upvote_data.add_row(postID_UV=postID,userID_UV=userID,upvotes_UV = Upvotes)

  def Downvote_click(self, **event_args):
    self.users = [
      (user["email"], user) for user in app_tables.users.search()
    ]
    userID = anvil.server.call('getUUID',user['email'])
    existing_upvote = app_tables.upvote_data.get(postID_UV=postIDG,userID_UV=userID)
    existing_downvote = app_tables.downvote_data.get(postID_DV=postIDG,userID_DV=userID)

    if not anvil.users.get_user():
      alert("Must log in to downvote!")
    elif existing_upvote:
      print("Un-Upvoting")
      self.uploads['Upvotes'] = self.uploads['Upvotes'] - 1
      Upvotes = self.uploads['Upvotes']
      self.Upvote.text = Upvotes
      self.Upvote.background = ""
      self.Upvote.bold = False
      postID = postIDG
      DelRow = app_tables.upvote_data.get(postID_UV=postID,userID_UV=userID)
      DelRow.delete()

      #Downvoting:
      print("Downvoting...")
      self.uploads['Downvotes'] = self.uploads['Downvotes'] + 1
      Downvotes = self.uploads['Downvotes']
      self.Downvote.text = Downvotes
      self.Downvote.background = "theme:Secondary Container"
      self.Downvote.bold = True
      postID = postIDG
      app_tables.downvote_data.add_row(postID_DV=postID,userID_DV=userID,downvotes_DV=Downvotes)

    elif existing_downvote:
      print("Un-Downvoting")
      self.uploads['Downvotes'] = self.uploads['Downvotes'] - 1
      Downvotes = self.uploads['Downvotes']
      self.Downvote.text = Downvotes
      self.Downvote.background = ""
      self.Downvote.bold = False
      postID = postIDG
      DelRow = app_tables.downvote_data.get(postID_DV=postID,userID_DV=userID)
      DelRow.delete()

    else:
      print("Downvoting...")
      self.uploads['Downvotes'] = self.uploads['Downvotes'] + 1
      Downvotes = self.uploads['Downvotes']
      self.Downvote.text = Downvotes
      self.Downvote.background = "theme:Secondary Container"
      self.Downvote.bold = True
      postID = postIDG
      app_tables.downvote_data.add_row(postID_DV=postID,userID_DV=userID,downvotes_DV=Downvotes)

  def comment_change(self, **event_args):
    print()    




    
    
