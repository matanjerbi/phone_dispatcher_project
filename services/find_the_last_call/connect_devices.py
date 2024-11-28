from flask import blueprints, request, jsonify
from neo4j import GraphDatabase
from neo4j_service import LastCallRepository

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "12345678")
)

find_last_call_blueprint = blueprints.Blueprint('find_last_call_blueprint', __name__)


@find_last_call_blueprint.route("/api/find-last_call", methods=['POST'])
def get_interaction():
    data = request.json
    if not data:
        return jsonify({
            "status": "error",
            "message": "Missing device ID"
        }), 400

    repo = LastCallRepository(neo4j_driver)
    result = repo.find_last_call(data['id'])

    return jsonify({
        "status": "success",
        "data": result
    }), 200