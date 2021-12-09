import requests, urllib.parse as ulp

origem = ["Abolição", "Alto da Boa Vista", "Anchieta", "Andaraí", "Anil", "Bancários", "Bangu", "Barra da Tijuca", "Barra de Guaratiba", "Barros Filho", "Belford Roxo", "Bento Ribeiro", "Bonsucesso", "Botafogo", "Brás de Pina", "Cachambi", "Cacuia", "Camorim", "Campo Grande", "Cancela Preta", "Cascadura", "Catete", "Centro (Bairro)", "Centro (Niterói)", "Cidade Nova", "Cocotá", "Copacabana", "Cosme Velho", "Cosmos", "Curicica", "Del Castilho", "Duque de Caxias", "Engenho da Rainha", "Engenho de Dentro", "Engenho Novo", "Estácio", "Flamengo", "Fonseca", "Freguesia de Jacarepaguá", "Gávea", "Glória", "Grajaú", "Guadalupe", "Humaitá", "Icaraí", "Ipanema", "Irajá", "Itaboraí", "Jacarepaguá", "Jardim Botânico", "Jardim Carioca", "Jardim Guanabara", "Jardim Sulacap", "Joá", "Lagoa", "Lapa", "Laranjeiras", "Leblon", "Leme", "Lins de Vasconcelos", "Madureira", "Magé", "Maracanã", "Marechal Hermes", "Maria Paula", "Méier", "Mesquita", "Monero", "Nilópolis", "Nova Iguaçu", "Oswaldo Cruz", "Paciência", "Pavuna", "Pechincha", "Penha", "Piedade", "Pilares", "Portuguesa", "Praça Seca", "Praia da Bandeira", "Quintino Bocaiuva", "Ramos", "Realengo", "Recreio dos Bandeirantes", "Região Oceânica (Niterói)", "Riachuelo", "Ribeira", "Rio Comprido", "Rocha", "Santa Cruz", "Santa Teresa", "São Conrado", "São Cristóvão", "São Francisco Xavier", "São Gonçalo", "São João de Meriti", "Saúde", "Taquara", "Tijuca", "Urca", "Vargem Pequena", "Vicente de Carvalho", "Vila da Penha", "Vila Isabel", "Vila Valqueire", "Vista Alegre", "Zona Zen", "Zumbi"]
destino = ['Cidade Universitária Rio de Janeiro', 'UFRJ - Campus Praia Vermelha', 'UFRJ Macaé']

f = open("bairros.tsv", "w")
f.write("Bairro de Origem\tBairro de Destino\tDistância total\tTempo de trajeto\n")
for o in origem:
  o = ulp.quote(o + " Rio de Janeiro")
  for d in destino:
    d = ulp.quote(d)
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={o}&destinations={d}&mode=driving&language=pt-BR&key=YOUR_API_KEY"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers = headers, data = payload)
    bairro_origem = response.json()["origin_addresses"][0]
    bairro_destino = response.json()["destination_addresses"][0]
    distancia = response.json()["rows"][0]["elements"][0]["distance"]["text"]
    tempo = response.json()["rows"][0]["elements"][0]["duration"]["text"]
    f.write(bairro_origem + "\t" + bairro_destino + "\t" + distancia + "\t" + tempo + "\n")

f.close()