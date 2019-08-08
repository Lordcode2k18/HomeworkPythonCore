def enough(cap, on, wait):
    wait_passenger = cap - (on + wait)
    if wait_passenger == 0:
        return wait_passenger
    elif wait_passenger > 0:
        return 0
    else:    
        return wait_passenger*(-1)