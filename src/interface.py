import json

import requests


class RegresApi:
    @staticmethod
    def users(id):
        url = 'https://reqres.in/api/users/'
        id = str(id)
        user = requests.get(url+id)
        user_data = user.json()

        # json.dumps() to beautify the json data
        return json.dumps(user_data, indent=4)



