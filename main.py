from flask import Flask, request, jsonify

app = Flask(__name__)

# Bloco 1: Tio Sam
tio_sam_cidades = [
    "Aguaí", "Bady Bassitt", "Cravinhos", "Cubatão", "Franca", "Indaiatuba", "Itapetininga", "Itu",
    "Itupeva", "Leme", "Limeira", "Lins", "Mirassol", "Mogi Guaçu", "Mogi Mirim", "Peruíbe",
    "Pirassununga", "Porto Ferreira", "Salto", "São José do Rio Preto", "Artur Nogueira", "Cosmópolis",
    "Estiva Gerbi", "Tambaú", "Santa Rita do Passa Quatro", "Santa Cruz das Palmeiras", "Casa Branca", "Cedral"
]

# Bloco 2: Barretos
barretos_cidades = [
    "Barretos", "Bebedouro", "Olímpia"
]

# Bloco 3: Cidades gerais
cidades_gerais = [
    "Aguaí", "Águas de Santa Bárbara", "Alumínio", "Americana", "Américo Brasiliense", "Amparo",
    "Araçariguama", "Araçoiaba", "Araras", "Artur Nogueira", "Atibaia", "Bady Bassitt", "Barretos",
    "Bebedouro", "Birigui", "Biritiba-Mirim", "Boa Esperança do Sul", "Bom Jesus dos Perdões", "Borborema",
    "Bragança Paulista", "Cabreúva", "Caçapava", "Caieiras", "Campinas", "Campo Limpo Paulista",
    "Cândido Rodrigues", "Capivari", "Casa Branca", "Cedral", "Colina", "Conchal", "Cordeirópolis",
    "Cosmópolis", "Cravinhos", "Cubatão", "Descalvado", "Dracena", "Elias Fausto", "Embu-Guaçu",
    "Estiva Gerbi", "Fernandópolis", "Franca", "Francisco Morato", "Guaíra", "Guariba", "Guarujá",
    "Guarulhos", "Hortolândia", "Indaiatuba", "Ipeúna", "Itapecerica da Serra", "Itapetininga",
    "Itapevi", "Itatiba", "Itu", "Itupeva", "Jaguariúna", "Jales", "Jandira", "Jardinópolis",
    "Jarinu", "Jaú", "Joanópolis", "Jundiaí", "Leme", "Limeira", "Lins", "Mauá", "Miguelópolis",
    "Mirassol", "Mogi Guaçu", "Mogi Mirim", "Monte Alto", "Monte Azul Paulista", "Monte Mor",
    "Nova Odessa", "Olímpia", "Orlândia", "Osasco", "Paulínia", "Penápolis", "Peruíbe",
    "Pindamonhangaba", "Piracicaba", "Pirassununga", "Pitangueiras", "Pontal", "Porto Ferreira",
    "Praia Grande", "Ribeirão Preto", "Rio Claro", "Rio das Pedras", "Salto", "Santa Bárbara d'Oeste",
    "Santa Cruz das Palmeiras", "Santa Rita do Passa Quatro", "Santo André", "Santos", "São Bernardo do Campo",
    "São Caetano do Sul", "São Carlos", "São José do Rio Preto", "São José dos Campos", "São Paulo",
    "Sertãozinho", "Sorocaba", "Sumaré", "Suzano", "Tabapuã", "Tabatinga", "Tambaú", "Taquaritinga",
    "Taubaté", "Tatuí", "Valinhos", "Vargem Grande do Sul", "Várzea Paulista", "Vinhedo", "Votorantim"
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
