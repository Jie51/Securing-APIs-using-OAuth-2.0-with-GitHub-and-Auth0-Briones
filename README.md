# Securing-APIs-using-OAuth-2.0-with-GitHub-and-Auth0-Briones

## 🚀 How to Get and Run this Project

Follow these steps to set up the lab on your local machine:

### 1. Clone the Repository
Open your terminal or command prompt and run:
```bash
git clone <your-repository-url>
cd <your-folder-name>
```
### 2. Set Up a Virtual Environment
(Recommended)To keep your dependencies organized, create and activate a virtual environment:
PowerShell# Create the environment
```
python -m venv .venv
```

# Activate it (Windows)
```
.\.venv\Scripts\activate
```
### 3. Install DependenciesUse the requirements.txt file to install all necessary libraries:
   ```
    Bashpip install -r requirements.txt
   ```
### 5. Configure GitHub OAuthGo to your GitHub Developer Settings and create a New OAuth App.
Set the Homepage URL to http://localhost:5000.
Set the Authorization Callback URL to http://localhost:5000/callback.
Copy your Client ID and Client Secret into the app.register section of app.py .

### 6. Run the ApplicationStart the Flask server:  

Bashpython app.py


### 7. try [local](http://localhost:5000/) to access it in your browser
