from flask import Flask, jsonify, request

data = [{'Name': '2MASSW J0045214+163445', 'Radius': '115817394.942', 'Mass': '4.3669537236e+28', 'Gravity': '217.1485027627916', 'Distance': '57.0'}, 
        {'Name': 'WISEP J004701.06+680352.1Ãƒâ€šÃ‚Â\xa0[fr]', 'Radius': '92939884.82999994', 'Mass': '2.2784106384e+28', 'Gravity': '175.93553814787887', 'Distance': '40.0'}, 
        {'Name': '2MASS J03264225-2102057Ãƒâ€šÃ‚Â\xa0[de]', 'Radius': '92939884.82999994', 'Mass': '3.4176159576e+28', 'Gravity': '263.90330722181835', 'Distance': '80.0'}, 
        {'Name': '2MASS J03552337+1133437', 'Radius': '94369729.212', 'Mass': '3.797351064e+28', 'Gravity': '284.407579076671', 'Distance': '29.8'}, 
        {'Name': '2MASS J04433764+0002040', 'Radius': '127256149.99799992', 'Mass': '4.1770861704e+28', 'Gravity': '172.04486250521128', 'Distance': '82.0'}, 
        {'Name': '2MASS J05012406-0010452Ãƒâ€šÃ‚Â\xa0[de]', 'Radius': '98659262.35799992', 'Mass': '3.987218617199999e+28', 'Gravity': '273.2248236044696', 'Distance': '64.0'}, 
        {'Name': 'LSR 0602+3910Ãƒâ€šÃ‚Â\xa0[de]', 'Radius': '100804028.93099992', 'Mass': '5.3162914896e+28', 'Gravity': '348.96256329986886', 'Distance': '34.6'}, 
        {'Name': '2MASS J10224821+5825453Ãƒâ€šÃ‚Â\xa0[de]', 'Radius': '100804028.93099992', 'Mass': '5.1264239364e+28', 'Gravity': '336.49961461058786', 'Distance': '60.0'}, 
        {'Name': 'DENIS-P J142527.97-365023.4Ãƒâ€šÃ‚Â\xa0[de]', 'Radius': '94369729.212', 'Mass': '3.987218617199999e+28', 'Gravity': '298.6279580305045', 'Distance': '38.0'}, 
        {'Name': '2MASSW J2206450-421721', 'Radius': '95084651.403', 'Mass': '4.1770861704e+28', 'Gravity': '308.16153675250763', 'Distance': '93.0'}, 
        {'Name': '2MASSW J2244316+204343', 'Radius': '92224962.63899992', 'Mass': '2.2784106384e+28', 'Gravity': '178.67379332366767', 'Distance': '56.0'}, 
        {'Name': '2MASS J23224684-3133231', 'Radius': '99374184.54899992', 'Mass': '4.5568212768e+28', 'Gravity': '307.7801971636203', 'Distance': '56.0'}, 
        {'Name': 'Sun', 'Radius': '695700000.0', 'Mass': '1.989e+30', 'Gravity': '274.10478078144416', 'Distance': '1.5813e-05'}, 
        {'Name': 'Sirius', 'Radius': '1189647000.0', 'Mass': '4.176900000000001e+30', 'Gravity': '196.8537463291381', 'Distance': '8.6'}, 
        {'Name': 'Alpha Centauri', 'Radius': '834840000.0', 'Mass': '2.1879e+30', 'Gravity': '209.38559643026983', 'Distance': '4.4'}, 
        {'Name': 'Altair', 'Radius': '1252260000.0', 'Mass': '3.5802e+30', 'Gravity': '152.280433767469', 'Distance': '17.0'}, 
        {'Name': 'Fomalhaut', 'Radius': '1252260000.0', 'Mass': '3.7791e+30', 'Gravity': '160.7404578656617', 'Distance': '25.0'}, 
        {'Name': 'Tau Ceti', 'Radius': '621260100.0', 'Mass': '1.557387e+30', 'Gravity': '269.1382688446168', 'Distance': '11.9'}, 
        {'Name': 'Delta Pavonis', 'Radius': '848754000.0', 'Mass': '1.971099e+30', 'Gravity': '182.5032503053017', 'Distance': '19.92'}, 
        {'Name': 'Titawin', 'Radius': '1029636000.0', 'Mass': '2.5260300000000002e+30', 'Gravity': '158.9267127430762', 'Distance': '44.25'}, 
        {'Name': '54 Piscium', 'Radius': '653958000.0', 'Mass': '1.5116400000000002e+30', 'Gravity': '235.7623736915997', 'Distance': '36.1'}]

App = Flask(__name__)

@App.route('/')

def index():
    return jsonify({
        "data": data,
        "message": "success"
    })

@App.route('/planet')

def get_names():
    name = request.args.get('name')
    planet_data =  next(item for item in data if item["Name"] == name)

    return jsonify({
        "data" : planet_data,
        "message" : "success"
    }), 200

if __name__ == '__main__':
    App.run()