from bs4 import BeautifulSoup

# Lista de obras 
obras = {
    "Red Dead Redemption 2": "https://image.api.playstation.com/cdn/UP1004/CUSA03041_00/Hpl5MtwQgOVF9vJqlfui6SDB5Jl4oBSq.png",
    "Star Wars: Original trilogy & Clone Wars": "https://i.redd.it/4kdml4fo1fa81.jpg",
    "The Lord of the Rings Trilogy": "https://m.media-amazon.com/images/I/71O5tRLd3fL._AC_UF894,1000_QL80_.jpg",
    
    
}

# Criar uma string HTML
html_content = "<!DOCTYPE html><html><head><title>Lista de Obras</title></head><body>"

# Adicionar cada obra com sua imagem e link
for obra, link in obras.items():
    html_content += f"<div><img src='{link}' alt='{obra}' width='200'><br>{obra}</div>"

# Fechar a tag HTML
html_content += "</body></html>"

# Salvar o conteúdo HTML em um arquivo
with open("lista_obras.html", "w") as file:
    file.write(html_content)

print("Arquivo HTML gerado com sucesso!")