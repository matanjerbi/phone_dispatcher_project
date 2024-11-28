
class StrengthRepository:
    def __init__(self, driver):
        self.driver = driver

    def find_all_signal_strength_stronger(self, data):
        with self.driver.session() as session:
            result = session.run("""
                match (d:Device)-[r:INTERACTED_WITH]->(d1:Device)
                where r.signal_strength_dbm > -60
                return d.name, d1.name, r.signal_strength_dbm
            """)
            data = [{"send": record["d.name"], "receive": record["d1.name"], "strength": record["r.signal_strength_dbm"]} for record in result]
        return data


