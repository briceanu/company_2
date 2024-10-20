
import requests
import sys


#  G 500 P 300
def sign_up():
    url = 'http://127.0.0.1:8000/api/driver/sign_up'   
    data = {"username":'marian',
            'password':'alwdi2LLL23',
            'confirm_password':'alwdi2LLL23',
            'email':'marian@gmail.com',
        }

    # users
    # costica ion12oLo
    # costica new password ==> ion12AA
    # gigi ak471989  is a superuser
    #  marian alwdi2LLL23

    save = requests.post(url=url,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)


def get_drivers():
    url = 'http://127.0.0.1:8000/api/driver/list'    
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NDQwMzExLCJpYXQiOjE3Mjk0MzY3MTEsImp0aSI6ImE4MjM2NTRiYzRiNTQ3NTg4YTI4OGJiM2IwYWZjM2I4IiwidXNlcm5hbWUiOiJnaWdpIn0.jKujV4BruDdUFtDTsJ6rVa8LGMN-TH62B-ViQzEC11Q'}

    save = requests.get(url=url,headers=headers)
    print(save.status_code)
    print(save.url)
    print(save.text)


def sign_in():
    url = 'http://127.0.0.1:8000/api/driver/sign_in'     

    data = {'username':'costica','password':'ion12oLo'}

    res = requests.post(url=url,data=data)
    print(res.status_code)
    print(res.url)
    print(res.text)


def remove_driver():
    url = 'http://127.0.0.1:8000/api/driver/remove_driver'    
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NDI5MTQ0LCJpYXQiOjE3Mjk0Mjg4NDQsImp0aSI6IjNiNzhmMzIwZWY5NjQxZTdhMzRhZjE4NzRkNjYzYTkyIiwidXNlcm5hbWUiOiJnaWdpIn0.-scYA5Z9DPOvE_J-gb29P6YgpiRfXCa4VYzRP1_ZHrY'}
    data = {'username':'gina'}
    save = requests.delete(url=url,headers=headers,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)



def get_new_access_token():
    url = 'http://127.0.0.1:8000/api/driver/new_access_token'    
    data = {'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTUxNjE2NiwiaWF0IjoxNzI5NDI5NzY2LCJqdGkiOiI3MDFlNjNmYmNiMzI0MzMyOGQ4ZGIwOTU1MDZhYzI3YyIsInVzZXJuYW1lIjoiY29zdGljYSJ9.GArwtK07MDdecKjOpfG-Co9_OTkPvUbesH2fKYO7zgU'}

    save = requests.post(url=url,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)

def sign_out():
    data = {'refresh':'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyOTUxNjE2NiwiaWF0IjoxNzI5NDI5NzY2LCJqdGkiOiI3MDFlNjNmYmNiMzI0MzMyOGQ4ZGIwOTU1MDZhYzI3YyIsInVzZXJuYW1lIjoiY29zdGljYSJ9.GArwtK07MDdecKjOpfG-Co9_OTkPvUbesH2fKYO7zgU'}

    url = 'http://127.0.0.1:8000/api/driver/sign_out'    

    save = requests.post(url=url,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)

def update_password():
    url = 'http://127.0.0.1:8000/api/driver/update_password'    
    headers = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5NDQwNjAzLCJpYXQiOjE3Mjk0MzcwMDMsImp0aSI6ImZkMmZlNjI1ZmM2ZTRiZDZhNWFhZjQ5MzA1OTcwM2U0IiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.Vrc9j7hr1ckSH9XvT5aKKOCohIgHxFT1oz02jlnUe00'}
    data = {'password':'ion12oLo2','confirm_password':'ion12oLo2'}
    save = requests.patch(url=url,headers=headers,data=data)
    print(save.status_code)
    print(save.url)
    print(save.text)






if __name__ == '__main__':

    if sys.argv[1] == 'sign_up':
        sign_up()
    elif sys.argv[1] == 'get_drivers':
        get_drivers()
    elif sys.argv[1] == 'sign_in':
        sign_in()
    elif sys.argv[1] == 'remove':
        remove_driver()
    elif sys.argv[1] == 'new_access':
        get_new_access_token()
    elif sys.argv[1] == 'sign_out':
        sign_out()
    elif sys.argv[1] == 'update_password':
        update_password()
    

    else:
        exit()

