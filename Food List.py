print("Enter the food items one by one you want to add to the list.")
print("when you are done hit q")
print("Enter the food item you want to add to the list :")
foodlist = []

while True:
    
    data = input()
    if (data) == "q" :
       break 
    foodlist.append(data)
breakpoint

print("Your final food list is:", foodlist)

