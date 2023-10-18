import requests


def weather_by_location(location: str):
    url = f"https://wttr.in/{location}"
    payload = {"n": "", "T": "", "q": "", "M": "", "F": "", "lang": "ru"}
    return requests.get(url, params=payload).text


def main():
    locations = ["svo", "Череповец", "London"]
    for location in locations:
        print(weather_by_location(location))


if __name__ == "__main__":
    main()
