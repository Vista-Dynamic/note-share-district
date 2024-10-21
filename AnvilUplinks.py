import anvil.server

anvil.server.connect("server_3FXNVHHTPAU5EQUBBITY55YP-A4CIUNX2HJN4U7UB")

@anvil.server.callable
def getActive():
    print("Active")


anvil.server.wait_forever()