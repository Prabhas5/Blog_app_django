'''Assignment 2: Algorithm Implementation and Optimization

Problem Statement: You are given a list of integers representing stock prices on consecutive days.
Write a Python function max_profit(prices) that calculates the maximum profit that can be achieved 
by buying and selling the stock once. Additionally, optimize the function to minimize time complexity.'''

#Solution 

#input arr
prices=[7, 12, 5, 3, 12, 4, 9, 2, 8] 
def mx_profit(prices:list):
    # if list is empty return zero
    if not prices:
        return 0
    max_profit=0
    min_price=prices[0]
    #from second index
    i=1
    while i<len(prices):
        if prices[i]<min_price:
            #keep the minimum value store
            min_price=prices[i]
        else:
            max_profit=max(max_profit,(prices[i]-min_price))
        
        i+=1
    return max_profit
print(mx_profit(prices=prices))

