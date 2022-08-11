def stock_buy(prices):
          left,right = 0,1
          maxPro = 0

          while right < len(prices):
                    if prices[left] < prices[right]:
                              profit = prices[right] - prices[left]
                              maxPro = max(maxPro,profit)
                    else:
                              left = right
                    right += 1

          print(maxPro)                              


stock_buy([2,334,5,156,100])
