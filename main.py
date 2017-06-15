import requests

if __name__=='__main__':
    url='https://www.youtube.com/watch?v=12NPmrdoKKs'
    response=requests.get(url)

    print(response)
