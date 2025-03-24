from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/rankings', methods=['GET'])
def get_rankings():
    rankings = compute_rankings(teams)
    return jsonify(rankings.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
