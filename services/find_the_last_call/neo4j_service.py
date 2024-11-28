class LastCallRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_last_call(self, device_id):
        with self.driver.session() as session:
            result = session.run("""
                            MATCH (d:Device)-[r:INTERACTED_WITH]-(other:Device)
                            WHERE d.id = $device_id
                            RETURN {
                                device: {
                                    id: other.id,
                                    name: other.name,
                                    model: other.model
                                },
                                interaction: {
                                    method: r.method,
                                    timestamp: toString(r.timestamp),
                                    signal_strength_dbm: r.signal_strength_dbm,
                                    distance_meters: r.distance_meters,
                                    duration_seconds: r.duration_seconds
                                }
                            } as result
                            ORDER BY r.timestamp DESC
                            LIMIT 1
                        """, device_id=device_id)

            record = result.single()
            return record["result"] if record else None
