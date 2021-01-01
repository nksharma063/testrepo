# Time to calculate hour and minute for complete
#running starts from breakfast time
#whole number are hours and fraction part in minute
#seconds are ignored in calculations

time_to_leave = 6.52 #AM
time_to_leave_in_seconds = 6*60*60 + 52*60 #hour_to_seconds = hour * 3600, min_to_seconds = minute * 60

easy_pace_time_minutes = 8.15  #minutes adn seconds
easy_pace_time_in_seconds = 8*60 + 15 #inseconds
print(easy_pace_time_in_seconds)

tempo_pace_time_minutes = 7.12  #minutes and seconds
tempo_pace_time_in_seconds = 7*60 + 12
print(tempo_pace_time_in_seconds)



easy_pace_miles = float(input("Enter the no of miles on easy pace: "))
tempo_pace_miles = float(input("Enter the no of miles on tempo pace: "))

time_spent_on_running_seconds = (easy_pace_miles * easy_pace_time_in_seconds) + (tempo_pace_miles * tempo_pace_time_in_seconds) + time_to_leave_in_seconds
print(time_spent_on_running_seconds)



#final time calculation in hour , minute, seconds
time_spent_hours = time_spent_on_running_seconds//3600  # floor division for hours
t_s_h = int(time_spent_hours)
print(time_spent_hours)
time_spent_part_hour = time_spent_on_running_seconds%3600 #modulo division for remaning seconds
time_spent_part_minutes = time_spent_part_hour // 60 #floor division for minute
t_s_p_m = int(time_spent_part_minutes)
print(time_spent_part_minutes)
time_spent_part_seconds = time_spent_part_hour % 60 # modullo division for seconds
t_s_p_s = int(time_spent_part_seconds)
print(time_spent_part_seconds)
print("I get home for breakfast at: " + str(t_s_h) + ":" + str(t_s_p_m) + ":" + str(t_s_p_s) + "am")
