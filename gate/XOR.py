import AND,OR , NAND
def XOR_GATE(x1,x2):
    AND.AND_GATE(NAND.NAND_GATE(x1,x2),OR.OR_GATE(x1,x2));



XOR_GATE(1,0)