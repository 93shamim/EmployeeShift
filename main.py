from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for demonstration purposes
employee_data = [
    {"id": 1, "name": "John Doe"},
    {"id": 2, "name": "Jane Smith"}
]

shifts_data = [
    {"id": 1, "name": "Morning Shift"},
    {"id": 2, "name": "Afternoon Shift"}
]

@app.route('/')
def index():
    return render_template('index.html', employees=employee_data, shifts=shifts_data)

@app.route('/submit_shift', methods=['POST'])
def submit_shift():
    if request.method == 'POST':
        employee_id = request.form['employee']
        shift_id = request.form['shift']
        # Here you can add code to handle the submitted shift data
        print(f"Submitted shift for Employee ID {employee_id} to Shift ID {shift_id}")
        return redirect(url_for('index'))
    
if __name__ == "__main__":
    app.run(debug=True)
