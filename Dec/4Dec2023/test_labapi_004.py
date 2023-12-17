import requests


def main():
    id = "1711"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    responce_body = requests.get(full_url)
    assert responce_body.status_code == 200

    data = responce_body.json()

    # Assertions
    assert "first name" in data, "Incorrect First name"
    assert "last name" in data, "last name key present"

    assert data["first name"] == "Josh", "Incorrect first name"
    assert data["last name"] == "Allen", "incorrect last name"

if __name__ == "__main__":
     main()
