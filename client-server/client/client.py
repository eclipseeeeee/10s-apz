import urllib.request
import json

class Client:
    def get_messages(self):
        url = 'http://localhost:8080/api/messages'
        response = urllib.request.urlopen(url)
        if response.status == 200:
            return json.loads(response.read().decode())
        else:
            return None

    def post_message(self, message):
        url = 'http://localhost:8080/api/messages'
        data = {'message': message}
        data = json.dumps(data).encode()
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        response = urllib.request.urlopen(req)
        if response.status == 200:
            return 'Message sent'
        else:
            return None
