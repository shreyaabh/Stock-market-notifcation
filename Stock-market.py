import bs4
import requests
from bs4 import BeautifulSoup
from twilio.rest import Client 
import time

account_sid = "Your twilio sid" #Enter your twilio sid
auth_token = "Your twilio token" #Enter your twilio token
client = Client(account_sid, auth_token)


def getData(url):
        r=requests.get(url)
        return r.content

def send_email():
    sms = client.messages.create(
    from_="Your twilio number", #Enter your twilio number
    body=f"Share value has reached to the desired amount. You can now trade!",
    to="Your number", #Enter your cell number connected to twilio
    )
    print(sms.sid)

def run_app():
    table_name_data = []
    for td in soup.find_all('td'):
        td_text = td.text
        table_name_data.append(td_text)  
    #print(table_name_data[::10])

    table_value_data = []
    for td in soup.find_all('td'):
        td_text = td.text
        table_value_data.append(td_text)  
    # print(table_value_data[4::10])

    ## ADD DATA TO DICTINOARY ##
    zip_iterator = zip(table_name_data[::10],table_value_data[4::10])
    dicto= dict(zip_iterator)

    print(dicto)


    ## ACCESSING THE DATA ##
    user_input='Share name' #Enter the company name
    user_input=user_input.upper()
    if user_input in dicto:
        for key,value in dicto.items():
                if key == user_input:
                    print(f"The recent value of the company is : {value}")
                    value_get=value
    else:
        print("The company name is not there!")
     
    user_value='Highest share value' #Enter the amount you want it to reach
    if user_value==value_get:
        send_email(user_input)
    else:
        print(f"You will be notified when the value reaches {user_value}")


if __name__=="__main__":
        ## GETTING THE DATA ##
        myHtmlData = getData("Website name") #Enter the website you want to scrape
        soup=BeautifulSoup(myHtmlData,'html.parser')
        while True:
            run_app()
            print('\n')
            time_wait = 10
            print('\n')
            print(f"Wait {time_wait} seconds!")
            time.sleep(time_wait *1)
    
    
        

    




    
    