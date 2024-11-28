from flask import blueprints, request, jsonify
from neo4j import GraphDatabase
from neo4j_service import StrengthRepository

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",  # שים לב: פורט 7687, לא 7474!
    auth=("neo4j", "12345678")
)

signal_strength_blueprint = blueprints.Blueprint('signal_strength_blueprint', __name__)



@signal_strength_blueprint.route("/api/signal-strength", methods=['GET'])
def get_interaction():
    repo = StrengthRepository(neo4j_driver)
    data = repo.find_all_signal_strength_stronger(neo4j_driver)
    return jsonify({
        "status": "success",
        "data": data
    }), 200
