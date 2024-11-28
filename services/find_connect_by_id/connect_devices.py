from flask import blueprints, request, jsonify
from neo4j import GraphDatabase
from neo4j_service import ConnectionRepository

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "12345678")
)

find_connect_blueprint = blueprints.Blueprint('find_connect_blueprint', __name__)


@find_connect_blueprint.route("/api/find-connection", methods=['POST'])
def get_interaction():
    data = request.json
    if not data or 'id' not in data:
        return jsonify({
            "status": "error",
            "message": "Missing device ID"
        }), 400

    repo = ConnectionRepository(neo4j_driver)
    result = repo.find_connection(data['id'])

    return jsonify({
        "status": "success",
        "data": result
    }), 200