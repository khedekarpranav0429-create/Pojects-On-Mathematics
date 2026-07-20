Months=[6,12,24]
CurrentSubscribers=5000
GrowthPermonth=12/100
for Month in Months:
    NewSubscribers=(CurrentSubscribers*(1+GrowthPermonth)**Month)
    Growth=NewSubscribers -CurrentSubscribers
    print()
    print("After",Month,"Month:")
    print("Subcriber :",int(NewSubscribers))
    print("Growth :",int(Growth))
    print("----------------------------------")

