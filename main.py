from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Bloco 1: Tio Sam
tio_sam_cidades = [
    "Açaí", "Bady Bassitt", "Cravinhos", "Cubatão", "Franca", "Indaiatuba", "Itapetininga", "Itu",
    "Itupeva", "Leme", "Limeira", "Lins", "Mirassol", "Mogi Guaçu", "Mogi Mirim", "Peruíbe",
    "Pirassununga", "Porto Ferreira", "Salto", "São José do Rio Preto", "Artur Nogueira", "Cosmópolis",
    "Estiva Gerbi", "Tambaú", "Santa Rita do Passa Quatro", "Santa Cruz das Palmeiras",
    "Casa Branca", "Cedral"
]

# Bloco 2: Barretos
barretos_cidades = [
    "Barretos", "Bebedouro", "Olímpia"
]

# Bloco 3: Cidades gerais
cidades_gerais = [
    "Açaí", "Águas de Santa Bárbara", "Alumínio", "Americana", "Américo Brasiliense", "Amparo",
    "Araçoiaba da Serra", "Araçariguama", "Araras", "Artur Nogueira", "Atibaia", "Bady Bassitt", "Barretos",
    "Bebedouro", "Birigui", "Biritaba-Mirim", "Boa Esperança do Sul", "Bom Jesus dos Perdões", "Borboema",
    "Bragança Paulista", "Cabreúva", "Caçapava", "Caieiras", "Campinas", "Campo Limpo Paulista",
    "Cândido Rodrigues", "Capivari", "Casa Branca", "Cedral", "Colina", "Conchal", "Cordeirópolis",
    "Cosmópolis", "Cravinhos", "Cubatão", "Descalvado", "Diadema", "Espírito Santo do Pinhal",
    "Estiva Gerbi", "Fernandópolis", "Franca", "Hortolândia", "Ibaté", "Ibirá", "Ibitinga", "Indaiatuba",
    "Itapecerica da Serra", "Itapetininga", "Itapeva", "Itatiba", "Itu", "Ituverava", "Jaboticabal",
    "Jacareí", "Jaguariúna", "Jales", "Jandira", "Jarinu", "Jaú", "Jundiaí", "Lençóis Paulista", "Leme",
    "Limeira", "Lins", "Lorena", "Mairinque", "Marília", "Matão", "Mococa", "Mogi Guaçu", "Mogi Mirim",
    "Monte Alto", "Monte Azul Paulista", "Monte Mor", "Nova Odessa", "Olímpia", "Orlândia", "Osasco",
    "Ourinhos", "Paulínia", "Penápolis", "Pereira Barreto", "Peruíbe", "Pindamonhangaba", "Piracicaba",
    "Pirassununga", "Porto Ferreira", "Praia Grande", "Ribeirão Preto", "Rio Claro", "Rio das Pedras",
    "Salto", "Santa Bárbara d'Oeste", "Santa Cruz das Palmeiras", "Santa Rita do Passa Quatro",
    "Santo André", "Santos", "São Bernardo do Campo", "São Caetano do Sul", "São Carlos", "São José do Rio Preto",
    "São José dos Campos", "São Paulo", "Sertãozinho", "Sorocaba", "Sumaré", "Suzano", "Taboão da Serra",
    "Tambaú", "Taquaritinga", "Taubaté", "Tietê", "Valinhos", "Vinhedo", "Votorantim", "Votuporanga"
]

@app.route('/verificar-cidade')
def verificar_cidade():
    nome_cidade = request.args.get('nome')

    if not nome_cidade:
        return app.response_class(
            response=json.dumps({"erro": "Parâmetro 'nome' é obrigatório"}, ensure_ascii=False),
            mimetype='application/json'
        ), 400

    cidade_formatada = nome_cidade.strip().title()

    if cidade_formatada in tio_sam_cidades:
        return app.response_class(
            response=json.dumps({"atendida": True, "cidade": cidade_formatada, "grupo": "Tio Sam"}, ensure_ascii=False),
            mimetype='application/json'
        )

    if cidade_formatada in barretos_cidades:
        return app.response_class(
            response=json.dumps({"atendida": True, "cidade": cidade_formatada, "grupo": "Barretos"}, ensure_ascii=False),
            mimetype='application/json'
        )

    if cidade_formatada in cidades_gerais:
        return app.response_class(
            response=json.dumps({"atendida": True, "cidade": cidade_formatada, "grupo": "Padrão"}, ensure_ascii=False),
            mimetype='application/json'
        )

    return app.response_class(
        response=json.dumps({"atendida": False, "cidade": cidade_formatada, "grupo": None}, ensure_ascii=False),
        mimetype='application/json'
    )
