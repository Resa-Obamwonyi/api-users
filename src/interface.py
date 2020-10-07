import requests


class RegresApi:
    @staticmethod
    def users(id):
        url = 'https://reqres.in/api/users/'
        id = str(id)
        user = requests.get(url+id)
        user_data = user.json()
        return user_data


