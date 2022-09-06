import requests
from bs4 import BeautifulSoup as bs
import time

def solution(para):
    a = '1 1 2 2 2 8'
    answer = ""
    for i in range(len(a)):
        if not para[i] == ' ':
            answer += str(int(a[i]) - int(para[i]))
        else:
            answer += ' '
    return answer


q_num = input()
a = []
cnt = 0.0

response = requests.get("https://www.acmicpc.net/problem/" + q_num)

html = bs(response.text, 'html.parser')

sample = html.select('pre.sampledata')

for i in sample:
    a.append(i.get_text().replace('\r\n', ''))

start = time.time()
for i in range(0, int(len(a)/2)+1, 2):
    b = solution(a[i])
    if not 'A' <= a[i+1][0] <= 'z':
        b = str(b) + '\n'
    if b == a[i+1]:
            print("Correct!")
            cnt += 1
    else:
            print("Incorrect!")

end = time.time()
print("Score:", cnt/(len(a)/2)*100)
print("time: %.2fms" %((end - start)*1000))


