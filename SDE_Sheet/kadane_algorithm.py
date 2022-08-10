l=[-2,1,-3,4,-1,2,1,-5,4]
maxsum = 0
currsum = 0
for i in range (len(l)):
          currsum = currsum + l[i]
          if currsum > maxsum :
                    maxsum = currsum 

          if  currsum < 0 :
                    currsum = l[i]

print(maxsum)                    
