def simple_interest(p,t,r):
    print("amount is",p)
    print("time is",t)
    print("rate is",r)

    si=(p * t * r)/100

    print("simple interest is",si)
    return si

simple_interest(30000, 6, 2)