# using assert keyword
import requests
def main():
    id = "1464"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    responce_body = requests.get(full_url)
    assert responce_body.status_code == 200

if __name__ == "__main__":
    main()
