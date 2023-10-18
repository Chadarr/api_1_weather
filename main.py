import requests


def weather_by_location(location: str):
    url = f"https://wttr.in/{location}"
    payload = {"1": "", "n": "", "T": "", "q": "", "M": "", "F": ""}
    headers = {"Accept-Language": "ru"}
    return requests.get(url, headers=headers, params=payload).text


def main():
    print(weather_by_location("svo"))
    print(weather_by_location("Череповец"))
    print(weather_by_location("London"))


if __name__ == "__main__":
    main()
