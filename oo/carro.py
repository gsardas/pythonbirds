"""
Voce deve criar uma classe carro que vai possuir
dois atributos compostos por outras classes:

1) Motor
2) Direcao

O motor tera a responsabilidade de controlar a velicidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Metodo acelerar, que devera incrementar a velocidade de uma unidade
3) Metodo frear que devera decrementar a velocidade em duas unidades

A direcao terá a responsabilidade de controlar a direcao. Ela oferece
os seguintes atributos:
1) Valor de direcao com valores possiveis: Norte, Sul, Leste e Oeste
2) Metodo girar a direita
3) Metodo girar a esquerda

   N
 O   L
   S

    Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0










"""