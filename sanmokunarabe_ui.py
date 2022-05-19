from sanmokunarabe_game import State
import tkinter as tk

# UIクラス
class GameUI(tk.Frame):
    # 初期化
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title('三目並べ')

        self.state = State()

        # キャンバスの生成
        self.c = tk.Canvas(self, width=300, height=300)
        self.c.bind('<Button-1>', self.turn_of_human)
        self.c.pack()

        # 描画の更新
        self.update_draw()
    
    # 人間のターン
    def turn_of_human(self, event):
        # ゲーム終了時
        if self.state.game_done():
            # 初期状態に戻す
            self.state = State()
            self.update_draw()
            return
        
        # 機械のターンのとき
        if not self.state.sente():
            return
        
        # クリック位置を行動に変換
        x = int(event.x/100)
        y = int(event.y/100)
        if x < 0 or 2 < x or y < 0 or 2 < y: # 範囲外
            return
        okubasho = x + y * 3

        # 置けない場所
        if not (okubasho in self.state.okerubasho_list()):
            return
        
        # 次の状態を取得
        self.state.ishi_oku(okubasho)
        self.update_draw()

        # 機械のターン
        self.master.after(1000, self.turn_of_ai)
    
    # 機械のターン
    def turn_of_ai(self):
        # ゲーム終了時
        if self.state.game_done():
            return
        
        # 行動の取得
        okubasho = self.state.random_action()

        # 次の状態を取得
        self.state.ishi_oku(okubasho)
        self.update_draw()
    
    # 石の描画
    def draw_ishi(self, index, player):
        x = (index%3)*100+10
        y = int(index/3)*100+10
        if not player:
            self.c.create_oval(x, y, x+80, y+80, width = 4.0, outline = '#FF0000')
        else:
            self.c.create_line(x, y, x+80, y+80, width = 4.0, fill = '#0000FF')
            self.c.create_line(x+80, y, x, y+80, width = 4.0, fill = '#0000FF')
    
    # 描画の更新
    def update_draw(self):
        self.c.delete('all')
        self.c.create_rectangle(0, 0, 300, 300, width = 0.0, fill = '#FFFFFF')
        self.c.create_line(100, 0, 100, 300, width = 2.0, fill = '#000000')
        self.c.create_line(200, 0, 200, 300, width = 2.0, fill = '#000000')
        self.c.create_line(0, 100, 300, 100,  width = 2.0, fill = '#000000')
        self.c.create_line(0, 200, 300, 200, width = 2.0, fill = '#000000')
        for i in range(9):
            if self.state.banmen[i] == 0:
                self.draw_ishi(i, False)
            if self.state.banmen[i] == 1:
                self.draw_ishi(i, True)



# ゲームの実行
f = GameUI()
f.pack()
f.mainloop()