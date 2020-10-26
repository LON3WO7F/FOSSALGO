def linearsearch(name, element):
   for i in range(len(name)):
      if name[i] == element:
         return i
   return -1
name = ['G','o','u','r','a','v','s','p','w','t']
element = 'a'
print("element found at index "+str(linearsearch(name,element)))
