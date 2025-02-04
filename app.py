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
        print("Received Form Data (Step 1):", request.form)  # Debugging line

        session['sleep'] = request.form['sleep']
        session['screen_time'] = request.form['screen_time']
        session['books'] = request.form['books']
        return redirect(url_for('entry_step2'))
    
    return render_template('entry_step1.html')

@app.route('/entry_step2', methods=['GET', 'POST'])
def entry_step2():
    if request.method == 'POST':
        print("Received Form Data (Step 2):", request.form)  # Debugging line

        session['fitness'] = request.form['fitness']
        session['work_hours'] = request.form['work_hours']
        session['social'] = request.form['social']
        return redirect(url_for('entry_step3'))
    
    return render_template('entry_step2.html')

@app.route('/entry_step3', methods=['GET', 'POST'])
def entry_step3():
    if request.method == 'POST':
        print("Received Form Data (Step 3):", request.form)  # Debugging line

        session['goal'] = request.form['goal']
        session['improvement'] = request.form['improvement']
        session['achievement'] = request.form['achievement']
        session['challenge'] = request.form['challenge']
        return redirect(url_for('summary'))
    
    return render_template('entry_step3.html')

@app.route('/summary', methods=['GET', 'POST'])  # ✅ FIXED: Accepts both GET and POST
def summary():
    print("Loading Summary Page...")  # Debugging line
    return render_template('summary.html', data=session)

if __name__ == '__main__':
    app.run(debug=True)
