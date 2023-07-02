<p align="center">
<img src="https://i.ibb.co/YXsBNPT/BATTLESHIP-02-07-2023-1.png" alt="logo" width="400" height="95"/>
</p>

Introduction
---
This is a multiplayer browser based full-stack application based on the (surprise surprise) battleship board gamewhere two players take turns trying to sink each other's ships. Full rules of the actual board game can be found [here](https://www.hasbro.com/common/instruct/battleship.pdf)
(There has been a few tweaks to the rules here and there in this project, you can read more on that in the [features](https://github.com/umutbaykan/battleship/edit/main/README.md#features) section)

The motivation behind this is to create an application where I can gradually keep on implementing new concepts I would like to learn more on. For the initial step, I wanted to find out more about web-sockets and design an events based game instead of relying solely on CRUD methods. The game battleship was chosen as it is both simple enough that I can work with, also complex enough that game logic cannot be built using only a handful of lines.

The application supports multiplayer gameplay and allows more than one game to be played at the same time. It is currently in progress so it has not been deployed yet, but you can run it on your local machine to try it out using [installation](https://github.com/umutbaykan/battleship/edit/main/README.md#installation) instructions.

Technologies Used
---
### Frontend: 
React, JavaScript, Cypress (In Progress!)
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original-wordmark.svg" alt="react" width="40" height="40"/> 
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/>
<img src="https://www.cypress.io/images/layouts/cypress-logo.svg" alt="cypress" width="40" height="40"/>

### Backend: 
Python, Flask, MongoDB, PyTest
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg" alt="flask" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg" alt="mongodb" width="40" height="40"/>
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pytest/pytest-original.svg" alt="pytest" width="40" height="40"/>


**Why this stack?**

There isn't a specific reason why this particular stack was chosen other than the fact I wanted to try out a different backend framework and language on this project as a challenge (python / flask). MongoDB was picked because I envision the application will go through changes as I develop it further, so I wanted to pick something that would give me more flexibility on the long run. 
Some additional packages were used; such as Flask-SocketIO for web-sockets, PyMongo to interact with the database, Formik and Yup for form validation on frontend.

Installation
---
First things first, hopefully this application will be deployed soon. During that process, I hope to streamline the process to launch the backend more smoothly. Also there will inevitably be a cleanup operation to tidy the configuration files and unnecessary folders. But in the meanwhile, if you want to install it locally clone this repo.

You need to install Python and MongoDB for this application to work, so the following instructions assume you have both installed.

Before you install dependancies, you might want to create a python virtual environment for this project. The instructions below are for a macOS system, you can find out more about creating virtual environments in other opearting systems through this [link](https://docs.python.org/3/library/venv.html).
Once you are in the root folder of application, navigate to api folder and install dependencies.

```terminal
# battleship/api
# To create a virtual environment
python3 -m venv .venv

# To activate the virtual environment you just created
. .venv/bin/activate

# Once you are in the virtual environment
pip install -r requirements.txt

# This should install all dependencies. 
```

By default, the application tries to connect to _mongodb://0.0.0.0/battleship_ for development and _mongodb://0.0.0.0/battleship-test_ for testing.
Upon initial launch, the application will create two folders under the api/ folder, with the names of flask_session (to store user sessions in files) and instance.
You can override app launch configurations by creating a config.py in the instance folder and input any override values in there. For example, if you want to change the address of the database you want to connect to:

```python
# instance/config.py
MONGO_URI='mongodb://0.0.0.0/my-own-database'

# To override test database:
# tests/conftest.py
@pytest.fixture
def app():
    app = create_app(
        {
            "TESTING": True,
            # You can change the address below
            "MONGO_URI": "mongodb://0.0.0.0/battleship-test",
        }
    )
```

While you are in the virtual environment

To run the app:
```terminal
# battleship/api
flask --app battleship run

# If you want to run it in debug mode
flask --app battleship run --debug
```
Once you have the server running, you should see a message like this on your terminal:
```terminal
Launching on config.py settings
Server initialized for threading.
 * Serving Flask app 'battleship'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

To run tests:
```terminal
# battleship/api
python -m pytest
```

Features
---


TODOS
---

