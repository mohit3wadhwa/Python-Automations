from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)


from_whatsapp_number = 'whatsapp:+3333'
#to_whatsapp_number   = 'whatsapp:+333'
to_whatsapp_number   = 'whatsapp:+1223455'
#to_whatsapp_number   = 'whatsapp:+3333'


client.messages.create(body='Hey There! I, Python',
					   from_=from_whatsapp_number,
					   to=to_whatsapp_number)

#print(message.sid)
