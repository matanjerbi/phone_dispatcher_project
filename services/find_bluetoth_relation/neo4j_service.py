
class BluetoothRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_bluetooth(self):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (start:Device)
                MATCH (end:Device)
                WHERE start <> end
                MATCH path = shortestPath((start)-[:INTERACTED_WITH*]->(end))
                WHERE ALL(r IN relationships(path) WHERE r.method = 'Bluetooth')
                WITH path, length(path) as pathLength
                ORDER BY pathLength DESC
                LIMIT 1
                RETURN 
                    pathLength,
                    [node in nodes(path) | {
                        id: node.id,
                        name: node.name,
                        model: node.model
                    }] as devices
            """)

            record = result.single()
            if record:
                return {
                    "path_length": record["pathLength"],
                    "connected_devices": record["devices"]
                }
            return None
