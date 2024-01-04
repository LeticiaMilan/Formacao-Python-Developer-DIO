contatos = {"leticiamilan.dev@gmail.com": {"nome": "Leticia", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["leticiamilan.dev@gmail.com"] = {"nome": "Le"}

print(contatos["leticiamilan.dev@gmail.com"])  # {"nome": "Leticia", "telefone": "3333-2221"}

print(copia["leticiamilan.dev@gmail.com"])  # {"nome": "Le"}