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
    "Limeira", "Lins", "Lorena", "Louveira", "Mairinque", "Mairiporã", "Marília", "Matão", "Mococa",
    "Mogi das Cruzes", "Mogi Guaçu", "Mogi Mirim", "Mongaguá", "Monte Alto", "Monte Alegre do Sul",
    "Monte Azul Paulista", "Monte Mor", "Motuca", "Nazará Paulista", "Nova Europa", "Nova Odessa", "Olímpia",
    "Orlândia", "Osasco", "Ourinhos", "Paranapanema", "Paulínia", "Penápolis", "Pereira Barreto", "Peruíbe",
    "Pindamonhangaba", "Pindorama", "Piracaia", "Piracicaba", "Pirassununga", "Piratininga", "Porto Ferreira",
    "Praia Grande", "Pratânia", "Quadra", "Rafard", "Ribeirão Bonito", "Ribeirão Corrente", "Ribeirão Preto",
    "Rio Claro", "Rio das Pedras", "Rincão", "Salto", "Saltinho", "Salto de Pirapora",
    "Santa Adélia", "Santa Bárbara d'Oeste", "Santa Branca", "Santa Cruz das Palmeiras", "Santa Ernestina",
    "Santa Gertrudes", "Santa Lúcia", "Santa Rita do Passa Quatro", "Santo André", "Santo Antônio de Posse",
    "Santos", "São Bernardo do Campo", "São Caetano do Sul", "São Carlos", "São José do Rio Preto",
    "São José dos Campos", "São Manuel", "São Vicente", "Sarapuí", "Sertãozinho", "Sorocaba",
    "Sumaré", "Suzano", "Tabatinga", "Taboão da Serra", "Tambaú", "Taquaritinga", "Taubaté", "Tatuí",
    "Tietê", "Tremembé", "Trabiju", "Valinhos", "Várzea Paulista", "Vinhedo", "Votorantim", "Votuporanga",
    "Guarujá", "Guariba", "Guararema", "Guatapará", "Iaras", "Igaratá", "Itaí", "Itajobi", "Itaju", "Itápolis",
    "Itapuí", "Itatinga", "Itupeva", "Jaborandi", "Laranjal Paulista", "Lindóia", "Patrocínio Paulista",
    "Pedreira", "Pereiras", "Pilar do Sul", "Porangaba", "Salesópolis", "São José do Rio Preto",
    "Vargem Grande Paulista", "Francisco Morato", "Franco da Rocha", "Dobrada", "Dois Córregos", "Dourado",
    "Fernando Prestes", "Bofete", "Botucatu", "Borborema", "Bocaina", "Areiópolis", "Avaré", "Agudos",
    "Barra Bonita", "Mirassol", "Mineiros do Tietê", "Capela do Alto", "Campina do Monte Alegre", "Angatuba",
    "Américo Brasiliense", "Araçoiaba da Serra", "Aguaí"
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
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render exige porta vinda da variável PORT
    app.run(host='0.0.0.0', port=port)
