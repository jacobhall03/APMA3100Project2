from rand import *
from statistics import *
from numpy import *
from matplotlib import pyplot
time_list = []
ticket_list = []

# Call loop
def run(iterator: int = 50):
    ticket = False
    time_sec = 0.0
    for calls in range(1,4):
        time_sec += 3
        x = sb_wait_time(iterator+calls*1000)
        # Waited less than 1.5 mins
        if x < 1.5:
            time_sec += (x * 60)
            # Connect to agent
            agent = rand(iterator+calls*2000) # Equal to rand func
            # print(agent)
            time_sec += 5
            if agent <= 0.2:
                time_sec += 72
                ticket = True
            elif agent <= 0.5 and agent > 0.2:
                time_sec += 96
                ticket = True
            elif agent <= 0.6 and agent > 0.5:
                time_sec += 81
                ticket = True
            elif agent > 0.6:
                time_sec += 114
                ticket = True
            break

        else:
            time_sec += 90 # Didn't reach switchboard
            time_sec += 2 # Hangup
    

    #No Call exit condition
    return (time_sec, ticket)

for i in range(1,501):
    tup = run(i)
    (times, tickets) = tup
    time_list.append(times)
    ticket_list.append(ticket_list)

print("Original list:\n", time_list)
#Values of W in numerical order
time_list.sort()
print("Sorted list:\n", time_list)

f = open("500w_values.txt", "w")
f.write(str(time_list))

cnt = 0
for i in range(0,len(time_list)):
    if time_list[i] >= 381.0:
        cnt += 1

print(cnt)

#Mean Value
print("Mean: ", mean(time_list))
#Median Value
print("Median: ", median(time_list))
#First Quartile
print("1st Quartile: ", quantile(time_list, 0.25))
#Third Quartile
print("3rd Quartile: ", quantile(time_list, .75))

cdf = []
for i in range(1, 501):
    cdf.append(i / 500)


pyplot.plot(time_list, cdf)
pyplot.grid(which='major', visible=True)
pyplot.grid(which='minor', visible=True)
pyplot.minorticks_on()
pyplot.xlabel("Time to Ticket/No Ticket (sec)")
pyplot.ylabel("Cumulative Probability")
pyplot.title("CDF of Time to Ticket")
pyplot.show()

# print(run(.5, 20))
# print(run(.5, 100))
# print(run(.5, 1))
# print(run(.5, 99))
# print(run(.5, 78))
# print(run(1.5, 78))
