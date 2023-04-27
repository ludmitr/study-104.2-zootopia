import requests

API_KEY = "XFRC5aD4/q1QCnKHZJiFRA==zknfRp8r7bXdBEPh"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {
        ...
      },
      'locations': [
        ...
      ],
      'characteristics': {
        ...
      }
    },
    """
    url = f"https://api.api-ninjas.com/v1/animals?name={animal_name}"
    res = requests.get(url, headers={"X-Api-Key": API_KEY})

    return res.json()
