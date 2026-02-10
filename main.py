from flask import Flask, render_template_string, request, session
import StringNumberConversion
import random
import os
import secrets

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY') or secrets.token_hex(32)

convert = StringNumberConversion.Conversion()

# Initialize session variables
@app.before_request
def initialize_session():
    if 'mode' not in session:
        session['mode'] = "Words to Number"
    if 'string' not in session:
        session['string'] = ""
    if 'number' not in session:
        session['number'] = 0
    if 'result' not in session:
        session['result'] = ""

tryString = ["Try: two thousand seventy seven", 
             "Try: eight billion", 
             "Try: one hundred thousand fifty nine",
             "Try: twenty hundred million ninety thousand seven hundred sixty eight",
             "Try: zero",
             "Try: seven",
             "Try: eleven",
             "Try: six hundred sixty nine"
             ]
tryNumber = ["Try: 190339",
             "Try: 66",
             "Try: 72",
             "Try: 10000400034",
             "Try: 803994",
             "Try: 2077",
             "Try: 2048",
             "Try: 2025"
             ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Update session variables from form data
        session['mode'] = request.form.get('mode', 'Words to Number')
        
        if session['mode'] == 'Words to Number':
            session['string'] = request.form.get('input', '')
            session['result'] = convert.convertToNum(session['string'])
        else:
            try:
                session['number'] = int(request.form.get('input', 0))
                session['result'] = convert.convertToString(session['number'])
            except ValueError:
                session['result'] = "Invalid number"

    # Generate placeholder text
    placeholder = random.choice(tryString) if session['mode'] == 'Words to Number' else random.choice(tryNumber)
    
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Number-Word Converter</title>
            <style>
                .container { width: 80%; margin: 0 auto; text-align: center; }
                h1 { font-size: 2.2em; }
                .input-group { margin: 20px 0; }
                textarea { width: 300px; height: 100px; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Number-Word Converter</h1>
                <form method="POST">
                    <div class="input-group">
                        <label>
                            <input type="radio" name="mode" value="Words to Number" 
                                {{ 'checked' if session.mode == 'Words to Number' }}>
                            Words to Number
                        </label>
                        <label>
                            <input type="radio" name="mode" value="Enter a number:" 
                                {{ 'checked' if session.mode == 'Enter a number:' }}>
                            Number to Words
                        </label>
                    </div>
                    
                    <div class="input-group">
                        <textarea name="input" placeholder="{{ placeholder }}">{{ 
                            session.string if session.mode == 'Words to Number' else session.number 
                        }}</textarea>
                    </div>
                    
                    <div class="input-group">
                        <button type="submit">Convert</button>
                    </div>
                </form>
                
                {% if session.result %}
                <div class="result">
                    <h3>Result:</h3>
                    <p>{{ session.result }}</p>
                </div>
                {% endif %}
            </div>
        </body>
        </html>
    ''', placeholder=placeholder)

if __name__ == '__main__':
    app.run(debug=True)