from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session management

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/entry')
def entry():
    return redirect(url_for('entry_step1'))

@app.route('/entry_step1', methods=['GET', 'POST'])
def entry_step1():
    if request.method == 'POST':
        session['sleep'] = request.form['sleep']
        session['screen_time'] = request.form['screen_time']
        session['books'] = request.form['books']
        return redirect(url_for('entry_step2'))
    return render_template('entry_step1.html')

@app.route('/entry_step2', methods=['GET', 'POST'])
def entry_step2():
    if request.method == 'POST':
        print("Received Form Data:", request.form)  # Debugging line

        # Ensure all fields exist in the form submission
        if 'fitness' not in request.form or 'work_hours' not in request.form or 'social' not in request.form:
            return "Error: One or more required fields are missing. Please go back and fill all fields.", 400
        
        # Store the data in the session
        session['fitness'] = request.form['fitness']
        session['work_hours'] = request.form['work_hours']
        session['social'] = request.form['social']

        return redirect(url_for('entry_step3'))

    return render_template('entry_step2.html')



@app.route('/entry_step3', methods=['GET', 'POST'])
def entry_step3():
    if request.method == 'POST':
        session['goal'] = request.form['goal']
        session['improvement'] = request.form['improvement']
        session['achievement'] = request.form['achievement']
        session['challenge'] = request.form['challenge']
        return redirect(url_for('summary'))
    return render_template('entry_step3.html')

@app.route('/summary')
def summary():
    return render_template('summary.html', data=session)

if __name__ == '__main__':
    app.run(debug=True)
