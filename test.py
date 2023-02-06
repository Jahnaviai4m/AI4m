import psycopg2
import json

def insert_data_from_json():
    try:
        with open("data.json",'r') as f:
            data =json.load(f)
        print(data,"data inserted")
    except Exception as e:
        print("Error reading JSON file:", e)
        return

    try:
        conn = psycopg2.connect(
            host="localhost",
            database="ocwes",
            user="pi",
            password="Ai4m2023",
            port = "5432"
        )
        cursor = conn.cursor()
    except Exception as e:
        print("Error connecting to database:", e)
        return

    try:
        query = "INSERT INTO rawtable (stationid, lotid,timestamp,spectroscope1allwavelengths,spectroscope1) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(query, [(d["stationid"], d["lotid"], d["timestamp"],d ["spectroscope1allwavelengths"], d["spectroscope1"]) for d in data])

        #conn.commit()

        cursor.execute(query)
        conn.commit()
        print("Data Inserted into the table successfully")
    except Exception as e:
        print("Unsuccessful")
        cursor.close()
        conn.close()

insert_data_from_json()
