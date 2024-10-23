import requests 






import requests
import sys


#  G 500 P 300
def create():
    url = 'http://127.0.0.1:8000/api/truck/create'   
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NTQ0NDYyLCJpYXQiOjE3Mjk1NDA4NjIsImp0aSI6IjkzYTI2ZDIzMGNmYTQ0NzFhYTI3ZGYzOGY5NTgzMzViIiwidXNlcm5hbWUiOiJnaWdpIn0.cTZTJKV-ep6b9_79837YS67pVSleX3l27xYrxtnZ1k8'}

    data = {"truck_brand":'Scania',
            'truck_model':'G 500',
            'color':'green',
            'fuel_type':'Diesel'}


    save = requests.post(url=url,data=data, headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)


def get_trucks():


    url = 'http://127.0.0.1:8000/api/truck/list'    
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NTQ0NDYyLCJpYXQiOjE3Mjk1NDA4NjIsImp0aSI6IjkzYTI2ZDIzMGNmYTQ0NzFhYTI3ZGYzOGY5NTgzMzViIiwidXNlcm5hbWUiOiJnaWdpIn0.cTZTJKV-ep6b9_79837YS67pVSleX3l27xYrxtnZ1k8'}

 

    save = requests.get(url=url, headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)

if __name__ == '__main__':

    if sys.argv[1] == 'post':
        create()
    elif sys.argv[1] == 'get':
        get_trucks()
    else:
        exit()

