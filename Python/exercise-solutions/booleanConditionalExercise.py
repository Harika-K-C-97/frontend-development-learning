miles = int(input('How far would you like to travel in miles? '))
if miles < 3:
  print('I suggest you to walk to your destination.')
elif miles > 3 and miles < 300:
  print('I suggest you to drive to your destination.')
else:
  print('I suggest you to fly to your destination.')