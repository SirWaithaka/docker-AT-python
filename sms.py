from flask import Flask
from AfricasTalkingGateway import AfricasTalkingGateway as ATG
from AfricasTalkingGateway import AfricasTalkingGatewayException as ATGException

app = Flask(__name__)

@app.route("/sms")
def index():

   username = "craftsmon"
   apikey = "38c3ad92fc1c5e84bacf19721a53e380fdc585420051728edc41721926fa700d"

   to = "+254713011722"
   message = "My test code for AT"

   gateway = ATG(username, apikey)

   try:
      results = gateway.smsMessage(to, message)

      for recipient in results:
         print(recipient)
   
   except: