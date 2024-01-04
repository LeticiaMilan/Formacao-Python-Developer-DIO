contatos = {
    "leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"},
    "joaovitormine@gmail.com": {"nome": "João Vitor", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "leticiamilan.dev@gmail.com" in contatos  # True
print(resultado)

resultado = "melet@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["leticiamilan.dev@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["joaovitormine@gmail.com"]  # True
print(resultado)