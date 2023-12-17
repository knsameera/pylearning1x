# API
# Request Lib
import requests


# Using main fun for runnig a program
def main():
    # get req=url

    responce_body =  requests.get("https://restful-booker.herokuapp.com/booking/1507")

    # print(responce_body.text)
    # print(responce_body.status_code)
    # print(responce_body.json())


if responce_body.status_code == 200:
    print("Tc#1- GET request is Successfull")
else:
    print("Tc#1- GET request is not Successfull")

if __name__ == "__main__":
    main()
