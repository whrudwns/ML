def AND_GATE(x1,x2):
    w1 = 0.5
    w2 = 0.5
    b = -1
    output = w1*x1 + w2*x2 +b
    if output < 0:
        print(0)
        return 0
    else:
        print(1)
        return 1


#AND_GATE(0,1)
