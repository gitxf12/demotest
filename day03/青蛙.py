high = 0
upper = 3
slip = 2
day = 0
while high < 20:
    day = day + 1
    high = high + upper
    if high == 20:
        print("第",day,"天爬出")
    else:
        high = high - slip



