from Token import Token

lista_tokens1 = []
lista_tokens1.append(Token(1, 'lexico', 'a'))
lista_tokens1.append(Token(2, 'lexico', 'b'))
lista_tokens1.append(Token(3, 'lexico', 'c'))

lista_tokens2 = []
lista_tokens2.append(Token(4, 'lexico', 'd'))
lista_tokens2.append(Token(5, 'lexico', 'e'))
lista_tokens2.append(Token(6, 'lexico', 'f'))

resultado = lista_tokens1 + lista_tokens2

for token in resultado:
    print(token.numero, token.tipo, token.lexema)