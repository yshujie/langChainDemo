from src.case.chains import (
    namer,
    anamer
)

def testNamer():
    print(namer.giveNameForProduct2()) 

def testANamer():
    anamer.generate_serially()
    
if __name__ == "__main__":
    testANamer()