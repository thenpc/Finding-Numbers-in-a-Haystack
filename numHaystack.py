import re

text = open ('regex_sum_338091.txt')
numList = list()
for line in text:
    line = line.rstrip()
    results = re.findall('[0-9]+', line)
    for answer in results:
        y = int(answer)
        numList.append(y)

print ( 'There are ' + str(len(numList)) + ' numbers in this file that have a total sum of ' + str(sum(numList)))
