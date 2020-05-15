from mesibo import Mesibo
from mesibo import MesiboNotify

#Mesibo invokes various Listeners for various events.
#For example, when you receive a message, receive an incoming call etc
#MesiboNotify is a class of listeners that can be invoked to get real-time notification of events



class MesiboListener(MesiboNotify):

    def __init__(self):
        pass

    def on_connectionstatus(self, status):
        print("===>on_connectionstatus: " + str(status))
        return 1


    def on_message(self, message_params,data):
        #invoked on receiving a new message or reading database messages
        print("===>on_message: from " + str(message_params['peer']))
        print(data)
        return 1

    def on_messagestatus(self, message_params):
        #Invoked when the status of outgoing or sent message is changed
        print("===>on_messagestatus: from " + str(message_params['peer'])+
        " status "+ str(message_params['status']))
        return 1


def send_text_message(to,message):
        #api is the Mesibo Python API instance.
        #Make sure the instance is initialised before you call API functions
        p = {}
        p['peer'] = to
        p['expiry'] = 3600
        data = message
        api.send_message(p,api.random(),data)



#Initialisation code
#Get auth token and app id from console
AUTH_TOKEN = "9cc354dd4b3fcf073d8b6bde3ad7f11b9b0be0ca3e04a0f401e771305a4"
APP_ID = "7811"
#Create a Mesibo Instance
pymesibo = Mesibo()

#Set Listener
pymesibo.set_listener(MesiboListener)

#Set your AUTH_TOKEN obtained from the Mesibo Console
pymesibo.set_accesstoken(AUTH_TOKEN)

#Set APP_ID which you used to create AUTH_TOKEN
pymesibo.set_appname(APP_ID)

#Set the name of the database
pymesibo.set_database("mesibo.db")

#Start mesibo
pymesibo.start()
