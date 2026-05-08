from flask import Flask, redirect, url_for, session, jsonify, make_response
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = "SECRET_KEY"  
oauth = OAuth(app)  


github = oauth.register(
    name='github',
    client_id='Ov23liFK42BTEjIbm9Zy',
    client_secret='2037c4c2e366e087e7ca0fbbbb6ee31e4c7c7280',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize',
    api_base_url='https://api.github.com/',
    client_kwargs={'scope': 'user:email'},
)

@app.route('/')
def index():
    if 'user' in session:
        return f'''
            <h1>Logged in as {session["user"]["login"]}</h1>
            <a href="/profile"><button>View Profile</button></a>
            <a href="/logout"><button>Logout</button></a>
        '''
    return '''
        <h1>Securing APIs using OAuth 2.0 with GitHub and Auth0</h1>
        <p>Status: Not Logged In</p>
        <a href="/login"><button>Login with GitHub</button></a>
        <br><br>
        <a href="/profile"><button>Try Accessing Profile (Protected)</button></a>
    '''

@app.route('/login') 
def login():
  
    return github.authorize_redirect(url_for('callback', _external=True))

@app.route('/callback')
def callback():
    try:
        token = github.authorize_access_token()
        user = github.get('user').json()
        session['user'] = user
        print(f"DEBUG: Successfully logged in as {user.get('login')}") 
        return redirect('/profile')
    except Exception as e:
        print(f"DEBUG: Error during callback: {e}")
        return f"Authentication Error: {e}", 500
    
@app.route('/profile') 
def profile():
    
    if 'user' not in session:
        return '<h1>Unauthorized</h1><p>Please <a href="/login">login</a> first.</p>', 401 # [cite: 92]
    
    user = session['user']
    response_text = f'''
        <h1>Welcome, {user["login"]}!</h1>
        <p>Email: {user.get("email", "Not Public")}</p>
        <img src="{user["avatar_url"]}" width="100">
        <br><br>
        <a href="/logout"><button>Logout</button></a>
    '''
   
    response = make_response(response_text)
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/logout') 
def logout():
    session.clear() 
    return redirect('/')


@app.route('/api/secure-data')
def secure_data():
    if 'user' not in session:
        return jsonify({"error": "Unauthorized"}), 401
    return jsonify({"message": "This is protected data!", "user": session['user']['login']})

if __name__ == '__main__':
    app.run(debug=True)