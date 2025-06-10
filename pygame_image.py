import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#背景画像のSurface
    bg_img2=pg.transform.flip(bg_img,True,False)#背景反転
    kk_img=pg.image.load("fig/3.png")
    kk_img=pg.transform.flip(kk_img,True,False)

    kk_rct=kk_img.get_rect()#こうかとんのrect
    kk_rct.center=300,200#こうかとん画像の中心座標の設定

    

    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        
        key_lst=pg.key.get_pressed()#押されたキー取得
        if key_lst[pg.K_UP]:         
            kk_rct.move_ip((0,-1))
        if key_lst[pg.K_DOWN]:         
            kk_rct.move_ip((0,+1))
        if key_lst[pg.K_LEFT]:         
            kk_rct.move_ip((-1,0))
        if key_lst[pg.K_RIGHT]:         
            kk_rct.move_ip((1,0))
        
        screen.blit(bg_img, [-tmr, 0])
        screen.blit(bg_img2,[-tmr+1600,0])
        screen.blit(bg_img,[-tmr+3200,0])
       #screen.blit(kk_img,[300,200])
        screen.blit(kk_img,kk_rct)
        pg.display.update()
        tmr += 1   

        if tmr==3199:
            tmr=0   
        clock.tick(200)
        


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()