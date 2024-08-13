base_fare = 5.00
fare_per_stop = 2.50

start_stop = int(input("What number stop are you at? "))
end_stop = int(input("What is the stop you want to go to? "))
number_of_stops = abs(end_stop - start_stop)

total_fare = base_fare + (fare_per_stop * number_of_stops)
print(f"The fare is ${total_fare}")