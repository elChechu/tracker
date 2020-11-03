from bs4 import BeautifulSoup
import requests
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# moodle params
uri = "https://estudy.salle.url.edu/"
login = "login/index.php"
tracker = "mod/attendance/view.php?id=554161&view=4"
tracker_form = "mod/attendance/attendance.php"


def get_public_ip():
    # 84.88.224.0 - 84.88.243.255
    req = requests.get('https://ifconfig.me')
    if req.status_code == 200:
        ip = str(req.text).split(".")
        if int(ip[0]) == 84 and int(ip[1]) == 88 and int(ip[2]) >= 224 and int(ip[2]) <= 243:
            return True
        else:
            return False
    else:
        return None


def get_credentials():
    f = open('credenciales.txt')
    return f.readlines()
    

def track_assistance(location, username, password):
    
    req = requests.get(uri)

    if req.status_code == 200:
        s = requests.Session()
        payload = {'user': username, 'password': password, 'username': username}
        response = s.post(uri + login, data=(payload), verify=False)

        if response.status_code == 200:
            r = s.get(uri + tracker)
            soup = BeautifulSoup(r.text, 'lxml')
            tbody = soup.findAll('tbody')[1]
            td = tbody.findAll('td')
            a = td[len(td)-1].find('a', href=True)
            req = s.get(str(a['href']), verify=False)
            
            if req.status_code == 200:
                soup = BeautifulSoup(req.text, 'lxml')                 
                form = soup.find('form', {'action':'https://estudy.salle.url.edu/mod/attendance/attendance.php'})
                inputs = form.findAll('input')
                payload = {}

                for i in inputs:
                    payload[i['name']] = i['value']
                
                if location != False:
                    payload['status'] = '5118'
                else:
                    payload['status'] = '5117'

                del payload['submitbutton']
                del payload['cancel']

                print(payload)       
                res_form = s.post(uri + tracker_form, data=(payload))


def check_credentials(username, password):
    s = requests.Session()
    payload = {'user': username, 'password': password, 'username': username}
    response = s.post(uri + login, data=(payload), verify=False)

    if response.status_code == 200:
        r = s.get(uri + tracker)
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            tbody = soup.findAll('tbody')[1]
            td = tbody.findAll('td')
            return True
        except:
            return False
    else:
        return None

        



if __name__ == "__main__":

    data = get_credentials()
    username = data[0].replace("\n", "")
    password = data[1].replace("\n", "")
    check = check_credentials(username, password)

    if check != None:
        if check:
            if get_public_ip() != None:
                track_assistance(get_public_ip(), username, password)
            else:
                print("Check your internet connection")
        else: 
            print("Usuario o contraaseña incorrectos, modifica el archivo credenciales.txt")
    else:
        print("Check your internet connection")



