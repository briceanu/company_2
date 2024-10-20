import requests 






import requests
import sys


#  G 500 P 300
def create():
    url = 'http://127.0.0.1:8000/api/truck/create'   
    data = {"truck_brand":'Mercedes_Benz',
            'truck_model':'Axor',
            'color':'white',
            'fuel_type':'Diesel'}


    save = requests.post(url=url,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)


def get_trucks():


    url = 'http://127.0.0.1:8000/api/truck/list'    
 

    save = requests.get(url=url)
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

