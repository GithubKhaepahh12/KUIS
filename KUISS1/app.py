from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route('/api/v1/bmi', methods=['POST'])
def bmi():
    height = float(request.form.get('height'))
    weight = float(request.form.get('weight'))
    BMI = weight / (height/100)**2
    msg = "BMI Anda adalah " + str(BMI)
    if BMI <= 18.4:
        ket = "Berat Anda Kurus."
    elif BMI <= 25:
        ket = "Berat Anda Normal."
    elif BMI <= 40:
        ket = "Berat Anda Berlebih."
    else:
        ket = "Berat Anda Dangerous."
    data = {'result': 'true', 'msg': msg, 'ket': ket}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=False, port=8080)