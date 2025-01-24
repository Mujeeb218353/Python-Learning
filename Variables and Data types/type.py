myName="Mujeeb Ur Rahman"
print(type(myName))

floatNumber=10.5
print(type(floatNumber))

isStudent=True
print(type(isStudent))

age=None
print(type(age))

complexNumber=2+3j
print(type(complexNumber))

integerNumber=20
print(type(integerNumber))

bigInteger=1234567890123456789012345678901234567890
print(type(bigInteger))

listOfNumbers=[1,2,3,4,5]
print(type(listOfNumbers))

tupleOfNumbers=(1,2,3,4,5)
print(type(tupleOfNumbers))

setOfNumbers={1,2,3,4,5}
print(type(setOfNumbers))

dictOfNumbers={"one":1, "two":2, "three":3}
print(type(dictOfNumbers))

frozensetOfNumbers=frozenset([1,2,3,4,5])
print(type(frozensetOfNumbers))

byteData=b"Hello"
print(type(byteData))

byteArrayData=bytearray([65,66,67,68,69])
print(type(byteArrayData))

memoryViewData=memoryview(b"Hello")
print(type(memoryViewData))

rangeOfNumbers=range(1,10)
print(type(rangeOfNumbers))

print(float(integerNumber))  # Convert integer to float
print(int(floatNumber))      # Convert float to integer