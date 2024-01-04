contatos = {
    "leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"},
    "joaovitormine@gmail.com": {"nome": "João Vitor", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Leticia', 'telefone': '3333-2221'}, {'nome': 'João Vitor', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)