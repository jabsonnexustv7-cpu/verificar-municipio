from flask import Flask, request, jsonify

app = Flask(__name__)

# Bloco 1: Tio Sam
tio_sam_cidades = [
    "Aguaí", "Bady Bassitt", "Cravinhos", "Cubatão", "Franca", "Indaiatuba", "Itapetininga", "Itú",
    "Itupeva", "Leme", "Limeira", "Lins", "Mirassol", "Mogi Guaçu", "Mogi Mirim", "Peruíbe", "Pirassununga",
    "Porto Ferreira", "Salto", "São José do Rio Preto", "Artur Nogueira", "Cosmópolis", "Estiva Gerbi",
    "Tambaú", "Santa Rita do Passa Quatro", "Santa Cruz das Palmeiras", "Casa Branca", "Cedral"
]

# Bloco 2: Barretos
barretos_cidades = [
    "Barretos", "Bebedouro", "Olímpia"
]

# Bloco 3: Cidades gerais
cidades_gerais = [
    "Aguaí", "Águas de Santa Bárbara", "Alumínio", "Americana", "Américo Brasiliense", "Amparo",
    "Araçariguama", "Araraquara", "Araras", "Artur Nogueira", "Atibaia", "Bady Bassitt", "Barretos",
    "Bebedouro", "Biritiba-Mirim", "Boa Esperança do Sul", "Bom Jesus dos Perdões", "Borborema",
    "Bragança Paulista", "Cabreúva", "Caçapava", "Caieiras", "Campinas", "Campo Limpo Paulista",
    "Cândido Rodrigues", "Capivari", "Casa Branca", "Cedral", "Colina", "Conchal", "Cordeirópolis",
    "Cosmópolis", "Cravinhos", "Cristais Paulista", "Cubatão", "Descalvado", "Dobrada", "Engenheiro Coelho",
    "Estiva Gerbi", "Fernando Prestes", "Franca", "Francisco Morato", "Franco da Rocha", "Gavião Peixoto",
    "Guaíra", "Guapiçu", "Guararema", "Guariba", "Guarujá", "Guatapará", "Holambra", "Hortolândia",
    "Ibaté", "Ibitinga", "Igaratá", "Indaiatuba", "Iracemápolis", "Itajobi", "Itaju", "Itanhaém", "Itápolis",
    "Itirapúã", "Itupeva", "Jaborandi", "Jaboticabal", "Jacareí", "Jaguariúna", "Jarinu", "Jundiaí", "Leme",
    "Limeira", "Lindóia", "Louveira", "Mairiporã", "Matão", "Mirassol", "Mogi das Cruzes", "Mogi Guaçu",
    "Mogi Mirim", "Mongaguá", "Monte Alto", "Monte Mor", "Motuca", "Nazaré Paulista", "Nova Europa",
    "Nova Odessa", "Olímpia", "Patrocínio Paulista", "Paulínia", "Pedreira", "Peruíbe", "Pindorama",
    "Piracaia", "Piracicaba", "Pirajuí", "Pirassununga", "Pitangueiras", "Porto Ferreira", "Praia Grande",
    "Rafard", "Ribeirão Bonito", "Ribeirão Corrente", "Ribeirão Preto", "Rincão", "Salesópolis",
    "Santa Adélia", "Santa Bárbara d'Oeste", "Santa Branca", "Santa Cruz das Palmeiras", "Santa Ernestina",
    "Santa Gertrudes", "Santa Lúcia", "Santa Rita do Passa Quatro", "Santa Rosa de Viterbo",
    "Santo Antônio de Posse", "Santos", "São Bernardo do Campo", "São Carlos", "São José do Rio Preto",
    "São José dos Campos", "São Vicente", "Serra Azul", "Serra Negra", "Sorocaba", "Sumaré", "Tabatinga",
    "Tambaú", "Taquaritinga", "Taubaté", "Trabiju", "Tremembé", "Uchoa", "Valinhos", "Várzea Paulista",
    "Vinhedo", "Votorantim"
]

@app.route('/verificar-cidade')
def verificar_cidade():
    nome_cidade = request.args.get('nome')
    
    if not nome_cidade:
        return jsonify({"erro": "Parâmetro 'nome' é obrigatório"}), 400

    cidade_formatada = nome_cidade.strip().title()

    if cidade_formatada in tio_sam_cidades:
        return jsonify({"atendida": True, "cidade": cidade_formatada, "grupo": "Tio Sam"})

    if cidade_formatada in barretos_cidades:
        return jsonify({"atendida": True, "cidade": cidade_formatada, "grupo": "Barretos"})

    if cidade_formatada in cidades_gerais:
        return jsonify({"atendida": True, "cidade": cidade_formatada, "grupo": "Padrão"})

    return jsonify({"atendida": False, "cidade": cidade_formatada, "grupo": None})
