# A classic example of an optimization problem involves making change using the fewest coins.
# Suppose you are a programmer for a vending machine manufacturer.
# Your company wants to streamline effort by giving out the fewest possible coins in change for each transaction.

# minCoins is the minimum number of coins for each number all the way up until 63
# coinValueList is the different coin value amounts we have [1, 5, 10, 25]
# change is the amount of change we are attempting to make
# coinsUsed is the type of coins we've used to get to the specific cents we are on in our array
def dpMakeChange(coinValueList,change,minCoins,coinsUsed):
   #  creating a list of possibilities to store minimum nuber
   # of coins per specific value
   # zero index list of the amt we want
   for cents in range(change+1):
      coinCount = cents
      # next coin to add
      newCoin = 1
      # for each value in the coin list we have, check to see
      # if the value is less than the current num cents we are on
      for j in [c for c in coinValueList if c <= cents]:
            # checking to sew what the min number coins
            # adding min coins (+1 to the min)
            if minCoins[cents-j] + 1 < coinCount:
               coinCount = minCoins[cents-j]+1
               newCoin = j
      # list of 63
      minCoins[cents] = coinCount
      # list of 63
      coinsUsed[cents] = newCoin
   return minCoins[change]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin

def main():
    amnt = 63
    clist = [1,5,10,21,25]
    coinsUsed = [0]*(amnt+1)
    coinCount = [0]*(amnt+1)

    print("Making change for",amnt,"requires")
    print(dpMakeChange(clist,amnt,coinCount,coinsUsed),"coins")
    print("They are:")
    printCoins(coinsUsed,amnt)
    print("The used list is as follows:")
    print(coinsUsed)

main()
