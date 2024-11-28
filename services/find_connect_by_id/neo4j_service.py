class ConnectionRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_connection(self, device_id):
        with self.driver.session() as session:
            result = session.run("""
                MATCH (d:Device)-[r:INTERACTED_WITH]-(d1:Device)
                WHERE d.id = $device_id 
                RETURN {
                    count: COUNT(d),
                    connections: COLLECT({
                        connected_device: d1.id,
                        name: d1.name,
                        connection_type: r.method
                    })
                } as result
            """, device_id=device_id)

            record = result.single()
            if record:
                return record["result"]
            return {"count": 0, "connections": []}
