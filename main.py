import pygame
import random

# Inicializa o Pygame
pygame.init()

# Define as cores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Define a largura e altura da tela
LARGURA = 600
ALTURA = 600

# Função para criar a matriz
def criar_matriz(tamanho):
    return [[' ' for _ in range(tamanho)] for _ in range(tamanho)]

# Função para sortear a posição do peixe
def sortear_peixe(tamanho):
    return random.randint(0, tamanho - 1), random.randint(0, tamanho - 1)

# Função para exibir a matriz
def exibir_matriz(screen, matriz, tamanho, font):
    cell_size = LARGURA // tamanho
    for i in range(tamanho):
        for j in range(tamanho):
            pygame.draw.rect(screen, WHITE, (j * cell_size, i * cell_size, cell_size, cell_size))
            pygame.draw.rect(screen, BLACK, (j * cell_size, i * cell_size, cell_size, cell_size), 2)
            texto = font.render(matriz[i][j], True, BLACK)
            screen.blit(texto, (j * cell_size + cell_size // 3, i * cell_size + cell_size // 3))

# Função para o jogo de pescaria
def jogar(tamanho, rodadas, tentativas_por_rodada):
    screen = pygame.display.set_mode((LARGURA, ALTURA))
    pygame.display.set_caption("Jogo de Pescaria")

    font = pygame.font.Font(None, 36)

    matriz_jogador = criar_matriz(tamanho)
    matriz_computador = criar_matriz(tamanho)
    peixe_computador = sortear_peixe(tamanho)
    peixe_jogador = sortear_peixe(tamanho)

    peixes_jogador = 0
    peixes_computador = 0

    clock = pygame.time.Clock()
    jogo_rodando = True

    while jogo_rodando:
        screen.fill(GREEN)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogo_rodando = False

        # Exibe a matriz do jogador
        exibir_matriz(screen, matriz_jogador, tamanho, font)

        pygame.display.flip()

        # Jogador
        for rodada in range(rodadas):
            for tentativa in range(tentativas_por_rodada):
                print(f"\nRodada {rodada + 1} de {rodadas}")
                print(f"Tentativa {tentativa + 1} de {tentativas_por_rodada}")
                while True:
                    print(f"Você, tentativa {tentativa + 1} de {tentativas_por_rodada}")
                    pos = input(f"Escolha uma posição para pescar (linha entre 0 e {tamanho-1}): ")
                    try:
                        pos = int(pos)
                        if pos < 0 or pos >= tamanho:
                            print(f"Posição inválida. Tente um número entre 0 e {tamanho-1}.")
                        elif matriz_jogador[pos][0] != ' ':
                            print("Espaço já ocupado! Escolha outra posição.")
                        else:
                            matriz_jogador[pos][0] = 'X'  # Marca o espaço escolhido
                            break
                    except ValueError:
                        print("Entrada inválida. Digite um número válido.")

                if (pos, 0) == peixe_jogador:
                    peixes_jogador += 1

        pygame.quit()

# Função principal
def main():
    tamanho = int(input("Escolha o tamanho da matriz (ex: 5 para uma matriz 5x5): "))
    rodadas = int(input("Número de rodadas: "))
    tentativas_por_rodada = int(input("Tentativas por rodada: "))
    jogar(tamanho, rodadas, tentativas_por_rodada)

if __name__ == "__main__":
    main()
