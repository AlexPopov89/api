import requests


class TestNewPlace:

    def test_create_new_place(self):

        json_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"

        }




        result = requests.post("https://rahulshettyacademy.com/maps/api/place/add/json?key=qaclick123",
                               json=json_for_create_new_place,
                               headers={'Content-Type': 'application/json'})
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success CREATE NEW LOCATION!')
        else:
            print('Error CREATE NEW LOCATION!!!')
        response_json = result.json()
        print(f"Результат метода ПОСТ{response_json=}")

        url = "https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123&place_id=" + response_json["place_id"]
        print(url)
        result = requests.get(url,
            headers={'Content-Type': 'application/json'})
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success GET NEW LOCATION!')
        else:
            print('Error GET NEW LOCATION!!!')
        # result.encoding = 'utf-8'
        # response_json = result.json()
        print(result.text)

        result = requests.delete("https://rahulshettyacademy.com/maps/api/place/delete/json?key=qaclick123&place_id=" + response_json["place_id"],
                               # json=json_for_delete_new_place,
                               headers={'Content-Type': 'application/json'})
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success DELETE NEW LOCATION!')
        else:
            print('Error DELETE NEW LOCATION!!!')

        print(result.text)

        result = requests.get(
            "https://rahulshettyacademy.com/maps/api/place/get/json?key=qaclick123&place_id=" + response_json["place_id"],
            headers={'Content-Type': 'application/json'})
        assert 200 == result.status_code
        if result.status_code == 200:
            print('Success GET NEW LOCATION!')
        else:
            print('Error GET NEW LOCATION!!!')


