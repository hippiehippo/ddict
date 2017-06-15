import requests # using requests library, recieves username and password. sends a post request and returns the response
def post(username, password):
    r = requests.post('http://127.0.0.1:8080/signin', data = {'username' : username, 'password': password})
    return r.text == 'good'

if __name__ == '__main__':
    print post('fish', 'sucks')
