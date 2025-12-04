from flask import Flask, request, jsonify

app = Flask(__name__)

students = []

@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    students.append(data)
    return jsonify({"message": "Student added successfully"})

@app.route("/students", methods=["GET"])
def view_students():
    return jsonify(students)

@app.route("/search/<name>", methods=["GET"])
def search_student(name):
    result = [s for s in students if s["name"].lower() == name.lower()]
    return jsonify(result)

@app.route("/update/<sid>", methods=["PUT"])
def update_student(sid):
    data = request.json
    for s in students:
        if s["id"] == sid:
            s.update({k:v for k,v in data.items() if v})
            return jsonify({"message":"Student updated"})
    return jsonify({"message":"Student not found"}),404

@app.route("/delete/<sid>", methods=["DELETE"])
def delete_student(sid):
    global students
    students = [s for s in students if s["id"] != sid]
    return jsonify({"message":"Student deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
