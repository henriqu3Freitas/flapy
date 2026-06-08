def calcular_pontos(pontos_atual, pontos_ganhos):
    return pontos_atual + pontos_ganhos


def tomar_dano(vida_atual, dano):
    return vida_atual - dano


def jogador_perdeu(vidas):
    return vidas <= 0


def limitar_valor(valor, minimo, maximo):
    if valor < minimo:
        return minimo
    if valor > maximo:
        return maximo
    return valor


def verificar_colisao(retangulo_1, retangulo_2):
    return retangulo_1.colliderect(retangulo_2)