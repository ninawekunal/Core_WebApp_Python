# Core_WebApp_Python
A Basic Demonstration App in python flask for a client-server architecture.
This app demonstrates a Web server architecture with sqlite connection for a basic login page.

To run the app: 
1. Make sure python3 is installed
2. Install requirements: 
```bash
pip install -r requirements.txt
```
3. Create a virtual environment: 
```bash
python3 -m venv venv
```
4. Activate the virtual env: 

Windows: 
```bash
venv\Scripts\activate
```
Mac: 
```bash
source venv/bin/activate
```
5. Run the app:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
6. Visit http://localhost:5000 to view the page in the browser.
7. Use the credentials `testuser` and `testpassword` for successful login.