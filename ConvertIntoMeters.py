# FROM METERS MILES
print("meters              miles")
meters = 1000
for i in range(1, 10):
    print(meters, format(meters * 0.000621, ">20.3f"))
    meters += 1000
