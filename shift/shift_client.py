
import requests
import sys


#  G 500 P 300

    # users
    # costica ion12oLo
    # costica new password ==> ion12AA
    # gigi ak471989  is a superuser
    #  marian alwdi2LLL23

 

def save_shift():
    url = 'http://127.0.0.1:8000/api/shift/shift'    
    # this is marian token
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NTUzMzg5LCJpYXQiOjE3Mjk1NDk3ODksImp0aSI6IjcyZTVkODI1ZGYxZTQ4MjViMzQ0MzA1ZTBmZDc0MDFmIiwidXNlcm5hbWUiOiJtYXJpYW4ifQ.-7w-YQakLePNr3gyKulEbCpbpua9DsNwE5HA0UIa-cI'}
    data = {'truck_used':1,
            'driver_id':'ac43692d-b9c4-474c-9aad-73b8e41df0f6',
            'hours_worked':9.10,
            'payment_per_hour':18.3,
            'weight_carried':31,
            'distance_driven':170
            }
            
    save = requests.post(url=url,headers=headers,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)


def get_shifts():
    url = 'http://127.0.0.1:8000/api/shift/shift'    
    headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NjkzMjQzLCJpYXQiOjE3Mjk2ODk2NDMsImp0aSI6IjE0YzE3ZmVkY2NmMTRlZjA5YzNmZWJmY2QzMDJkMzI4IiwidXNlcm5hbWUiOiJtYXJpYW4ifQ.WthPIjPmmx6SP-RONnEZg1JAD6PWqblUKXuAPWCJSOc'}
 
    save = requests.get(url=url, headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)



def list_hours():
    url = 'http://127.0.0.1:8000/api/shift/list_total_hours'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)




def hard_working():
    url = 'http://127.0.0.1:8000/api/shift/hard_working'    
    data = {'hours':15,
            'distance':200,
            }
            
    save = requests.get(url=url,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)



def weight_distance():
    url = 'http://127.0.0.1:8000/api/shift/weight'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)

def total_payment():
    url = 'http://127.0.0.1:8000/api/shift/total_payment'    
    data= {"payment_per_hour":f'{sys.argv[2]}'}
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NzA2MDU1LCJpYXQiOjE3Mjk3MDI0NTUsImp0aSI6ImI2NWVlYWM1NGYyNjQ2NDJiZTMzODc1NzE5YWFhNjQ5IiwidXNlcm5hbWUiOiJnaWdpIn0.2-1TnWbrQ8fM-Bvx4KGi5OICW39s8vamT7ruVVBRiuA'}


    save = requests.get(url=url,data=data,headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)




if __name__ == '__main__':

    if sys.argv[1] == 'save_shift':
        save_shift()
    if sys.argv[1] == 'get_shifts':
        get_shifts() 
    if sys.argv[1] == 'list_hours':
        list_hours() 
    if sys.argv[1] == 'hard_working':
        hard_working() 
    if sys.argv[1] == 'total_payment':
        total_payment()
    if sys.argv[1] == 'weight_distance':
        weight_distance()
    else:
        exit()

