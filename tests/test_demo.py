import requests
import pytest


class TestFactApi:
    cat_url = "https://catfact.ninja/fact"
    dog_url = "https://dog-api.kinduff.com/api/facts"

    animals = [
        "cat",
        "dog"
    ]

    def get_funny_fact(type):
        def dog():
            response = requests.get(TestFactApi.dog_url)
            return response

        def cat():
            response = requests.get(TestFactApi.cat_url)
            return response

        if type == "dog":
            return dog
        else:
            return cat

    @pytest.mark.parametrize('whos_fact', animals)
    def test_check_fact(self, whos_fact):
        response = TestFactApi.get_funny_fact(whos_fact)()
        assert response.status_code == 200, "Wrong response code"
        try:
            print(response.json()["fact"] + "\n")
        except:
            print(response.json()["facts"][0] + "\n")
