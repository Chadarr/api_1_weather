import requests


def weather_by_location(location: str):
    url = f"https://wttr.in/{location}"
    payload = {"n": "", "T": "", "q": "", "M": "", "F": "", "lang": "ru"}
    return requests.get(url, params=payload).text


def main():
    print(weather_by_location("svo"))
    print(weather_by_location("Череповец"))
    print(weather_by_location("London"))


if __name__ == "__main__":
    main()
