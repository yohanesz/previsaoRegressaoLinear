from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import pandas as pd 

app = Flask(__name__)
CORS(app)

modelo = joblib.load('modelo_nivel_rio.pkl')
scaler = joblib.load('scaler_nivel_rio.pkl')

@app.route('/')
def index():
    return 'API de Previsão do Nível do Rio'

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.get_json()

        entrada = [
            dados['NívelItuporanga'],
            dados['ChuvaItuporanga'],
            dados['NívelTaió'],
            dados['ChuvaTaió']
        ]

    
        entrada_df = pd.DataFrame([entrada], columns=['NívelItuporanga', 'ChuvaItuporanaga', 'NívelTaió', 'ChuvaTaió'])
        entrada_normalizada = scaler.transform(entrada_df)
        previsao_cm = modelo.predict(entrada_normalizada)[0]

        return jsonify({
            'previsao_nivel_rio': round(float(previsao_cm / 100), 2)
        })

    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
