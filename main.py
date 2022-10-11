from replit import clear
from art import logo
# as long as it is true we want to keep rerunning - so lets make a variable 
keep_going=True
slient_acution=[]
print(logo)
print('welcome to the silent auction!')
# we want to have a function that adds to a big list
def adding_to_silent():
  name=input('what is your name? ')
  bid=input('what is your bid ')
  new_bid={"name":name,"bid":bid}
  slient_acution.append(new_bid)
  print(slient_acution)

while keep_going ==True:
  adding_to_silent()
  next=input('is there another bid? y/n? ')
  if next == 'n':
    keep_going=False
  else:
    clear()
#lastly we want to be able to check the list
if keep_going == False: 
  bid=0
  for thing in slient_acution:
    new_bid=int(thing['bid'])
    if new_bid>bid:
      bid=new_bid
      winner=(thing["name"])
      
print(f'{winner} is the winner at ${bid}')       



