import pygame
from pygame.locals import *
from random import randint

pygame.init()

largura = 640
altura = 480
snake_x = largura / 2 - 25
snake_y = altura / 2 - 25
apple_x = randint(0,590)
apple_y = randint(0,430)
x_controle = 0
y_controle = 0
velocidade = 8
fontPrimary = pygame.font.SysFont('Arial', 20, True, True)
fontSecundary = pygame.font.SysFont('Arial', 12, True, True)
tela = pygame.display.set_mode([largura, altura])
pygame.display.set_caption('Snake')
Clock = pygame.time.Clock()

def snake_up(lista_cobra):
    for XY in lista_cobra:
        pygame.draw.rect(tela,[0,255,0],(XY[0],XY[1],20,20))
def game_over():
    tela.fill([255, 255, 255])
    # Mensagem de Game Over
    texto = fontPrimary.render("GAME OVER", True, [0, 0, 0])
    tela.blit(texto, [largura / 2 - 50, altura / 2 - 50])
    # Mensagem jogar novamente
    texto = fontSecundary.render("Press [ENTER] p/Jogar Novamente", True, [100, 100, 100])
    tela.blit(texto, [largura / 2 - 95, altura / 2 - 20])


lista_cobra = []
pontos = 0
tamanho_snake = 3
on = True
while on:
    Clock.tick(60)
    tela.fill([255,255,255])
    menssagem = (f'Pontos: {pontos}')
    texto = fontPrimary.render(menssagem, False, [0, 0, 0])
    tela.blit(texto,[500,40])
    for event in pygame.event.get():
        if event.type == QUIT:
            on = False
        if event.type == KEYDOWN:
            if event.key == K_w:
                x_controle = 0
                y_controle = -velocidade
            if event.key == K_a:
                x_controle = -velocidade
                y_controle = 0
            if event.key == K_s:
                x_controle = 0
                y_controle = velocidade
            if event.key == K_d:
                x_controle = velocidade
                y_controle = 0
    snake_x += x_controle
    snake_y += y_controle

    if pygame.key.get_pressed()[K_UP]:
        x_controle = 0
        y_controle = -velocidade
    if pygame.key.get_pressed()[K_LEFT]:
        x_controle = -velocidade
        y_controle = 0
    if pygame.key.get_pressed()[K_DOWN]:
        x_controle = 0
        y_controle = velocidade
    if pygame.key.get_pressed()[K_RIGHT]:
        x_controle = velocidade
        y_controle = 0
    snake = pygame.draw.rect(tela, [0,255,0], (snake_x, snake_y, 20, 20))
    apple = pygame.draw.rect(tela,[255,0,0],(apple_x,apple_y,20,20))

    if apple.colliderect(snake):
        apple_x = randint(0, 590)
        apple_y = randint(0, 430)
        pontos += 1
        tamanho_snake += 1

    lista_cabeca = []
    lista_cabeca.append(snake_x)
    lista_cabeca.append(snake_y)

    lista_cobra.append(lista_cabeca)
    snake_up(lista_cobra)
    mouse = pygame.mouse.get_pressed()

    if len(lista_cobra) > tamanho_snake:
        del lista_cobra[0]
    if snake_x > largura + 50:
        game_over()
        if (mouse[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]):
            pontos = 0
            snake_x = largura / 2 - 25
            snake_y = altura / 2 - 25
            x_controle = 0
            y_controle = 0
    if snake_x < 0:
        game_over()
        if (mouse[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]):
            pontos = 0
            snake_x = largura / 2 - 25
            snake_y = altura / 2 - 25
            x_controle = 0
            y_controle = 0
    if snake_y >  altura + 50:
        game_over()
        if (mouse[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]):
            pontos = 0
            snake_x = largura / 2 - 25
            snake_y = altura / 2 - 25
            x_controle = 0
            y_controle = 0
    if snake_y < 0:
        game_over()
        if (mouse[0] or pygame.mouse.get_pressed()[1] or pygame.mouse.get_pressed()[2]):
            pontos = 0
            snake_x = largura / 2 - 25
            snake_y = altura / 2 - 25
            x_controle = 0
            y_controle = 0
    pygame.display.update()