from flask import Flask, jsonify, send_from_directory
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/data')
def data():
    df = pd.read_excel(r"C:\Users\aakas\Downloads\projects\Project\test2.xlsx", header=1)
    print(df.columns.tolist())
    #print(df.head())
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")  # Normalize column names
    #return df.to_json(orient='records')

    data = []
    for _, row in df.iterrows():
        data.append({
            "name": row.get("employee_name", ""),
            "id": row.get("employee_id", ""),
            "email": row.get("email_id", ""),
            "resume": row.get("resume", "Not Uploaded"),
            "salary_slip": row.get("salary_slip", "Not Uploaded"),
            "aadhar_card": row.get("aadhar_card", "Not Uploaded"),
            "pan_card": row.get("pan_card", "Not Uploaded"),
        })
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
