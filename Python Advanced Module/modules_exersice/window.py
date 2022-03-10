import tkinter as tk

def render_main_screen(window):
    B = tk.Button(window, text = "Hello", command = lambda : print('Hello word'))
    login_buton = tk.Button(window, text = "Login", bg = 'green', fg = 'white', command = lambda : print('Hello word!'))
if __name__ == '__main__':
    window = tk.Tk()
    window.geometry('600x600')
    window.title('My cool GUI Shop')
    window.mainloop()