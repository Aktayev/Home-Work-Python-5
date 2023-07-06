import re

def main():
   hours = input("Hours: ")
   if hours := re.search(r"^(\d+\:?[0-5]?[0-9]? [A-Z]+) to (\d+\:?[0-5]?[0-9]? [A-Z]+)$", hours):
      first_time = convert(hours.group(1))
      last_time = convert(hours.group(2))
      print(f"{first_time} to {last_time}")
   else:
      print("ValueError")

def convert(time):
   if 'PM' in time:
      convert = re.search(r"^(\d+)(\:\d+)?(?: [A-Z]+)", time)
      con = int(convert.group(1)) + 12
      full_con = convert.group(2)
      if full_con == None:
         return(f"{con}:00")
      return(f"{con}{full_con}")
   if 'AM' in time:
      convert = re.search(r"^(\d+)(\:\d+)?(?: [A-Z]+)", time)
      con = convert.group(1)
      full_con = convert.group(2)
      if full_con == None:
         return(f"{con}:00")
      return(f"{con}{full_con}")
   else:
      print("ValueError")


if __name__ == "__main__":
    main()
# print(f"{time.group(1)} to {time.group(2)}")

# hours = input("hours:")
# if matches := re.search(r"^(\d+\:?[0-5]?[0-9]? [A-Z]+) to (\d+\:?[0-5]?[0-9]? [A-Z]+)$", hours):
#    first_time = matches.group(1)
#    last_time = matches.group(2)
#    if 'PM' in last_time:
#       convert = re.search(r"^(\d+)(\:\d+)( [A-Z]+)", last_time)
#       con = int(convert.group(1)) + 12
#       full_con = convert.group(2)
#       # return con, full_con
#    if 'PM' in first_time:
#       convert_f = re.search(r"^(\d+)(\:\d+)( [A-Z]+)", first_time)
#       con_f = int(convert_f.group(1)) + 12
#       full_con_f = convert_f.group(2)
#       # return con, full_con
#    print(f"{con}{full_con} to {con_f}{full_con_f}")



