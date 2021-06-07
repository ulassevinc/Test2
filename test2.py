def getShares(totalIndividualShares):
    while(1):
        shares = int(input("Please enter the number of shares: "))
        if(shares==0):
            break
        elif(shares>0):
            totalIndividualShares.append(shares)


def getTotalShares(totalIndividualShares):
    totalShares = 0
    for share in totalIndividualShares:
        totalShares += share
    return totalShares


def countShareHoldersNeeded(totalSortedIndividualShares,sharesNeeded):
    shareSum = 0
    count = 0
    for share in totalSortedIndividualShares:
        shareSum += share
        count += 1
        if(shareSum >= sharesNeeded):
            break
    return count


def main():
    totalIndividualShares = []
    getShares(totalIndividualShares)
    totalShares = getTotalShares(totalIndividualShares)
    print("Thank you, there is a total of ",totalShares,"shares represented here.")
    
    sortedShares = sorted(totalIndividualShares,reverse=True)
    sharesNeeded = round(totalShares/2) + 1
    print("Shares needed for majority vote is ",sharesNeeded)
    supportShares = countShareHoldersNeeded(sortedShares,sharesNeeded)
    print("You need the support of top ",supportShares," shareholders for this number of votes.")


main()


