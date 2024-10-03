# Count the number of Sunday jack will get within n number of days.
# Example 1:
# Input
# mon-> input String denoting the start of the month.
# 13 -> input integer denoting the number of days from the start of the month.
# Output :
# 2 -> number of days within 13 days.
# Explanation:
# The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then
# next Sunday in next 7 days and so on.
# Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will
# end up in another sunday. Total 2 sundays may fall within 13 days.

def sunsum(day,days):
    x=0
    mydict={"mon":6,"tue":5,"wed":4,"thu":3,"fri":2,"sat":1,"sun":0}
    if days-mydict[day]>=0:
        x=days-mydict[day]
        if day=="sun":
            x-=1
        return (x//7)+1
    else:
        return -1
z=sunsum("thu",2)
print(z)