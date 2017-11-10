from twilio.rest import Client

account_sid=""

auth_token=""
client=Client(account_sid, auth_token)

message=client.messages.create(
    to="+19726706437", 
    from_="+19724585557",
    body="Hey Jude, what about showing off your sms sender app!!!")

print (message.sid)    
                                   
