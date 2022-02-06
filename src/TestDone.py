class TestDone:

# ==========================================
# CONSTRUCTOR
# ==========================================

  def __init__(self):
    self.date           = ""
    self.time           = ""
    self.ping           = 0   #ms
    self.speed_download = 0.0 #Mbit/s
    self.speed_upload   = 0.0 #Mbit/s

# ==========================================
# OBJECT PRINT
# ==========================================
# This method prints the object (self) values

  def ObjectPrint(self):
      print("Date: "+str(self.date)+" Time: "+str(self.time)+" Ping: "+str(self.ping)+" Download Speed: "+str(self.speed_download)+" Upload Speed: "+str(self.speed_upload))