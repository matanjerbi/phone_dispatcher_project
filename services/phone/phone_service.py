from flask import blueprints, request, jsonify
from neo4j import GraphDatabase

from neo4j_service import PhoneRepository

# from app.phone_tracker.dispatchers import PhoneInteractionDispatcher
# from app.phone_tracker.repository import PhoneInteractionRepository
# from app.phone_tracker.services import PhoneTrackerService
# from app.phone_tracker.models import PhoneInteraction

neo4j_driver = GraphDatabase.driver(
    "bolt://localhost:7687",  # שים לב: פורט 7687, לא 7474!
    auth=("neo4j", "12345678")
)

phone_blueprint = blueprints.Blueprint('phone_blueprint', __name__)


@phone_blueprint.route("/api/phone_tracker", methods=['POST'])
def get_interaction():
    # data = request.json
    # phone = PhoneRepository(neo4j_driver)
    # for device in data['devices']:
    #     phone.create_device(phone)
    # return jsonify(data), 200
    data = request.json  # זה מכיל את כל הדאטה כולל devices ו-interaction
    phone = PhoneRepository(neo4j_driver)
    return phone.create_device(data)

# @phone_blueprint.route("/api/phone_tracker", methods=['POST'])
# def get_interaction():
#     print(request.json)
#     return jsonify({}), 200
