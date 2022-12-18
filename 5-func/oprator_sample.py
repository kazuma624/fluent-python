from collections import namedtuple
from operator import attrgetter, itemgetter, methodcaller


metro_data = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74020386)),
    ('San Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

for city in sorted(metro_data, key=itemgetter(1)):
    print(city)
"""
('San Paulo', 'BR', 19.649, (-23.547778, -46.635833))
('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889))
('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
('Mexico City', 'MX', 20.142, (19.433333, -99.133333))
('New York-Newark', 'US', 20.104, (40.808611, -74020386))
"""

# 1 番目の要素と 0 番目の要素を取得するような関数を定義
cc_name = itemgetter(1, 0)
for city in metro_data:
    print(cc_name(city))
"""
('JP', 'Tokyo')
('IN', 'Delhi NCR')
('MX', 'Mexico City')
('US', 'New York-Newark')
('BR', 'San Paulo')
"""

# namedtuple として LatLong と Metropolis を定義する
LatLong = namedtuple('LatLong', 'lat long')
Metropolis = namedtuple('Metropolis', 'name cc pop coord')

# metro_data をそれぞれ上で定義した namedtuple に格納する
metro_areas = [
    Metropolis(name, cc, pop, LatLong(lat, long))
    for name, cc, pop, (lat, long) in metro_data
]

print(metro_areas[0])
"""
Metropolis(
    name='Tokyo', cc='JP', pop=36.933, coord=LatLong(lat=35.689722, long=139.691667)
)
"""

# name 属性と coord.lat 属性（ネストされてる）を取得するような関数を定義
name_lat = attrgetter('name', 'coord.lat')
for city in sorted(metro_areas, key=attrgetter('coord.lat')):
    print(name_lat(city))

"""
('San Paulo', -23.547778)
('Mexico City', 19.433333)
('Delhi NCR', 28.613889)
('Tokyo', 35.689722)
('New York-Newark', 40.808611)
"""

# メソッドを適用できる関数を def func(): ... を使わずに定義している
s = 'The time has come'
upcase = methodcaller('upper')
print(upcase(s)) # 'THE TIME HAS COME'

hiphonate = methodcaller('replace', ' ', '-')
print(hiphonate(s)) # 'The-time-has-come'
