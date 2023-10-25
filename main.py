import requests
import logging

logging.basicConfig(level=logging.DEBUG)


def weather_by_location(location: str):
    url = f"https://wttr.in/{location}"
    payload = {"nTqMF": "", "lang": "ru"}
    response = requests.get(url, params=payload)
    response.raise_for_status()
    if "error" in response.text:
        raise requests.exceptions.HTTPError(response.json["error"])
    return response.text


def main():
    locations = ["svo", "Череповец", "London"]
    for location in locations:
        print(weather_by_location(location))


if __name__ == "__main__":
    main()
