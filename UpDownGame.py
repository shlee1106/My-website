import random
from tkinter import *

# 랜덤 숫자 생성
answer = random.randint(1, 100)
attempts = 0  # 시도 횟수
max_attempts = 6  # 최대 시도 횟수

def numberGame():
    global attempts, answer, max_attempts

    try:
        number = int(ety.get())
    except ValueError:
        lbl_result.config(text="❌ 숫자를 입력하세요!", fg="red")
        return

    attempts += 1
    remaining_attempts = max_attempts - attempts  # 남은 시도 횟수 계산
    lbl_attempts.config(text=f"시도 횟수: {attempts}번")  # 시도 횟수 갱신
    lbl_chance.config(text=f"남은 시도 횟수: {remaining_attempts}번")  # 남은 시도 횟수 갱신


    if number < answer:
        lbl_result.config(text="🔼 더 큰 숫자입니다.", fg="blue")
        diff = abs(number - answer)
        if diff <= 5:
            lbl_result.config(text="🔥 아주 가깝습니다!")
    elif number > answer:
        lbl_result.config(text="🔽 더 작은 숫자입니다.", fg="orange")
        diff = abs(number - answer)
        if diff <= 5:
            lbl_result.config(text="🔥 아주 가깝습니다!")
    else:
        lbl_result.config(
            text=f"🎉 정답입니다! 정답: {answer}\n총 시도 횟수: {attempts}번", fg="green"
        )
        reset_game()
        return

    if attempts == max_attempts:
        lbl_result.config(text=f"💔 실패! 정답은 {answer}입니다.", fg="red")
        reset_game()

def reset_game():
    global attempts, answer, max_attempts
    attempts = 0
    answer = random.randint(1, 100)
    ety.delete(0, END)
    lbl_attempts.config(text="시도 횟수: 0번")  # 시도 횟수 초기화
    lbl_chance.config(text=f"남은 시도 횟수: {max_attempts}번")  # 남은 시도 횟수 초기화

# GUI 설정
window = Tk()
window.title("숫자 맞추기 게임")
window.geometry("450x350")
window.configure(bg="#f9f9f9")  # 배경색
window.bind("<Return>", lambda event: numberGame()) #엔터 키로 확인 버튼 동작


# grid에서 위젯들이 중앙에 정렬되도록 설정
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)

# 제목
lbl_title = Label(
    window,
    text="🔢 숫자 맞추기 게임 🔢",
    font=("Helvetica", 16, "bold"),
    bg="#f9f9f9",
    fg="#333",
)
lbl_title.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

# 설명
lbl_subtitle = Label(
    window,
    text="1부터 100 사이의 숫자를 맞혀보세요! (기회: 6번)",
    font=("Helvetica", 12),
    bg="#f9f9f9",
    fg="#666",
)
lbl_subtitle.grid(row=1, column=0, columnspan=2, pady=5, sticky="nsew")

# 입력 필드
ety = Entry(window, font=("Helvetica", 14), width=10, justify="center")
ety.grid(row=2, column=0, columnspan=2, pady=10, sticky="nsew")

# 확인 버튼
btn = Button(
    window,
    text="확인!",
    font=("Helvetica", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    command=numberGame,
)
btn.grid(row=3, column=0, columnspan=2, pady=10, sticky="nsew")

# 결과 표시
lbl_result = Label(window, text="", font=("Helvetica", 14), bg="#f9f9f9", fg="#333")
lbl_result.grid(row=4, column=0, columnspan=2, pady=10, sticky="nsew")

# 시도 횟수와 남은 시도 횟수 표시 (grid 사용)
lbl_attempts = Label(
    window, text="시도 횟수: 0번", font=("Helvetica", 12), bg="#f9f9f9", fg="#666"
)
lbl_chance = Label(
    window, text=f"남은 시도 횟수: {max_attempts}번", font=("Helvetica", 12), bg="#f9f9f9", fg="#666"
)

# 시도 횟수와 남은 시도 횟수를 좌우로 배치
lbl_attempts.grid(row=5, column=0, padx=20, pady=5, sticky="w")  # 왼쪽에 배치
lbl_chance.grid(row=5, column=1, padx=30, pady=5, sticky="e")  # 오른쪽에 배치

# 하단 메모
lbl_footer = Label(
    window,
    text="🎯 행운을 빕니다! 🎯",
    font=("Helvetica", 10),
    bg="#f9f9f9",
    fg="#999",
)
lbl_footer.grid(row=6, column=0, columnspan=2, pady=15, sticky="nsew")

# 창 크기 조정 불가
window.resizable(False, False)

window.mainloop()
