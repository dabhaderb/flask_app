from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p> Hello, World! </p>"


@app.route("/sum/<int:x>/<int:y>")
def sum_numbers(x, y):
    total_sum = x + y
    output_dir = "output"
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    file_path = os.path.join(output_dir, f"text_{total_sum}.txt")

    with open(file_path, 'w') as file:
        file.write(f"Total sum is: {total_sum}")

    return f"<p>Total Sum: {total_sum}</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)


