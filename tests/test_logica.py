from src.funcoes import calcular_pontos, jogador_perdeu, limitar_valor


def test_calcular_pontos():
    assert calcular_pontos(10, 5) == 15


def test_jogador_perdeu_com_zero_vidas():
    assert jogador_perdeu(0) is True


def test_jogador_nao_perdeu_com_vidas():
    assert jogador_perdeu(3) is False


def test_limitar_valor_abaixo_do_minimo():
    assert limitar_valor(-5, 0, 100) == 0


def test_limitar_valor_acima_do_maximo():
    assert limitar_valor(150, 0, 100) == 100


def test_limitar_valor_dentro_do_intervalo():
    assert limitar_valor(50, 0, 100) == 50