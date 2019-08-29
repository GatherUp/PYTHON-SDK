import requests # https://realpython.com/python-requests/
import json

class Credentials:

  def __init__(self, client_id, bearer):
    self.__client_id = client_id
    self.__bearer = bearer

  def get_client_id(self):
    return self.__client_id

  def get_bearer(self):
    return self.__bearer

class Response:

  def __init__(self, response):
    self.__data = json.loads(response)

  def get_raw_data(self):
    return self.__data

  def get_code(self):
    if "errorCode" in self.__data:
      return self.__data["errorCode"]
    return -1

  def is_success(self):
    return self.get_code() == 0

  def get_message(self):
    if "errorMessage" in self.__data:
      return self.__data["errorMessage"]
    return "Unknown"

  def has(self, key):
    return key in self.__data

  def get(self, key):
    if self.has(key):
      return self.__data[key]
    return None

class Client:

  def __init__(self, credentials, url = "https://app.gatherup.com/api", aggregate = 1):
    self.__credentials = credentials
    self.__url = url
    self.__aggregate = aggregate

  def request(self, endpoint, data):
    data["clientId"] = self.__credentials.get_client_id()

    if self.__aggregate > 0:
      data["aggregateResponse"] = 1

    response = requests.post(
      self.__url + endpoint,
      json=data,
      headers={"Authorization": "Bearer " + self.__credentials.get_bearer()
    })

    return Response(response.content)
