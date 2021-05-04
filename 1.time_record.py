import time
start_time = time.time() # 시간 측정 시작

# ~~~~
# 프로그램 소스코드
a=[1,2,3,4,5]
b=0
for i in a:
   b += i
print(b)
# ~~~~


end_time=time.time() # 측정 종료
print("time: ",end_time - start_time) # 수행시간 출력
