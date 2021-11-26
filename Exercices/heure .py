from datetime import *
now = datetime.now()
current_hour = now.hour
current_minute = now.minute

current_time_base = current_hour*60+current_minute

if current_time_base<630:
    next_pause_hour=10
    next_pause_min=30
    next_pause_base=630
elif current_time_base<750:
    next_pause_hour=12
    next_pause_min=30
    next_pause_base=750
elif current_time_base<930:
    next_pause_hour=15
    next_pause_min=30
    next_pause_base=930
elif current_time_base<990 and datetime.today().weekday() == 4:
    next_pause_hour=17
    next_pause_min=0
    next_pause_base=990
elif datetime.today().weekday() != 4 and current_time_base<1020:
    next_pause_hour=0
    next_pause_min=0
    next_pause_base=1020
elif current_time_base>1020:
    print("la journée est finie FDP")
    next_pause_hour=0
    next_pause_min=0
    next_pause_base=1020

waiting = next_pause_base-current_time_base
waiting_hours = waiting//60
waiting_minutes = waiting%60

print(f'La prochaine pause est à {next_pause_hour}H{next_pause_min}, il reste {waiting_hours}H{waiting_minutes} à attendre')