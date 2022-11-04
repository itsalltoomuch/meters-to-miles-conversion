### This is a sample of using Python write a function to convert meters to miles.

## Briefly introduction: 
Reference: https://www.calculatorful.com/meters-to-miles 

In the SI unit system, the meter is the basic unit of length. The meter is defined as the distance traveled by light in a vacuum in exactly 1/299792458 seconds.

The mile is a British imperial measure and a customary unit of distance in the United States. Both are based on the older English unit of length equal to 5,280 English feet, or 1,760 yards

The quart is an English unit of volume which equals a quarter gallon. 

### How many miles are in a meter? 

There are 0.000621 miles in a meter. 
So, whenever you need to convert meters to miles, multiply your meter figure by 0.000621 to get your miles figure. For example, to convert [5000 meters to miles](https://www.calculatorful.com/meters-to-miles) we have:

```
5000 * 0.000621 = 3.105 (mi)
```

## A simple Python program to generate a converstion table
```
# FROM METERS MILES
print("meters              miles")
meters = 1000
for i in range(1, 10):
    print(meters, format(meters * 0.000621, ">20.3f"))
    meters += 1000
```
- The print() function prints the specified message to the screen, or other standard output device. The message can be a string, or any other object, the object will be converted into a string before written to the screen.

- A for loop is used for iterating over a sequence. In this example, it iterates over a list of number from 1 to 10.

The result of above function is as follow:
| Meters            | Miles           |
| ------------------ | ------------------------------------------------------------ |
|1000|0.621|
|2000|1.242|
|3000|1.863|
|4000|2.484|
|5000|3.105|
|6000|3.726|
|7000|4.347|
|8000|4.968|
|9000|5.589|