n=int(input())
li=[[1]]                       # intiliaze a list with first element

for i in range(n - 1):                                       # loop  through till n-1 element
          temp = [0] + li[-1] + [0]                          # add 0 to first and last element 
          row =[]                                            # create a empty list to add next element
          for j in range(len(li[-1])+1):                     # loop through the lengh of pervious element + 1          
                    row.append(temp[j]+temp[j+1])            # add the two adjacent pointer j , j+1 and append to row
          li.append(row)                                     # append it to li
print(li)                          