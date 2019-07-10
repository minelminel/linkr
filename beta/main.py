

from dispatch import Dispatcher

# target = "http://google.com"
# schema = Dispatcher(target).create_schema()
# print(schema)
import time
import requests
import timeout_decorator

@timeout_decorator.timeout(4, use_signals=False, timeout_exception=TimeoutError)
def foo(target):
    import requests
    try:
        r = requests.get(target)
    except:
        return None

print(foo("http://facebookdsafldsafsd.com"))


#
#
# def mytest():
#     print("Start")
#     for i in range(1,10):
#         time.sleep(1)
#         print("{} seconds have passed".format(i))
