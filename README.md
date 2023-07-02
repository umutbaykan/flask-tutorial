<p align="center">
<img src="https://i.ibb.co/YXsBNPT/BATTLESHIP-02-07-2023-1.png" alt="logo" width="400" height="95"/>
</p>

Introduction
---
This is a multiplayer browser based full-stack application based on the (surprise surprise) battleship board gamewhere two players take turns trying to sink each other's ships. Full rules of the actual board game can be found [here](https://www.hasbro.com/common/instruct/battleship.pdf)
(There has been a few tweaks to the rules here and there in this project, you can read more on that in the [features](https://github.com/umutbaykan/battleship/edit/main/README.md#features) section)

The motivation behind this is to create an application where I can gradually keep on implementing new concepts I would like to learn more on. For the initial step, I wanted to find out more about web-sockets and design an events based game instead of relying solely on CRUD methods. The game battleship was chosen as it is both simple enough that I can work with, also complex enough that game logic cannot be built using only a handful of lines.

The application supports multiplayer gameplay and allows more than one game to be played at the same time. It is currently in progress so it has not been deployed yet, but you can run it on your local machine to try it out using [installation](https://github.com/umutbaykan/battleship/edit/main/README.md#installation) instructions.

Features
---
This section divides the features of the application into several sections and shows small clips for illustration. Often we will see two, maybe three browsers on the screen to display what the other users are seeing.
The application is mostly loyal to the original game rules apart from one; when a player hits the opponent target they do not get information on which ship they hit. This is done consciously as I think the game becomes easier if you know which ship you struck.

### Signup - Login - Logout
- Nothing really exciting here. No e-mail is required at this point as this is a toy app.
- Forms are validated with Formik - Yup on frontend, additional cross checks with db is done on backend.

### Landing Page / Lobby
- All available games are displayed on the lobby. Player can see the game configurations and host player prior to joining.
- Once a game is full, it is removed from the lobby.
- If any of the players leave prior to the game starting, the room becomes available again and displayed on the lobby.
- Players can configure their own games and create a room to be displayed in the lobby.

### Game
- Each game is a room. Players in the room only receive information for their corresponding room and not others.
- Game has a chat section where players can talk to one another. Information coming from the server is also displayed in this section.
- Game URL's are protected, therefore players need to join through verififcation from backend.

**Prior to game starting:**
- Player can place their ships and press start game to signal they are ready. Game does not initiate until both players are ready.
- Players can still leave / join the room as they like prior to game starting. If both players leave the room, the room and game automatically closes without saving.
- Players can currently only randomise the positions of their ships. Placing ships manually is a feature I plan to add on later. Randomisation is done on frontend, but validation is done on backend to ensure player has not cheated.

**Once game has started:**
- Game state gets saved at the end of every turn so players can come back to it at a later date.
- Players take turn shooting at each other's boards (big surprise there). Players hits and misses are displayed on the board.
- If any of the players leave halfway through, the other player gets a notification and the room closes down until it is loaded again by one of the players.
- Game state is masked in the backend, so players never get information on where their opponent's ships are.

**When game ends:**
- Players get to see each others full boards.
- Game state gets updated with the winner.
- Players can still keep on chatting, room closes when they leave.

### Profile
- Application profile section displays the history of the games user has played.
- Simple statistics on how many games user has played and their W/L ratio is displayed.
- It provides a load link to reactivate unfinished games. Once this link is pressed, the game room reopens from where players left off.
- Loaded games are considered private and cannot be joined from the lobby by random people. Players can see their reactivated unfinished games in the profile section, and can click the join button to take their place again.

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

You need to install Python, Node and MongoDB for this application to work, so the following instructions assume you have all those installed.

### Backend

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
Once you have the server running, you should see a message like this on your terminal. By default, your backend application will run on port 5000:
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
### Frontend

Once you have completed the installation for the backend server, you need to navigate to the frontend folder and install dependencies.
```terminal
# battleship/frontend
npm install
```
To start the frontend server
```terminal
npm start
```
Once that operation is complete, you should see a message like this on your terminal
```terminal
Compiled successfully!

You can now view frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.0.37:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
```
At this point, both your backend and frontend servers should be running. You should see the landing page once you open http://localhost:3000/ from your browser.
Remember, your backend server needs to be running for your application to work.

Structure
---
This section briefly covers the filing structure and logic of the application.
A high level explanation of the file structure can be found below:

```terminal
.
├── api
│   ├── battleship 
│   │   ├── database      # connection to db, methods accessing the db
│   │   ├── events        # handling of websocket events 
│   │   ├── models        # models that handle game logic
│   │   ├── routes        # API calls, route handling
│   │   ├── utils         # helper methods, global ROOM object, app extensions
│   │   └── __init__.py   # app factory
│   ├── instance
│   │   └── config.py     # configuration file - this is still under development so likely to change
│   └── tests
│       ├── seeds         # collection of seeds in DB and JSON objects to mimic data sent from frontend 
│       └── conftest.py   # test configurations
└── frontend
    ├── public            # img files and logos
    └── src
        ├── components    # components shared across multiple pages
        ├── pages         # sections and their respective components
        ├── services      # methods that conduct API call backend routes - shared across multiple components
        ├── utils         # helper methods
        ├── App.js        # 
        ├── index.js      #
        └── socket.js     # socket.io connection for frontend
```

- The application relies on server side sessions for verifications. 
- Initial game creation / loading is handled through API calls for verification purposes.
- All game actions are handled by events. Game sends an updated game state JSON object to players in the room each time game gets updated.
- Validations are done on backend to prevent unauthorized users from joining games. Users cannot take place of other players in games that already started, or manually put in URL's in the browser to bypass checks.
- Games are saved to database at the end of each turn, but game state is accessed through memory caching. All game state is stored in a global room object.
- All game model objects have serialize / deserialize methods to allow transfer of game state as a JSON object in a bidirectional way between frontend / backend.

Some items are still under development and very likely going to change:
- Configurations will be revisited before deployment, so those sections are in progress.
- CORS is currently enabled for development, but possibly removed later.
- Sessions will possibly be written to the database instead of having separate files for each session.
- At this point you might be wondering, why does it look.. awful? Why yes, yes it does. This is because CSS has been put together very quickly (and very poorly) just to see something on the front end. This will hopefully be tidied later.

//TODOS
---

These have been organised in order of next steps to take.
### Important
- Docker to containerize the app.
- Deploy using AWS or another provider.
- Setup a CI/CD workflow to automate deployment as development progresses.

### At some point
- Setup cypress tests for frontend.
- Add tests for event handling in backend.
- Add more validators to handle incoming JSON data from frontend.

### Nice to haves
- Users to be able to place ships manually.
- Enhance the statistics section to give more interesting data to user. Compare all users to have a leaderboard.
- Users to get notifications when a game they played in is loaded by their opponent instead of relying on an API call.
- Nicer looking actual images for the ships.
- Users to be able to create their own ships.
- Users to have private games.
- Replays, allowing users to replay a game at different speeds.
- Observers, users that do not have control over the game but can see masked version of both player boards and join the chat.
