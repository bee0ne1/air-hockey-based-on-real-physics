# SIMULAÇÃO
descontinuado: implementation of the air hockey game based on real physical collisions between objects, using real mathematical models to show how physics can be fun. project implemented in python using mainly the pygame library, made for a college assignment in physics

OBS:
COMO PROSSEGUIR:
  - fazer com que o tamanho da parede de colisão mude com o tamanho da janela aberta
  - fazer o menu de configurações
  - documentar o código
  - fazer o read-me do código explicando toda a fisica envolvida
  - colocar no padrão de implementação desejado pela monitora
# SIMULAÇÃO
descontinuado: implementation of the air hockey game based on real physical collisions between objects, using real mathematical models to show how physics can be fun. project implemented in python using mainly the pygame library, made for a college assignment in physics

OBS:
COMO PROSSEGUIR:
  - fazer com que o tamanho da parede de colisão mude com o tamanho da janela aberta
  - fazer o menu de configurações
  - documentar o código
  - fazer o read-me do código explicando toda a fisica envolvida
  - colocar no padrão de implementação desejado pela monitora

JOGO SIMULAÇÃO DE COLISÃO ELÁSTICA
Criamos um jogo simulação bidimensional onde é possivel visualizar corpos, representados por bolas, se colidindo de forma elástica,
onde a energia cinética e o momento linear total do sistema se conservam e os corpos envolvidos não sofrem deformações permanentes 
durante o impacto. Ou seja, após o encontro entre os corpos, a direção, o sentido e o módulo da velocidade é afetado, porém a massa não se altera.
OBSERVAÇÃO: A parede, ou seja, as bordas da tela, não são consideradas para a colisão e servem apenas para redirecionar o vetor do corpo

MANUAL DE INSTRUÇÕES PARA O JOGO:
  Após executar o código, será aberto uma janela pygame onde o usuário se deparará com um menu contendo 3 opções:
  (imagem contendo o menu principal)
  INICIAR: inicia o jogo pressionando a tecla enter, caso o usuário não mexa em nenhuma configuração, o jogo iniciará com o número
  de corpos e suas respectivas massas e velocidades geradas aleatoriamente.
  (imagem contendo o jogo rodando)
  CONFIGURAR: abre o menu de configurações pressionando a tecla C. navegando por ele através das teclas direcionais (arrow keys) é possivel:
  determinar o intervalo de massa mínima (1) e máxima (2) dos corpos no jogo; Determinar o intervalo de velocidade mínima (3) e máxima (4) dos corpos, e o número de corpos (5). 
  (imagem contendo as configurações)
  Pressionando ESC, o usuário retorna ao menu inicial.
  SAIR: pressiona a tecla ESC para fechar o programa, (inclusive na tela do jogo).
  OBSERVAÇÃO: conforme o usuário expande e contrai a janela do jogo, as paredes que fecham a área do jogo seguem o padrão e adaptam seu comprimento. 
  (colocar duas imagens de tamanho diferente para exemplificar essa parte visual do jogo)

  CONCEITO DE FISICA E MODELO MATEMÁTICO
    Conceito Principal: Colisão Elástica
    Modelo Matemático: (colocar a fórmula da colisao elastica explicando oq é cada coisa)
    Aplicabilidade: O jogo simula como corpos de diferentes massas e velocidades reagem a impactos entre si, essa aplicação pode ser usada
    em testes mais simples da física pois forças externas como por exemplo força de atrito, resistência do ar, gravidade, não são consideradas.

  IMPLEMENTAÇÃO:
  Linguagens e Pacotes:
  O projeto foi implementado em Python utilizando os pacotes pygame, sys, random e math. Cada um desses pacotes oferece ferramentas específicas para lidar com visualização, computação científica, interações físicas, aleatoriedade, permitindo que a simulação seja interativa e visualmente intuitiva.
  
Como Usar
Instalação e Dependências:

Certifique-se de que o Python 3.6+ (ou outra versão de linguagem) está instalado.

Dependências incluem: Math, PyGame, Random.

Instale os pacotes necessários executando:
pip install -r requirements.txt
Exemplos de Uso:

Para rodar a simulação básica, utilize o código:
(nome do arquivo).py e execute o terminal

Informações sobre o projeto:

Esste projeto foi desenvolvido por:
(nome dos alunos): email dos alunos

Como parte do processo avaliativo da disciplina 7600105 - Física Básica I (2024) da USP-São Carlos ministrada pela(o) [Prof. Krissia de Zawadzki/Esmerindo de Sousa Bernardes]
