from flask import blueprints, request, jsonify
from neo4j import GraphDatabase
from neo4j_service import PhoneRepository

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",  # שים לב: פורט 7687, לא 7474!
    auth=("neo4j", "12345678")
)

phone_blueprint = blueprints.Blueprint('phone_blueprint', __name__)


@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
    data = request.json
    insert_data = PhoneRepository(neo4j_driver)
    return insert_data.create_device(data)


