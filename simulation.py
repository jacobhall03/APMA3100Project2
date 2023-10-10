from rand import rand
time_list = []
ticket_list = []

# Call loop
def run(x: float = .5, iterator: int = 50):
    calls = 0
    ticket = False
    time_sec = 0.0
    result = []
    for calls in range(0,3):
        time_sec += 3
        # x = 0 # Switchboard function
        # Waited less than 1.5 mins
        if x < 1.5:
            time_sec += (x * 60)
            # Connect to agent
            agent = rand(iterator) # Equal to rand func
            print(agent)
            time_sec += 5
            if agent <= 0.2 and agent >= 0.0:
                time_sec += 72
                ticket = True
            elif agent <= 0.5 and agent > 0.2:
                time_sec += 96
                ticket = True
            elif agent <= 0.6 and agent > 0.5:
                time_sec += 81
                ticket = True
            elif agent <= 1.0 and agent > 0.6:
                time_sec += 114
                ticket = True
            break

        else:
            time_sec += 90 # Didn't reach switchboard
            time_sec += 2 # Hangup
    

    #No Call exit condition
    result.append(time_sec)
    result.append(ticket)
    return result

print(run(.5, 20))
print(run(.5, 100))
print(run(.5, 1))
print(run(.5, 99))
print(run(.5, 78))
print(run(1.5, 78))
