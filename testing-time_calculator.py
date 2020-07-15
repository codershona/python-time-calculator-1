def add_time(start, duration):
  first = start.split()
  second = duration. split() 

  n1= first[0].split(":")
  n1_hour = int(n1[0])
  n1_min = int(n1[1])

  n2= second[0].split(":")
  n2_hour = int(n2[0])
  n2_min = int(n2[1])

  days = 0
  
  if first[1] == "PM":
    n1_hour += 12

  minute_sum = n1_min + n2_min 
  hour_sum = n1_hour + n2_hour

  if minute_sum > 60:
    minute_sum -= 60
    hour_sum +=1
  
  if hour_sum > 24:
    days = hour_sum//24
    hour_sum = hour_sum - days*24

  if hour_sum <=12:
    meridieme = "AM"
  else: 
    meridieme = "PM"

  if hour_sum<10: 
    hour_sum = "0" + str(hour_sum)
  
  if minute_sum<10: 
    minute_sum = "0" + str(minute_sum)

  new_time = str(hour_sum) + ":" + str(minute_sum) + " " + meridieme 

  if days > 0:
    if days == 1:
      new_time += "(next day)"
    else:
      new_time += " (" + str(days) + " days later)"


  return new_time