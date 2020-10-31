import q6


print ('Test 1:')
neighbours = [("Mary", "Jason"), ("John", "Alan"), 
              ("Jason", "George"), ("Alan", "Christie"), 
              ("Christie", "Mary"), ("George", "")]
print ("Expected:['John', 'Alan', 'Christie', 'Mary', 'Jason', 'George']")
print ("Actual  :" + str(q6.get_lineup(neighbours)) )
print()

print ('Test 2:')
neighbours = [("Chris", "Darren"), ("Alice", "Bob"), 
              ("Darren", ""), ("Bob", "Chris")]
print ('Expected:["Alice", "Bob", "Chris", "Darren"]')
print ("Actual  :" + str(q6.get_lineup(neighbours)))