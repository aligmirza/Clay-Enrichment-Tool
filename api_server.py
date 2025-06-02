import importlib.util
import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
API_KEYS = os.getenv("API_KEYS", "your-secret-api-key").split(",")
LOGIC_FOLDER = "logic"

@app.before_request
def check_api_key():
    key = request.headers.get("X-API-Key")
    if key not in API_KEYS:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/run', methods=['POST'])
def run_logic():
    payload = request.json
    logic_key = payload.get("logic")
    data = payload.get("data")

    if not logic_key:
        return jsonify({"error": "Missing logic key"}), 400

    logic_path = os.path.join(LOGIC_FOLDER, f"{logic_key}.py")
    if not os.path.exists(logic_path):
        return jsonify({"error": f"Logic '{logic_key}' not found"}), 404

    try:
        spec = importlib.util.spec_from_file_location("logic_module", logic_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        result = module.run(data)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
