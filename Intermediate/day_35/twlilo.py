# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = "ACd06fb7ca26f0747854632a9545ed1ab5"
auth_token = "ef067d6d51f4c3ee00864fcb880b28e4"


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

client = Client(account_sid, auth_token)

message = client.messages.create(body="Iam eamin, HI", from_='+15752686391', to='+880 1749-319102')

print(message.status)
