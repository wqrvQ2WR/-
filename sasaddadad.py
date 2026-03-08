import time

StartTime = time.time()
입력 = input("문자열 입력: ")
EndTime = time.time()

걸린시간_초 = EndTime - StartTime
걸린시간_분 = 걸린시간_초 / 60

단어수 = len(입력) / 5   # 1단어 = 5글자 기준
WPM = 단어수 / 걸린시간_분

print("걸린 시간:", 걸린시간_초, "초")
print("추정 단어 수:", 단어수)
print("타자 속도:", WPM, "WPM")