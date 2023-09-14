import tkinter as tk

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Lỗi")

# Tạo cửa sổ giao diện đồ họa
window = tk.Tk()
window.title("Máy tính cầm tay")

# Tạo ô nhập liệu
entry = tk.Entry(window, width=20, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4)

# Tạo các nút số và phép toán
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    ('bui van hieu', 4),  # Change to a tuple with the button text and columnspan
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

# ...
for button_text in buttons:
    if isinstance(button_text, tuple):  # If it's a tuple of buttons
        button = tk.Button(
            window, text=button_text[0], padx=50, pady=10, font=('Arial', 25),
            command=lambda b=button_text[0]: button_click(b) if b != '=' else calculate()
        )
        if button_text[0] == 'bui van hieu':
            button.config(state="disabled")
        button.grid(row=row_val, column=col_val, columnspan=button_text[1])
    else:
        button = tk.Button(
            window, text=button_text, padx=15, pady=10, font=('Arial', 25),
            command=lambda b=button_text: button_click(b) if b != '=' else calculate()
        )
        button.grid(row=row_val, column=col_val)


    col_val += button_text[1] if isinstance(button_text, tuple) else 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Nút xóa
tk.Button(
    window, text='C', padx=15, pady=15, font=('Arial', 20),
    command=clear
).grid(row=row_val, column=col_val)

# Bắt đầu vòng lặp chạy ứng dụng
window.mainloop()