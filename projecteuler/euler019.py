"""
* 1 Jan 1900 was a Monday.
* Thirty days has September,
  April, June and November.
  All the rest have thirty-one,
  Saving February alone,
  Which has twenty-eight, rain or shine.
  And on leap years, twenty-nine.
* A leap year occurs on any year evenly divisible by 4, but not on a century 
  unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth 
century (1 Jan 1901 to 31 Dec 2000)?
"""

primer_sundays = 0
last_first = 2 # 0=Sunday, 1=Monday, etc...

for year in range(1901, 2001):
    primers = 0
    is_leap = year%4 is 0
    for month in xrange(1,13):
        next_first = -1
        if month in (1, 3, 5, 7, 8, 10, 12):
            next_first = 3 + last_first
        elif month in (11, 4, 6, 9,):
            next_first = 2 + last_first
        else:
            next_first = int(is_leap) + last_first
        next_first = next_first%7

        if next_first%7 == 0:
            primers += 1
        last_first = next_first
    print "during %d found: %d" % (year,primers,)
    primer_sundays += primers

print primer_sundays
        
     