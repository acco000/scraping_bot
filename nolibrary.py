string = "This is a penなんて生涯使ったことないsentenceですよ\
    1回も使ったことないでしょうが?\
        みんな。This is a penなんて言ったことある?ないだろー!?"

counter = {}
for w in string:
    if w in counter:
        counter[w] += 1
    else:
        counter[w] = 1
print(counter)