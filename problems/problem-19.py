import time

if __name__=="__main__":
    start = time.time()
    months = {"Jan": 31, "Feb": 28, "Mar": 31, "Apr": 30, "May": 31, "Jun": 30, "Jul": 31, "Aug": 31, "Sep": 30,
              "Oct": 31, "Nov": 30, "Dec": 31}
    total_days = 1
    day_of_week = 0
    sunday_count = 0

    for year in range(1900, 2000 + 1):
        for month, days in months.items():
            if month == "Feb" and (year % 4 == 0):
                days = 29
            total_days += days

            if year > 1900:
                day_of_week = total_days % 7
                if day_of_week == 0:
                    sunday_count += 1
    print("Sunday Count = {}".format(sunday_count))
    end = time.time()
    print("Completed in {0:.2}s".format(end - start))