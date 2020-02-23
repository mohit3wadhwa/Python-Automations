from twilio.rest import Client

account_sid = 'ACe0a2a0601e8336dfbcdc210907a5b850'
auth_token = 'd818d73a956de8d7bec9928b74f33f1d'
client = Client(account_sid, auth_token)


from_whatsapp_number = 'whatsapp:+14155238886'
#to_whatsapp_number   = 'whatsapp:+16023941428'
to_whatsapp_number   = 'whatsapp:+16026537892'
#to_whatsapp_number   = 'whatsapp:+9197113111000'


client.messages.create(body='Hey There! I, Python',
					   from_=from_whatsapp_number,
					   to=to_whatsapp_number)

#print(message.sid)
