# Importação do módulo Pygame e bibliotecas adicionais
import pygame
import math

# Inicializa o Pygame
pygame.init()

# Configurações da tela e definição de cores
LARGURA = 900
ALTURA = 400
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Air Hockey - Dois Jogadores")

# Definição de cores em RGB
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
CINZA = (200, 200, 200)
VERDE = (0, 255, 0)

# Parâmetros iniciais
RAIO_DISCO = 15
RAIO_JOGADOR = 30
VELOCIDADE_MAX_DISCO = 6
VELOCIDADE_MAX_JOGADOR = 5
MASSA_DISCO = 0.5
MASSA_JOGADOR = 2

# Posições dos gols
GOL_ESQUERDA = (0, ALTURA // 2 - 50, 10, 100)
GOL_DIREITA = (LARGURA - 10, ALTURA // 2 - 50, 10, 100)

# Classe Disco
class Disco:
    def __init__(self, x, y, velocidade_x, velocidade_y, massa):
        self.x = x
        self.y = y
        self.velocidade_x = velocidade_x
        self.velocidade_y = velocidade_y
        self.massa = massa

    def mover(self):
        self.x += self.velocidade_x
        self.y += self.velocidade_y

        # Limitar a velocidade máxima do disco
        velocidade = math.sqrt(self.velocidade_x**2 + self.velocidade_y**2)
        if velocidade > VELOCIDADE_MAX_DISCO:
            fator = VELOCIDADE_MAX_DISCO / velocidade
            self.velocidade_x *= fator
            self.velocidade_y *= fator

    def colisao_parede(self):
        if self.x <= RAIO_DISCO or self.x >= LARGURA - RAIO_DISCO:
            self.velocidade_x = -self.velocidade_x
        if self.y <= RAIO_DISCO or self.y >= ALTURA - RAIO_DISCO:
            self.velocidade_y = -self.velocidade_y

    def colisao_jogador(self, jogador):
        dx = self.x - jogador.x
        dy = self.y - jogador.y
        distancia = math.sqrt(dx**2 + dy**2)
        if distancia <= RAIO_DISCO + RAIO_JOGADOR:
            angulo = math.atan2(dy, dx)
            velocidade_distribuida = math.sqrt(jogador.velocidade_x**2 + jogador.velocidade_y**2)
            self.velocidade_x += (velocidade_distribuida * math.cos(angulo)) / self.massa
            self.velocidade_y += (velocidade_distribuida * math.sin(angulo)) / self.massa

    def desenhar(self):
        pygame.draw.circle(TELA, BRANCO, (int(self.x), int(self.y)), RAIO_DISCO)
        pygame.draw.line(TELA, BRANCO, (int(self.x), int(self.y)),
                         (int(self.x + self.velocidade_x * 10), int(self.y + self.velocidade_y * 10)), 2)

# Classe Jogador
class Jogador:
    def __init__(self, x, y, teclas, massa):
        self.x = x
        self.y = y
        self.velocidade_x = 0
        self.velocidade_y = 0
        self.massa = massa
        self.teclas = teclas

    def mover(self):
        keys = pygame.key.get_pressed()
        if keys[self.teclas["cima"]]:
            self.velocidade_y = -VELOCIDADE_MAX_JOGADOR
        elif keys[self.teclas["baixo"]]:
            self.velocidade_y = VELOCIDADE_MAX_JOGADOR
        else:
            self.velocidade_y = 0

        if keys[self.teclas["esquerda"]]:
            self.velocidade_x = -VELOCIDADE_MAX_JOGADOR
        elif keys[self.teclas["direita"]]:
            self.velocidade_x = VELOCIDADE_MAX_JOGADOR
        else:
            self.velocidade_x = 0

        self.x += self.velocidade_x
        self.y += self.velocidade_y

        # Limitar o jogador à área de jogo
        self.x = max(RAIO_JOGADOR, min(LARGURA - RAIO_JOGADOR, self.x))
        self.y = max(RAIO_JOGADOR, min(ALTURA - RAIO_JOGADOR, self.y))

    def desenhar(self):
        cor = AZUL if self.teclas["cima"] == pygame.K_w else VERMELHO
        pygame.draw.circle(TELA, cor, (int(self.x), int(self.y)), RAIO_JOGADOR)
        pygame.draw.line(TELA, cor, (int(self.x), int(self.y)),
                         (int(self.x + self.velocidade_x * 10), int(self.y + self.velocidade_y * 10)), 2)

# Função para desenhar texto na tela
def desenhar_texto(texto, cor, x, y, tamanho):
    fonte = pygame.font.Font(None, tamanho)
    texto_surface = fonte.render(texto, True, cor)
    texto_rect = texto_surface.get_rect(center=(x, y))
    TELA.blit(texto_surface, texto_rect)

# Função para desenhar a tabela de informações
def desenhar_tabela(placar, velocidade_dis):
    desenhar_texto(f"Placar: {placar[0]} - {placar[1]}", BRANCO, 750, 30, 30)
    desenhar_texto(f"Velocidade Disco: {velocidade_dis:.2f}", BRANCO, 750, 60, 20)
    desenhar_texto(f"Massa Disco: {MASSA_DISCO}", BRANCO, 750, 90, 20)

# Menu principal para configurações
def menu_principal():
    global VELOCIDADE_MAX_DISCO, VELOCIDADE_MAX_JOGADOR
    rodando = True
    while rodando:
        TELA.fill(PRETO)
        desenhar_texto("Air Hockey", BRANCO, LARGURA // 2, ALTURA // 4, 50)
        desenhar_texto("Pressione [1] para aumentar a velocidade do disco", BRANCO, LARGURA // 2, ALTURA // 2, 30)
        desenhar_texto("Pressione [2] para diminuir a velocidade do disco", BRANCO, LARGURA // 2, ALTURA // 2 + 40, 30)
        desenhar_texto("Pressione [3] para aumentar a velocidade do jogador", BRANCO, LARGURA // 2, ALTURA // 2 + 80, 30)
        desenhar_texto("Pressione [4] para diminuir a velocidade do jogador", BRANCO, LARGURA // 2, ALTURA // 2 + 120, 30)
        desenhar_texto("Pressione [Enter] para começar o jogo", VERDE, LARGURA // 2, ALTURA - 50, 30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    VELOCIDADE_MAX_DISCO += 1
                elif evento.key == pygame.K_2:
                    VELOCIDADE_MAX_DISCO = max(1, VELOCIDADE_MAX_DISCO - 1)
                elif evento.key == pygame.K_3:
                    VELOCIDADE_MAX_JOGADOR += 1
                elif evento.key == pygame.K_4:
                    VELOCIDADE_MAX_JOGADOR = max(1, VELOCIDADE_MAX_JOGADOR - 1)
                elif evento.key == pygame.K_RETURN:
                    rodando = False

        pygame.display.update()

# Função principal do jogo
def jogo():
    disco = Disco(LARGURA // 2, ALTURA // 2, 3, 3, MASSA_DISCO)
    jogador1 = Jogador(100, ALTURA // 2, {"cima": pygame.K_w, "baixo": pygame.K_s, "esquerda": pygame.K_a, "direita": pygame.K_d}, MASSA_JOGADOR)
    jogador2 = Jogador(LARGURA - 100, ALTURA // 2, {"cima": pygame.K_UP, "baixo": pygame.K_DOWN, "esquerda": pygame.K_LEFT, "direita": pygame.K_RIGHT}, MASSA_JOGADOR)
    placar = [0, 0]

    rodando = True
    while rodando:
        TELA.fill(PRETO)
        pygame.draw.rect(TELA, BRANCO, GOL_ESQUERDA)
        pygame.draw.rect(TELA, BRANCO, GOL_DIREITA)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        disco.mover()
        disco.colisao_parede()
        disco.colisao_jogador(jogador1)
        disco.colisao_jogador(jogador2)

        velocidade_dis = math.sqrt(disco.velocidade_x**2 + disco.velocidade_y**2)
        if disco.x <= 0:
            placar[1] += 1
            disco = Disco(LARGURA // 2, ALTURA // 2, 3, 3, MASSA_DISCO)
        elif disco.x >= LARGURA:
            placar[0] += 1
            disco = Disco(LARGURA // 2, ALTURA // 2, -3, -3, MASSA_DISCO)

        jogador1.mover()
        jogador2.mover()

        disco.desenhar()
        jogador1.desenhar()
        jogador2.desenhar()

        desenhar_tabela(placar, velocidade_dis)
        pygame.display.update()
        pygame.time.Clock().tick(60)

    pygame.quit()

# Execução do menu e do jogo
menu_principal()
jogo()
