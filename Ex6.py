def ordinalSuffix(number):
  number = str(number)
  # 11 - 20 range
  i = int(number)
  if 11 <= i <= 20:
    return number + "th"


  
  if number.endswith("1"):
    return number + "st"
  elif number.endswith("2"):
    return number + "nd"
  elif number.endswith("3"):
    return number + "rd"
  else:
    return number + "th"


assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'


print("Ex6 done")