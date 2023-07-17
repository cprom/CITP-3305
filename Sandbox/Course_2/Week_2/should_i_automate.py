#!/usr/bin/env python3

def should_i_automate(time_to_automate, time_to_perform, amount_of_time_done):
    manual_task_cal = (time_to_perform * amount_of_time_done)
    if time_to_automate < manual_task_cal:
        print("Lets Automate this Sucka")
    else:
        print("Do it manualy")

should_i_automate(20, 10, 1)