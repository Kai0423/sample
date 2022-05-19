import random
import math

# ゲームの状態
class State:
    # 初期化
    def __init__(self, banmen=None):
        # 石の配置
        self.banmen = banmen if banmen != None else [2]*9
    
    # 先手かどうか
    def sente(self):
        return True if self.ishi_kazoeru(self.banmen) % 2 == 0 else False
    
    # 石の数を数える
    def ishi_kazoeru(self, banmen):
        isi_kazu = 0
        for i in banmen:
            if i != 2:
                isi_kazu += 1
        return isi_kazu
    
    # どちらかが勝ったか
    def shouhai(self):
        for i in range(2):
            if (self.banmen[0] == self.banmen[1] == self.banmen[2] == i) or \
                (self.banmen[3] == self.banmen[4] == self.banmen[5] == i) or \
                (self.banmen[6] == self.banmen[7] == self.banmen[8] == i) or \
                (self.banmen[0] == self.banmen[3] == self.banmen[6] == i) or \
                (self.banmen[1] == self.banmen[4] == self.banmen[7] == i) or \
                (self.banmen[2] == self.banmen[5] == self.banmen[8] == i) or \
                (self.banmen[0] == self.banmen[4] == self.banmen[8] == i) or \
                (self.banmen[2] == self.banmen[4] == self.banmen[6] == i):
                return True
        return False
    
    # 引き分け判定
    def hikiwake(self):
        if self.ishi_kazoeru(self.banmen) == 9:
            return True
    
    # ゲーム終了かどうか
    def game_done(self):
        return self.shouhai() or self.hikiwake()
    
    # 石を置く
    def ishi_oku(self, okubasho):
        self.banmen[okubasho] = 0 if self.sente() else 1
    
    # 合法手のリストを取得
    def okerubasho_list(self):
        okerubasho = []
        for i in range(9):
            if self.banmen[i] == 2:
                okerubasho.append(i)
        return okerubasho
    
    # ランダムで行動選択
    def random_action(self):
        okerubasho = self.okerubasho_list()
        print(okerubasho)
        return okerubasho[random.randint(0, len(okerubasho)-1)]