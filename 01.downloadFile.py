import requests
import traceback

"""
res= requests.get('https://google.com')
res.status_code
print(res)
"""


badRes= requests.get('https://www.gazeta.ru/auto/news/2018/10/27/n_12217255a.shtml')
#badRes.status_code
#print(badRes)
try:
    badRes.raise_for_status()
except Exception as e:
    print(e, "\n")
    print("This the full print of code exception: ")
    traceback.print_exc()


res= requests.get('https://google.com')
res.status_code
print("-----------------------------------------------")
print(res)



