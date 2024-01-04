contatos = {"leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "leticiamilan.dev@gmail.com", {}
)  # {"leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"}
print(resultado)