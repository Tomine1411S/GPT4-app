import tkinter as tk
from tkinter import filedialog 
from tkinter import messagebox 
import tkinter.ttk as ttk
import time
import random as rand
import sys



#グローバル変数定義
main_bg = "aqua"
title_font = "Arial"
main_font = "Arial"

button_1 = "ふぁいる"
button_2 = "めにゅーう"
button_3 = "たいとるへ"
button_4 = "おぷしょんー"


# ウィンドウが生成されたフラグを取得するため（各ウィンドウが開いたときTrue、閉じたときFalseへ）
#global count_main, count_sub1, count_sub2, count_sub3
count_main = False
count_sub1 = False
count_sub2 = False
count_sub3 = False
count_sub4 = False



BUTTON_OPUTIONS = {
    "expand" : "True",
    "fill" : "tk.NONE",
    
}



#アプリケーション（GUI）クラス
class Application(tk.Frame):
    DEBUG_LOG = True
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()

        self.create_widgets()
        
    def create_widgets(self):
        
        global count_main
        count_main = True
        
        global pw_main, fm_main, fm_toolbar
        
        
        #メインウィンドウ作成
        pw_main = tk.PanedWindow(self.master, bg="blue", orient="vertical")
        pw_main.pack(expand=True, fill=tk.BOTH, side="left")
        
        #メインフレーム作成
        fm_main = tk.Frame(pw_main, bd=15, bg="aqua", relief="ridge")
        pw_main.add(fm_main)
        
    # -------- メインフレームのオブジェクト作成 --------
    
        
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_main, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        
        space_label = tk.Label(fm_main, text="", bg=main_bg, height=2)
        space_label.pack(side=tk.TOP)

        title_label = tk.Label(fm_main, text="~~~~~ ちゃっとじーぴーてぃーのあぷり ~~~~~", bg=main_bg, font=(title_font, 30), height=2)
        title_label.pack(side=tk.TOP)
        
        space_label = tk.Label(fm_main, text="", bg=main_bg, height=7)
        space_label.pack(side=tk.TOP)
    
        start_button = tk.Button(fm_main, text=" じゆうにあそぶ ", font=(main_font, 20), width=30, command=self.create_1)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" せっていしてあそぶ ", font=(main_font, 20), width=30, command=self.create_2)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" せんせいとあそぶ ", font=(main_font, 20), width=30, command=self.create_3)
        start_button.pack(side=tk.TOP, pady=10)
        start_button = tk.Button(fm_main, text=" おぷしょんだよ ", font=(main_font, 20), width=30, command=self.create_4)
        start_button.pack(side=tk.TOP, pady=10)
        
        

        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""


    
    #sub1
    def create_1(self):
        
        global count_sub1, count_main
        count_sub1 = True
        count_main = False
        
        global fm_sub1, pw_sub1
        pw_main.destroy()
        
        pw_sub1 = tk.PanedWindow(self.master, bg="blue", orient="vertical")
        pw_sub1.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_sub1 = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_sub1.add(fm_sub1)
    
    # -------- メインフレームのオブジェクト作成 --------
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_sub1, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
    
    
    #sub2
    def create_2(self):
                
        global count_sub2, count_main
        count_sub2 = True
        count_main = False
        
        global fm_sub2, pw_sub2
        pw_main.destroy()
        
        pw_sub2 = tk.PanedWindow(self.master, bg="red", orient="vertical")
        pw_sub2.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_sub2 = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_sub2.add(fm_sub2)
        
    # -------- メインフレームのオブジェクト作成 --------
    # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_sub2, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
        
    
    #sub3
    def create_3(self):
                
        global count_sub3, count_main
        count_sub3 = True
        count_main = False
        
        global fm_sub3, pw_sub3
        pw_main.destroy()
        
        pw_sub3 = tk.PanedWindow(self.master, bg="pink", orient="vertical")
        pw_sub3.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_sub3 = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_sub3.add(fm_sub3)
        
    # -------- メインフレームのオブジェクト作成 --------
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_sub3, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
    
    
    #sub4
    def create_4(self):
                
        global count_sub4, count_main
        count_sub4 = True
        count_main = False
        
        global fm_sub4, pw_sub4
        pw_main.destroy()
        
        pw_sub4 = tk.PanedWindow(self.master, bg="pink", orient="vertical")
        pw_sub4.pack(expand=True, fill=tk.BOTH, side="left")
        
        fm_sub4 = tk.Frame(bd=15, bg=main_bg, relief="ridge")
        pw_sub4.add(fm_sub4)
        
    # -------- メインフレームのオブジェクト作成 --------
        # ボタンを作成してツールバーに配置
        fm_toolbar = tk.Frame(fm_sub4, bg=main_bg)
        fm_toolbar.pack(anchor="nw")
        
        toolbar_button1 = tk.Button(fm_toolbar, text=button_1, bg="#fff")
        toolbar_button1.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button2 = tk.Button(fm_toolbar, text=button_2, bg="#fff")
        toolbar_button2.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button3 = tk.Button(fm_toolbar, text=button_3, bg="#fff", command=self.return_title)
        toolbar_button3.pack(side=tk.LEFT, padx=2, pady=2)
        toolbar_button4 = tk.Button(fm_toolbar, text=button_4, bg="#fff")
        toolbar_button4.pack(side=tk.LEFT, padx=2, pady=2)
        
        print('DEBUG:----{}----'.format(sys._getframe().f_code.co_name)) if self.DEBUG_LOG else ""
        
        
    
    # タイトルへ戻る
    def return_title(self):
        global count_main, count_sub1, count_sub2, count_sub3, count_sub4
        
        if count_main == True:
            pw_main.destroy()
        elif count_sub1 == True:
            pw_sub1.destroy()
        elif count_sub2 == True:
            pw_sub2.destroy()
        elif count_sub3 == True:
            pw_sub3.destroy()
        elif count_sub4 == True:
            pw_sub4.destroy()
        else:
            print("Error")
        
        print(str(count_main) + " : " + str(count_sub1) + " : " + str(count_sub2) + " : " + str(count_sub3))
        
        count_main = False
        count_sub1 = False
        count_sub2 = False
        count_sub3 = False
        
        self.create_widgets()
        
        
        return 0

        
        
# 実行
main_window = tk.Tk()       

#画面の幅と高さを取得
screen_width = main_window.winfo_screenwidth()
screen_height = main_window.winfo_screenheight()

myapp = Application(master=main_window)
myapp.master.title("DebianQuiz") # メインウィンドウの名前
myapp.master.geometry("1200x720") # ウィンドウの幅と高さピクセル単位で指定（width x height）
#myapp.master.attributes('-fullscreen', True) # フルスクリーン（終了ボタンがなくなるので非推奨）
myapp.mainloop()