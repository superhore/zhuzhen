from django.test import TestCase

# Create your tests here.

import requests,json


def foo():
    data = requests.post('http://127.0.0.1:8000/add/',data={'a':3,'b':4})

   # data = requests.post('http://127.0.0.1:8000/chat/',data={'msg':'您好,再见'})

    print(data.text)

foo()
