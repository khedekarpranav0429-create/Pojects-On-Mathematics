import math
PerDay_Visitors=[83767,18397407,673853899,78379278397,848349483840938]
Log_Traffic=[]
for Day,Traffic in enumerate(PerDay_Visitors,start=1):
    LowData=math.log10(Traffic)
    Log_Traffic.append(LowData)
    difference=0
    if Day >1:
        difference=Traffic-PerDay_Visitors[Day-2]
    print()
    print("Day :",Day)
    print("Visitore :",Traffic)
    print("Increse :",difference)
    print("Log Traffic :",LowData)
    print("----------------------------")

