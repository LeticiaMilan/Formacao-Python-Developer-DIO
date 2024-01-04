contatos = {
    "leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"},
    "joaovitormine@gmail.com": {"nome": "João Vitor", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["leticiamilan.dev@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'leticiamilan.dev@gmail.com': {'nome': 'Leticia'}, 'joaovitormine@gmail.com': {'nome': 'João Vitor', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)