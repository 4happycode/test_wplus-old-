from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

# Kunci API IQAir Anda
API_KEY = 'de4931a4-f8d6-4e16-a17d-c03a2ebf4c51'


@app.route('/get_air_quality', methods=['GET'])
def get_air_quality():
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')

    # Lakukan permintaan ke API IQAir dengan menggunakan kunci API Anda
    url = f'http://api.airvisual.com/v2/nearest_city?lat={latitude}&lon={longitude}&key={API_KEY}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            air_quality_data = response.json()
            return jsonify(air_quality_data)
        else:
            return jsonify({'error': 'Gagal mengambil data kualitas udara dari IQAir API'}), 500
    except Exception as e:
        return jsonify({'error': 'Terjadi kesalahan saat mengambil data kualitas udara: ' + str(e)}), 500


@app.route("/", methods=["GET"])
def index():
    return render_template("dashboard.html")


if __name__ == '__main__':
    app.run(debug=True)
