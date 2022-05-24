import hashlib
print(hashlib.sha512('test1234'.encode("utf-8")).hexdigest())

a = 0


def method1(args):
    print(args)


def method2():
    if a == 0:
        method1("hoge" + "fuga")
