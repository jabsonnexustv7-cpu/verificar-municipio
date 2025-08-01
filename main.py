from flask import Flask, request
import json

app = Flask(__name__)

# Bloco 1: Tio Sam
tio_sam_cidades = [
    "Aguaí", "Baby Bassitt", "Cravinhos", "Cubatão", "Franca", "Indaiatuba", "Itapetininga", "Itu",
    "Itupeva", "Leme", "Limeira", "Lins", "Mirassol", "Mogi Guaçu", "Mogi Mirim", "Peruibe", "Pirassununga",
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
    "Araçoiaguma", "Araçariguama", "Araras", "Artur Nogueira", "Atibaia", "Baby Bassitt", "Barretos",
    "Bebedouro", "Biritiba-Mirim", "Boa Esperança do Sul", "Bom Jesus dos Perdões", "Borboeama",
    "Bragança Paulista", "Cabreúva", "Caçapava", "Caieiras", "Campinas", "Campo Limpo Paulista",
    "Cândido Rodrigues", "Capivari", "Casa Branca", "Cedral", "Colina", "Conchal", "Cordeirópolis",
    "Coroados", "Cravinhos", "Cubatão", "Descalvado", "Diadema", "Dois Córregos", "Elias Fausto", "Embu",
    "Espírito Santo do Pinhal", "Estiva Gerbi", "Fernandópolis", "Franca", "Guaratinguetá", "Guariba",
    "Guarulhos", "Hortolândia", "Ilha Solteira", "Indaiatuba", "Itapecerica da Serra", "Itapetininga",
    "Itapeva", "Itatiba", "Itatiba", "Itu", "Itupeva", "Jaboticabal", "Jaguariúna", "Jales", "Jarinu",
    "Joanópolis", "Jundiaí", "Leme", "Limeira", "Lins", "Lorena", "Marília", "Matão", "Mauá",
    "Miguelópolis", "Mirassol", "Mococa", "Mogi das Cruzes", "Mogi Guaçu", "Mogi Mirim", "Monte Alto",
    "Monte Aprazível", "Monte Azul Paulista", "Nova Odessa", "Olímpia", "Orlândia", "Osasco", "Paulínia",
    "Pedreira", "Peruíbe", "Pindamonhangaba", "Piracicaba", "Pirassununga", "Poá", "Porto Ferreira",
    "Presidente Prudente", "Ribeirão Pires", "Ribeirão Preto", "Rio Claro", "Salto", "Santa Bárbara d'Oeste",
    "Santa Cruz das Palmeiras", "Santa Rita do Passa Quatro", "Santo André", "Santos", "São Bernardo do Campo",
    "São Carlos", "São João da Boa Vista", "São José do Rio Preto", "São José dos Campos", "São Paulo",
    "São Pedro", "Sertãozinho", "Sumaré", "Suzano", "Taboão da Serra", "Tambaú", "Taquaritinga", "Taubaté",
    "Tietê", "Valinhos", "Vargem Grande do Sul", "Várzea Paulista", "Votorantim", "Votuporanga"
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
