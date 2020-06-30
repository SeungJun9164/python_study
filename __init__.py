# animal 패키지가 어떤 모듈들의 합인지 __init__.py 파일에서 선언

from .cat import Cat # . <= 이폴더에 있는 cat.py 이라는 파일에서 Cat이라는 클래스를 가지고 와라
from .dog import Dog