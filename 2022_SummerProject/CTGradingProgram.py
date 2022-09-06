import requests
from bs4 import BeautifulSoup as bs
import time


''' 
이곳에 파일을 붙여넣기 합니다.
기본으로 설정된 함수의 이름은 'solution', 매개변수는 하나입니다.
'''


q_num = input()
qna_list = []
cnt = 0.0

response = requests.get("https://www.acmicpc.net/problem/" + q_num)

html = bs(response.text, 'html.parser')

sample = html.select('pre.sampledata')

for i in sample:
    qna_list.append(i.get_text().replace('\r\n', ''))

start = time.time()
for i in range(0, int(len(qna_list)/2)+1, 2):
    answer = solution(a[i])
    if not 'A' <= qna_list[i+1][0] <= 'z':
        answer = str(answer) + '\n'
    if answer == qna_list[i+1]:
            print("Correct!")
            cnt += 1
    else:
            print("Incorrect!")

end = time.time()
print("Score:", cnt/(len(qna_list)/2)*100)
print("time: %.2fms" %((end - start)*1000))