from flask import blueprints, request, jsonify
from neo4j import GraphDatabase
from neo4j_service import ConnectionRepository

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "12345678")
)

connect_blueprint = blueprints.Blueprint('connect_blueprint', __name__)


@connect_blueprint.route("/api/find-connection-between", methods=['POST'])
def get_interaction():
    data = request.json
    if not data or 'id_1' not in data:
        return jsonify({
            "status": "error",
            "message": "Missing device ID"
        }), 400

    repo = ConnectionRepository(neo4j_driver)
    result = repo.find_connection_between_two_devices(data['id_1'], data['id_2'])

    return jsonify({
        "status": "success",
        "data": result
    }), 200