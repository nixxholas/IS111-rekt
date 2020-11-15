from q5 import get_document_pair

print ('Test 1')
print ("Expected:[('D2', 'D4', 3)]")
print ("Actual  :" + str(get_document_pair('documents1.txt')))
print ()

print ('Test 2')
print ("Expected:[('D01', 'D02', 3), ('D03', 'D04', 3), ('D05', 'D06', 3)]")
print ("Actual  :" + str(get_document_pair('documents2.txt')))
print ()
