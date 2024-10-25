
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
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODM4NzU2LCJpYXQiOjE3Mjk4MzUxNTYsImp0aSI6ImMyNmIyNDc1YWM4YTQ3NzI4NTg4ZTgwMmRmYzU4NjFkIiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.W_mz734-v3fkSWyJ_pl6xrGJJD059jD1XDT5nY1T1w8'}
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
    headers = {'Authorization':'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODQyOTM0LCJpYXQiOjE3Mjk4MzkzMzQsImp0aSI6IjUxNmQwM2JkMGQ2YTQ0NjI5NTMzNGU2YmMzMzNlMmUxIiwidXNlcm5hbWUiOiJtYXJpYW4ifQ.uGhRCYmKFp52EmoCH7hpdmo-wcmwQ3mY2m_3TJrdLCk'}
 
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


def total_hours():
    url = 'http://127.0.0.1:8000/api/shift/total_hours'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)



def payment():
    url = 'http://127.0.0.1:8000/api/shift/payment'    
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5ODQzNjc0LCJpYXQiOjE3Mjk4NDAwNzQsImp0aSI6IjM0ODM2NGZmOTk4ODRhZWRhZjg1ZWExYjFiNzBjNTc5IiwidXNlcm5hbWUiOiJtYXJpYW4ifQ.SJqod0AzbDw3CePMkcxwE7avGxm0vy3HgnM87Ne0idk'}


    save = requests.get(url=url,headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)



def longest_distance():
    url = 'http://127.0.0.1:8000/api/shift/longest'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)

def nr_drivers():
    url = 'http://127.0.0.1:8000/api/shift/nr_drivers'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)

def hours_worked():
    url = 'http://127.0.0.1:8000/api/shift/hours_worked'    

    save = requests.get(url=url)
    print(save.status_code)
    print(save.url)
    print(save.text)


def bonus():
    url = 'http://127.0.0.1:8000/api/shift/bonus'    

    save = requests.get(url=url)
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
    if sys.argv[1] == 'total_hours':
        total_hours()
    if sys.argv[1] == 'payment':
        payment()
    if sys.argv[1] == 'longest':
        longest_distance()
    if sys.argv[1] == 'nr_drivers':
        nr_drivers()
    if sys.argv[1] == 'hours':
        hours_worked()
    if sys.argv[1] == 'bonus':
        bonus()
    else:
        print('no function found')
        exit(0)

