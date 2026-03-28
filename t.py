import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("머쉬베놈 스타일 대시보드 - 파이썬짱") #
root.geometry("800x450")

# 1. 이미지 불러오기 (이미지 파일이 파이썬 파일과 같은 폴더에 있어야 합니다)
# 주의: tkinter 기본 PhotoImage는 .gif, .png만 지원합니다. (.jpg는 별도 라이브러리 필요)
bg_image = PhotoImage(file="C:\\Users\\우리가족\\새 폴더\\깃\\back.png") 

# 2. 배경 이미지를 담을 레이블 생성
# root 전체를 꽉 채우도록 설정합니다.
bg_label = tk.Label(root, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1) # 화면에 꽉 채우기

# 3. 그 위에 다른 위젯 올리기
# 배경 레이블이 깔린 상태이므로, 다른 위젯들은 그 위에 나타납니다.
title_label = tk.Label(root, text="고독하구만", font=("Arial", 18), bg="blue")
title_label.pack(pady=10)

root.mainloop()