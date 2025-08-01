
from flask import Flask, request, jsonify

app = Flask(__name__)

cidades_atendidas = [
    "Aguaí", "Águas de Santa Bárbara", "Alumínio", "Americana", "Américo Brasiliense", "Amparo",
    "Araçariguama", "Araraquara", "Araras", "Artur Nogueira", "Atibaia", "Bady Bassitt", "Barretos",
    "Bebedouro", "Biritiba-Mirim", "Boa Esperança do Sul", "Bom Jesus dos Perdões", "Borborema",
    "Bragança Paulista", "Cabreúva", "Caçapava", "Caieiras", "Campinas", "Campo Limpo Paulista",
    "Cândido Rodrigues", "Capivari", "Casa Branca", "Cedral", "Colina", "Conchal", "Cordeirópolis",
    "Cosmópolis", "Cravinhos", "Cristais Paulista", "Cubatão", "Descalvado", "Dobrada", "Engenheiro Coelho",
    "Estiva Gerbi", "Fernando Prestes", "Franca", "Francisco Morato", "Franco da Rocha", "Gavião Peixoto",
    "Guaíra", "Guapiaçu", "Guararema", "Guariba", "Guarujá", "Guatapará", "Holambra", "Hortolândia",
    "Ibaté", "Ibitinga", "Igaratá", "Indaiatuba", "Iracemápolis", "Itajobi", "Itaju", "Itanhaém", "Itápolis",
    "Itirapuã", "Itupeva", "Jaborandi", "Jaboticabal", "Jacareí", "Jaguariúna", "Jarinu", "Jundiaí", "Leme",
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

@app.route('/verificar-cidade', methods=['GET'])
def verificar_cidade():
    nome_cidade = request.args.get('nome', '').strip()
    resultado = nome_cidade in cidades_atendidas
    return jsonify({"cidade": nome_cidade, "atendida": resultado})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
