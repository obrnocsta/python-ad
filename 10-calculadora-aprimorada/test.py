from calculadora_aprimorada import somarmultiplosnumeros, multiplicarmultiplosnumeros, ehpar, ehinteiro

# Teste 1 - soma de vários números inteiros positivos
def test_adicionar_múltiplos_inteiros_positivos():
    assert somarmultiplosnumeros([1, 2, 3, 4]) == 10


# Teste 2 - soma de vários números "complexos" (decimais e negativos)
def test_somar_múltiplos_números_complexos():
    assert somarmultiplosnumeros([1.5, -2, 3.25]) == 2.75


# Teste 3 - multiplicação de vários números inteiros positivos
def test_multiplicar_múltiplos_inteiros_positivos():
    assert multiplicarmultiplosnumeros([2, 3, 4]) == 24


# Teste 4 - multiplicação de vários números "complexos" (decimais e negativos)
def test_multiplicar_múltiplos_números_complexos():
    assert multiplicarmultiplosnumeros([1.5, -2, 4]) == -12


# Teste 5 - 6 é par?
def test_é_seis_par():
    assert ehpar(6) == True


# Teste 6 - -3.8 é par? (número decimal nunca é par)
def test_é_menos_três_ponto_oito_par():
    assert ehpar(-3.8) == False


# Teste 7 - 3 é um número inteiro?
def test_três_é_um_inteiro():
    assert ehinteiro(3) == True


# Teste 8 - 7.3 é um número inteiro?
def test_sete_ponto_três_é_um_inteiro():
    assert ehinteiro(7.3) == False