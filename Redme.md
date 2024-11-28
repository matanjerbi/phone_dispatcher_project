# Phone Dispatcher Project

## מבנה הפרויקט
```
phone_dispatcher_project/
├── services/
│   ├── find_bluetooth_relation/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── bluetooth_service.py
│   │   └── neo4j_service.py
│   │
│   ├── find_connect_between_two/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── find_connect.py
│   │   └── neo4j_service.py
│   │
│   ├── find_connect_by_id/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── connect_devices.py
│   │   └── neo4j_service.py
│   │
│   ├── find_the_last_call/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── connect_devices.py
│   │   └── neo4j_service.py
│   │
│   ├── insert_data/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── neo4j_service.py
│   │   └── phone_service.py
│   │
│   └── signal_strength/
│       └── __init__.py
│
└── README.md
```

## השירותים במערכת

### Find Bluetooth Relation (Port: 5001)
- מציאת קשרי בלוטות' בין מכשירים
- Endpoint: `GET /api/bluetooth`

### Find Connect Between Two (Port: 5002)
- מציאת קשרים בין שני מכשירים ספציפיים
- Endpoint: `POST /api/find-connection-between`

### Find Connect By ID (Port: 5003)
- מציאת כל החיבורים של מכשיר ספציפי
- Endpoint: `POST /api/find-connection`

### Find The Last Call (Port: 5004)
- מציאת השיחה האחרונה של מכשיר
- Endpoint: `POST /api/find-last_call`

### Insert Data (Port: 5005)
- הכנסת נתוני מכשיר חדש למערכת
- Endpoint: `POST /api/phone_tracker`

### Signal Strength
- שירות עתידי למדידת עוצמת אות (בפיתוח)

## הגדרות Neo4j
```
Host: localhost
Port: 7687
Username: neo4j
Password: 12345678
```

## התקנה והפעלה

### דרישות מקדימות
```bash
pip install flask neo4j
```

### הפעלת שירות
```bash
# עבור כל שירות, יש להיכנס לתיקייה שלו ולהריץ
python app.py
```
