# ALGORITMO EFICIENTE PARA ENCONTRAR A SUBSEQUÊNCIA PALINDRÔMICA MAIS LONGA (SPML)

def preencher_tabela(s, i, j, tabela):

    # Caso base: 1 caractere
    if i == j:
        return 1

    # Caso base: 2 caracteres iguais
    if s[i] == s[j] and i + 1 == j:
        return 2

    # Se ja foi calculado, retorna da tabela
    if tabela[i][j] != -1:
        return tabela[i][j]

    # Se o primeiro e ultimo caractere são iguais
    if s[i] == s[j]:
        tabela[i][j] = preencher_tabela(s, i + 1, j - 1, tabela) + 2
        return tabela[i][j]

    # Se eles não são iguais, calcula o maximo
    tabela[i][j] = max(preencher_tabela(s, i, j - 1, tabela), 
                       preencher_tabela(s, i + 1, j, tabela))
    return tabela[i][j]


def reconstruir_SPML_via_tabela(s, tabela, i, j):

    if i > j:
        return ""

    # Só um caractere
    if i == j:
        return s[i]

    # Se as extremidades forem iguais, elas fazem parte da subsequencia
    if s[i] == s[j]:
        return s[i] + reconstruir_SPML_via_tabela(s, tabela, i+1, j-1) + s[j]
    else:
        # Se nao forem iguais, seguimos o caminho que deu o valor maior em tabela
        if tabela[i][j-1] > tabela[i+1][j]:
            return reconstruir_SPML_via_tabela(s, tabela, i, j-1)
        else:
            return reconstruir_SPML_via_tabela(s, tabela, i+1, j)


if __name__ == "__main__":
    s = "BDASAEAADEEB"
    n = len(s)
    tabela = [[-1 for _ in range(n)] for _ in range(n)]
    preencher_tabela(s, 0, n - 1, tabela)
    subsequencia = reconstruir_SPML_via_tabela(s, tabela, 0, n - 1)
    print(f"A subsequência palíndrômica mais longa para '{s}' é '{subsequencia}'")
