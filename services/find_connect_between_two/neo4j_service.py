from flask import jsonify


class ConnectionRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_connection_between_two_devices(self, device_id_1, device_id_2):
        with self.driver.session() as session:
            result = session.run("""
                    MATCH (d:Device)-[r:INTERACTED_WITH]-(d1:Device)
                    WHERE d.id = $device_id AND d1.id = $device_id_1
                    RETURN d1
                    """, device_id=device_id_1, device_id_1=device_id_2)

            if result:
                return {"result": True}
            else:
                return {"result": False}
