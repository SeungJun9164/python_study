# animal package
# dog, cat modules
# python folder를 하나 만드는데, 폴더의 이름이 패키지의 이름이다.
# 패키지는 module들의 합이다.

from animal import dog
from animal import cat

from animal import * # animal 패키지가 갖고 있는 모듈은 전부 다

from geopy.geocoders import Nominatim

d = dog.Dog()
d.hi()

c = cat.Cat()
c.hi()

d = Dog()
c = Cat()

d.hi()
c.hi()

geolocator = Nominatim(user_agent="seungjun")
location = geolocator.geocode("Seoul, South Korea")
print(location)