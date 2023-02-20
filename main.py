import requests


def weather_by_location(location: str):
    url = f"https://wttr.in/{location}?1nTqMF"
    headers = {"Accept-Language": "ru"}
    return requests.get(url, headers=headers).text


def main():
    print(weather_by_location("svo"))
    print(weather_by_location("Череповец"))
    print(weather_by_location("London"))


if __name__ == "__main__":
    main()
