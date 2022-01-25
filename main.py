from urllib.request import urlopen


def get_temperature(city):
  url = "http://wttr.in/" + city + "?format=%t"
  page = urlopen(url)
  raw = page.read()
  temp = raw.decode("utf-8")
  return temp

city = input("State: ")
temp = get_temperature(city)
print(temp)