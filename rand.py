def rand(iteration: int = 50) -> float: 
    starting_value = 1_000
    multiplier = 24_693
    increment = 3517
    modulus = 2E17

    x = starting_value
    u = 0.0
    for i in range(0, iteration):
        x = (multiplier * x + increment) % modulus
        u = x / modulus
    
    return u