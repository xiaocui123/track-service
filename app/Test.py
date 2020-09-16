def multyResponse():
    a = list()
    print(type(a))
    a.append("test1")
    a.append("test2")
    return a

if __name__ == '__main__':
    a,b = multyResponse()
    print(a,b)
