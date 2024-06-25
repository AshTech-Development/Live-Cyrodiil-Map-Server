from flask import Flask, jsonify

app = Flask(__name__)

# Sample data for Cyrodiil map
CYRODIIL_DATA = {
    "Campaign 1": {
        "mapData": {
            "playerLocation": {"x": 12345, "y": 67890},
            "objectives": [
                {"x": 11111, "y": 22222, "name": "Objective 1", "description": "Capture this objective"},
                {"x": 33333, "y": 44444, "name": "Objective 2", "description": "Defend this objective"}
            ]
        },
        "campaignScores": [
            {"alliance": 1, "score": 1000},
            {"alliance": 2, "score": 2000},
            {"alliance": 3, "score": 1500}
        ],
        "emperorship": {
            "name": "Emperor Xyron",
            "alliance": 2,
            "remainingTime": "2 hours"
        }
    },
    "Campaign 2": {
        # ... add data for Campaign 2 here
    }
}

@app.route('/api/get-map-data', methods=['GET'])
def get_map_data():
    return jsonify(CYRODIIL_DATA)

if __name__ == '__main__':
    app.run(debug=True)
