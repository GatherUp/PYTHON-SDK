from gatherup.sdk import Client
from gatherup.sdk import Credentials

client = Client(Credentials("CLIENT_ID", "BEARER"))
response = client.request("/businesses/get", {})
if response.is_success():
  if response.has("data"):
    print(response.get("data"))
  else:
    print(response.get_raw_data())
else:
  print("Error: " + response.get_message())
