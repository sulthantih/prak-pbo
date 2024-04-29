import pygame
import random


pygame.init()


lebar_layar = 800
tinggi_layar = 600


layar = pygame.display.set_mode((lebar_layar, tinggi_layar))
pygame.display.set_caption("Game Ular")

gambar_ular = pygame.image.load("ular.png")
gambar_makanan = pygame.image.load("makanan.png")


ukuran_gambar_asli = gambar_ular.get_size()
ukuran_gambar_baru = (ukuran_gambar_asli[0] * 0.1, ukuran_gambar_asli[1] * 0.1)

gambar_ular = pygame.transform.scale(gambar_ular, ukuran_gambar_baru)
gambar_makanan = pygame.transform.scale(gambar_makanan, ukuran_gambar_baru)


x_ular = lebar_layar // 2
y_ular = tinggi_layar // 2


ukuran_ular = 10


panjang_ular = 5


x_makanan = random.randint(0, lebar_layar - gambar_makanan.get_width())
y_makanan = random.randint(0, tinggi_layar - gambar_makanan.get_height())


kecepatan_ular = 10


arah_ular = "ATAS"


skor = 0


font = pygame.font.Font(None, 36)


berjalan = True
while berjalan:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            berjalan = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and arah_ular != "KANAN":
                arah_ular = "KIRI"
            if event.key == pygame.K_RIGHT and arah_ular != "KIRI":
                arah_ular = "KANAN"
            if event.key == pygame.K_UP and arah_ular != "BAWAH":
                arah_ular = "ATAS"
            if event.key == pygame.K_DOWN and arah_ular != "ATAS":
                arah_ular = "BAWAH"

    if arah_ular == "ATAS":
        y_ular -= kecepatan_ular
    if arah_ular == "BAWAH":
        y_ular += kecepatan_ular
    if arah_ular == "KIRI":
        x_ular -= kecepatan_ular
    if arah_ular == "KANAN":
        x_ular += kecepatan_ular

    if x_ular < 0 or x_ular > lebar_layar - gambar_ular.get_width():
        berjalan = False
    if y_ular < 0 or y_ular > tinggi_layar - gambar_ular.get_height():
        berjalan = False

    if x_ular + ukuran_ular > x_makanan and x_ular < x_makanan + gambar_makanan.get_width() \
       and y_ular + ukuran_ular > y_makanan and y_ular < y_makanan + gambar_makanan.get_height():
        skor += 1
        panjang_ular += 1
        x_makanan = random.randint(0, lebar_layar - gambar_makanan.get_width())
        y_makanan = random.randint(0, tinggi_layar - gambar_makanan.get_height())

    layar.fill((0, 0, 0))

    for i in range(panjang_ular):
        x_segmen = x_ular + (i * ukuran_ular)
        layar.blit(gambar_ular, (x_segmen, y_ular))

    layar.blit(gambar_makanan, (x_makanan, y_makanan))

    teks_skor = font.render("Skor: " + str(skor), True, (255, 255, 255))
    layar.blit(teks_skor, (10, 10))

    pygame.display.update()

    jam = pygame.time.Clock()
    jam.tick(kecepatan_ular)

pygame.quit()
