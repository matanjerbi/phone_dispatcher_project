from flask import blueprints, request, jsonify
from neo4j import GraphDatabase

from neo4j_service import BluetoothRepository

# from app.phone_tracker.dispatchers import PhoneInteractionDispatcher
# from app.phone_tracker.repository import PhoneInteractionRepository
# from app.phone_tracker.services import PhoneTrackerService
# from app.phone_tracker.models import PhoneInteraction

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",
    auth=("neo4j", "12345678")
)

bluetooth_blueprint = blueprints.Blueprint('bluetooth_blueprint', __name__)


@bluetooth_blueprint.route("/api/bluetooth", methods=['GET'])
def get_bluetooth_path():
    repo = BluetoothRepository(neo4j_driver)
    data = repo.find_bluetooth()
    return jsonify({
        "status": "success",
        "data": data
    }), 200

