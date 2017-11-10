from twilio.rest import Client

account_sid="AC23b33b4d9e71e57e950b09aae8325151"

auth_token="0e760b36492fa7e7cc77896f9fd0fd3c"
client=Client(account_sid, auth_token)

message=client.messages.create(
    to="+19726706437", 
    from_="+19724585557",
    body="Hey Jude, what about showing off your sms sender app!!!")

print (message.sid)    
                                   
