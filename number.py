# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "ACe8b501826924f05ef2aa5f54db6e6717"
auth_token = "5f959916c230f62f48deb1feaa8cee08"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+525552881612",
                                             from_="+15163237821",
                                             body="Hola")
