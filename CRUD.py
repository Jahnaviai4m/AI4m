import psycopg2
import json

def insert_data(data):
    conn = psycopg2.connect(
        host="localhost",
        database="ocwes",
        user="postgres",
        password="admin"
    )
    cursor = conn.cursor()

    query = "INSERT INTO New_Scan (lot_number,scan_number,timestamp,substrate_type,precoating_type,coating_type,scan_status,current_CW,average_CW) VALUES (%s, %s, %s,%s,%s,%s,%s,%s,%s)"
    cursor.execute(query, (data["lot_number"], data["scan_number"], data["timestamp"],data["substrate_type"], data["precoating_type"], data["coating_type"], data["scan_status"], data["current_CW"], data["average_CW"] ))

    conn.commit()
    cursor.close()
    conn.close()

def fetch_data():
    conn = psycopg2.connect(
        host="localhost",
        database="ocwes",
        user="postgres",
        password="admin"
    )
    cursor = conn.cursor()

    query = "SELECT * FROM new_scan"
    cursor.execute(query)

    records = cursor.fetchall()

    cursor.close()
    conn.close()

    return records

def insert_data_from_json(json_file):
    with open(json_file) as f:
        data = json.load(f)

    conn = psycopg2.connect(
        host="localhost",
        database="ocwes",
        user="postgres",
        password="admin"
    )
    cursor = conn.cursor()

    query = "INSERT INTO Raw_Table (station_id, lot_id,timestamp,spectroscope1_allwavelengths,spectroscope1) VALUES (%s,%s,%s,%s,%s)"
    cursor.executemany(query, [(d["station_id"], d["lot_id"], d["timestamp"],d ["pectroscope1_allwavelengths"],d ["spectroscope1"]) for d in data])

    conn.commit()
    cursor.close()
    conn.close()
