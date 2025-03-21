import pygame
import time
import random

# Pygame başlat
pygame.init()

# Renkler
beyaz = (255, 255, 255)
siyah = (0, 0, 0)
kirmizi = (213, 50, 80)
yesil = (0, 255, 0)
mavi = (50, 153, 213)

# Ekran boyutları
displey_genislik = 600
displey_yukseklik = 400
displey = pygame.display.set_mode((displey_genislik, displey_yukseklik))
pygame.display.set_caption('Snake Game')

# Yılanın boyutu ve hızı
yilan_boyut = 10
yilan_hiz = 10

# Saat (FPS kontrolü)
saat = pygame.time.Clock()

# Font ayarları
font_stil = pygame.font.SysFont("bahnschrift", 25)
skor_font = pygame.font.SysFont("comicsansms", 35)

# Skor fonksiyonu
def skor_goster(skor):
    value = skor_font.render("Score: " + str(skor), True, siyah)
    displey.blit(value, [0, 0])

# Yılanı ekrana çizme fonksiyonu
def yilan_ciz(yilan_boyutu, yilan_lista):
    for x in yilan_lista:
        pygame.draw.rect(displey, yesil, [x[0], x[1], yilan_boyutu, yilan_boyutu])

# Ana oyun döngüsü
def oyun():
    oyun_bitti = False
    oyun_baslat = True

    x1 = displey_genislik / 2
    y1 = displey_yukseklik / 2

    x1_degisiklik = 0
    y1_degisiklik = 0

    yilan_lista = []
    uzunluk = 1

    yilan_hiz = 10

    # Yem oluşturma
    yemek_x = round(random.randrange(0, displey_genislik - yilan_boyut) / 10.0) * 10.0
    yemek_y = round(random.randrange(0, displey_yukseklik - yilan_boyut) / 10.0) * 10.0

    while oyun_baslat:

        # Oyun bitmişse
        while oyun_bitti == True:
            displey.fill(mavi)
            mesaj = font_stil.render("            You Beat. Press ESC.", True, kirmizi)
            displey.blit(mesaj, [displey_genislik / 6, displey_yukseklik / 3])
            skor_goster(uzunluk - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    oyun_bitti = False
                    oyun_baslat = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        oyun_bitti = False
                        oyun_baslat = False
                    if event.key == pygame.K_c:
                        oyun()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                oyun_bitti = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_degisiklik = -yilan_boyut
                    y1_degisiklik = 0
                elif event.key == pygame.K_RIGHT:
                    x1_degisiklik = yilan_boyut
                    y1_degisiklik = 0
                elif event.key == pygame.K_UP:
                    y1_degisiklik = -yilan_boyut
                    x1_degisiklik = 0
                elif event.key == pygame.K_DOWN:
                    y1_degisiklik = yilan_boyut
                    x1_degisiklik = 0

        # Yılanın sınırları geçmesi durumu
        if x1 >= displey_genislik or x1 < 0 or y1 >= displey_yukseklik or y1 < 0:
            oyun_bitti = True

        x1 += x1_degisiklik
        y1 += y1_degisiklik
        displey.fill(mavi)

        pygame.draw.rect(displey, siyah, [yemek_x, yemek_y, yilan_boyut, yilan_boyut])
        yilan_kafasi = []
        yilan_kafasi.append(x1)
        yilan_kafasi.append(y1)
        yilan_lista.append(yilan_kafasi)

        if len(yilan_lista) > uzunluk:
            del yilan_lista[0]

        for x in yilan_lista[:-1]:
            if x == yilan_kafasi:
                oyun_bitti = True

        yilan_ciz(yilan_boyut, yilan_lista)
        skor_goster(uzunluk - 1)

        pygame.display.update()

        # Yılan yemeği yediğinde
        if x1 == yemek_x and y1 == yemek_y:
            yemek_x = round(random.randrange(0, displey_genislik - yilan_boyut) / 10.0) * 10.0
            yemek_y = round(random.randrange(0, displey_yukseklik - yilan_boyut) / 10.0) * 10.0
            uzunluk += 1

        saat.tick(yilan_hiz)

    # Oyun bitince bekleme
    input("Game Over! Press ESC...")

    pygame.quit()
    quit()

# Oyunu başlat
oyun()
