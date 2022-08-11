def stock_buy(prices):
          left,right = 0,1                                         # creating two pointer left, right for numbers of days comaparison
          maxPro = 0                                               # initiaizing max_profit to 0

          while right < len(prices):                               # looping till the length of list 
                    if prices[left] < prices[right]:               # comparing left and right day price if right is greater then substract with left to calculate the                                                                             profit
                              
                              profit = prices[right] - prices[left]
                              maxPro = max(maxPro,profit)                        #finding the maxprofit from profit and maxprofit stored 
                    else:
                              left = right                                       # otherwise if left is greater than right then bring the left pointer to right and                                                                                            increment right by 1
                    right += 1

          print(maxPro)                              


stock_buy([2,334,5,156,100])
