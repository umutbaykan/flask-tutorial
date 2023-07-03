<p align="center">
<img src="https://i.ibb.co/YXsBNPT/BATTLESHIP-02-07-2023-1.png" alt="logo" width="400" height="95"/>
</p>

Table of Contents
---
1. [Introduction](https://github.com/umutbaykan/battleship#introduction)
2. [Features](https://github.com/umutbaykan/battleship#features)
3. [Technologies Used](https://github.com/umutbaykan/battleship#technologies-used)
4. [Installation](https://github.com/umutbaykan/battleship#introduction)
5. [Getting Started](https://github.com/umutbaykan/battleship#getting-started)
6. [Project Structure](https://github.com/umutbaykan/battleship#project-structure)
7. [TODOS](https://github.com/umutbaykan/battleship#todos)

Introduction
---
<img src="https://i.ibb.co/wc4KFsK/gamescreesnhot.png" alt="screenshot from game"/>

This project is a multiplayer browser-based full-stack application inspired by the (surprise surprise) classic battleship board game. In this game, two players take turns trying to sink each other's ships. While the core rules are based on the original game, there have been a few tweaks implemented, which are discussed in the [features](https://github.com/umutbaykan/battleship/edit/main/README.md#features) section. Full rules of the actual board game can be found [here](https://www.hasbro.com/common/instruct/battleship.pdf)

The main motivation behind developing this application is to explore and gradually implement new concepts that I'm interested in learning. For the initial step, I wanted to focus on websockets and design an event-based game, rather than relying solely on CRUD methods. Battleship was chosen as the game of choice because it strikes a balance between simplicity and complexity, providing an opportunity to work with game logic that requires more than just a few lines of code.

The application supports multiplayer gameplay and allows multiple games to be played simultaneously. Although it's still a work in progress and hasn't been deployed yet, you can run it on your local machine by following the [installation](https://github.com/umutbaykan/battleship/edit/main/README.md#installation) instructions provided.

Features
---
This section outlines the various features of the application and provides small clips for illustration purposes. In many cases, two browsers are shown on the screen to demonstrate what other users are seeing. While the application remains largely loyal to the original game rules, there is one notable difference: when a player successfully hits their opponent's target, they do not receive information about which ship they hit. This is done consciously as I think the game becomes easier if you know which ship you struck.

### Signup - Login - Logout
- Nothing really exciting here. No e-mail is required at this point as this is a toy app.
- Forms are validated using Formik and Yup on the frontend, with additional cross-checks performed on the backend using the database.
<img src="https://i.ibb.co/7Ydn6tF/optimize-signup.gif" alt="signup and login" width="800"/>

### Landing Page / Lobby
- The lobby displays all available games. Player can see the game configurations and the host player prior to joining.
- If any player leaves before the game starts, the room becomes available again and reappears in the lobby. 
- Players can also configure their own games and create rooms, which are then displayed in the lobby.
<img src="https://i.ibb.co/Z8Rvh1L/optimize-lobby-1.gif" alt="lobby and game configuration" width="800"/>

- Once a game is full, it is removed from the lobby.
<img src="https://i.ibb.co/whV9QtZ/optimize-lobby-2.gif" alt="game gets removed from lobby when full" width="800"/>

### Game
- Each game is represented by a room, and players only receive information relevant to their specific room, not others.
- The game includes a chat section where players can communicate with each other. Information from the server is also displayed in this section.
- Game URLs are protected, requiring verification from the backend for players to join.
<img src="https://i.ibb.co/C0QRHjy/optimize-chat.gif" alt="chat functionality" width="800"/>

<br /> <br />
_Prior to game starting:_
- Players can place their ships and signal their readiness by pressing the "start game" button. The game does not initiate until both players are ready.
- Players can freely join or leave the room before the game starts. If both players leave the room, the room and game automatically close without saving. 
- Currently, players can only randomize the positions of their ships, but manual ship placement is a planned feature for future development. Randomization occurs on the frontend, but backend validation ensures that players have not cheated.
<img src="https://i.ibb.co/h2KdFbq/optimize-shipplacing.gif" alt="placing ships" width="800"/>

<br /> <br />
_Once game has started:_
- The game state is saved at the end of every turn, allowing players to resume the game at a later date.
- Players take turns shooting at each other's boards (big surprise there), with hits and misses displayed on the board.
<img src="https://i.ibb.co/4JtSLTM/optimize-shooting.gif" alt="shooting" width="800"/>

- If one player leaves the game halfway through, the other player receives a notification, and the room closes until it is loaded again by either player.
- The game state is masked on the backend, ensuring that players never receive information about the locations of their opponent's ships.
<img src="https://i.ibb.co/GPNwjr2/optimize-leave-room-halfway.gif" alt="leaving room halfway through the game" width="800"/>

<br /> <br />
_When game ends:_
- Players have the opportunity to view each other's full boards. 
- The game state is updated with the winner.
- Players can continue chatting, but the room closes when they leave.
<img src="https://i.ibb.co/jrStmPk/optimize-game-end.gif" alt="game end" width="800"/>

### Profile
- The app's profile section displays the user's game history.
- It includes simple statistics such as the number of games played and the win/loss ratio.
- It provides a load link to reactivate unfinished games. Clicking on this link reopens the game room from where players left off.
<img src="https://i.ibb.co/Vgrz5q2/optimize-history.gif" alt="player history" width="800"/>

- Loaded games are considered private and cannot be joined from the lobby by random users.
- Players can view their reactivated unfinished games in the profile section and click the "join" button to resume their position.
<img src="https://i.ibb.co/9h9tyTc/optimize-game-load.gif" alt="game loading" width="800"/>

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

<br />

**Why this stack?**

There's no specific reason why I chose this particular stack other than the fact that I wanted to take on a challenge and try out a different backend framework and language for this project, which is why I went with Python and Flask. As for the database, MongoDB was the go-to option because I anticipate making further changes to the application as it develops. I wanted something that would provide me with flexibility in the long run.
Some additional packages were used; such as Flask-SocketIO for web-sockets, PyMongo to interact with the database, Formik and Yup for form validation on frontend.

Installation
---
Before we begin, please note that the application is not yet deployed, but you can still install and run it locally on your machine. Keep in mind that there might be some configuration changes during the deployment process.

Prerequisites
- Python
- Node.js
- npm
- MongoDB

### Backend

1) Clone this repository.
2) Open a terminal and navigate to the api folder within the project's root folder.

Before you install dependencies, you might want to create a python virtual environment for this project. The instructions below are for a macOS system, you can find out more about creating virtual environments for your opearting system through this [link](https://docs.python.org/3/library/venv.html).
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
To override the default database configuration, you can create a config.py file in the instance folder and provide your own values. For example, if you want to change the address of the database you want to connect to:

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

3) To run the backend server, execute the following command to run the app:
```terminal
# battleship/api
flask --app battleship run
# Optionally, you can run it in debug mode with the --debug flag.
```
To run tests:
```terminal
# battleship/api
python -m pytest
```

4) Once you have the server running, you should see a message like this on your terminal. By default, your backend application will run on port 5000:
```terminal
Launching on config.py settings
Server initialized for threading.
 * Serving Flask app 'battleship'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Frontend
5) Once you have completed the backend server installation, navigate to the frontend folder in the project's root folder. Install the required dependencies by running the following command:
```terminal
# battleship/frontend
npm install
```

6) To start the frontend server, use the command:
```terminal
npm start
```

7) Once that operation is complete, you should see a message like this on your terminal. You can access the application by opening http://localhost:3000 in your browser.
```terminal
Compiled successfully!

You can now view frontend in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.0.37:3000

Note that the development build is not optimized.
To create a production build, use npm run build.

webpack compiled successfully
```

With both the backend and frontend servers up and running, you should be able to see the landing page and start exploring the application.

Getting Started
---
Hopefully, this section will be expanded when the application is deployed. In the meantime, you can play the game locally by following these steps:

1) Open the application in two separate browser windows: one in normal mode and the other in incognito/private mode. This allows the backend to treat them as separate users.
2) Create an account in both browser windows to access all features.
3) Start the game by placing your ships and taking turns shooting at each other's boards (might be very difficult to hide your ships from your opponent staring at the same screen). 
4) To involve a third player, repeat the process by opening the application in a different browser or incognito/private mode.

Project Structure
---
The application's file structure and logic can be summarized as follows:

```terminal
.
├── api
│   ├── battleship
│   │   ├── database      # Handles the connection to the database and contains methods for accessing the data.
│   │   ├── events        # Manages the handling of WebSocket events.
│   │   ├── models        # Defines the models that handle the game logic.
│   │   ├── routes        # Handles the API calls and route handling.
│   │   ├── utils         # Provides helper methods, the global ROOM object, and app extensions.
│   │   └── __init__.py   # Serves as the app factory.
│   ├── instance
│   │   └── config.py     # Holds the configuration file (config.py) which is still under development and subject to change.
│   └── tests
│       ├── seeds         # Cntains a collection of seed data used in the database and JSON objects that mimic the data sent from the frontend.
│       └── conftest.py   # Test configurations.
└── frontend
    ├── public            # contains image files and logos used in the application.
    └── src
        ├── components    # Contains components shared across multiple pages.
        ├── pages         # Houses the sections and their respective components.
        ├── services      # Provides methods for conducting API calls to backend routes, shared across multiple components.
        ├── utils         # Includes helper methods.
        ├── App.js        # Contains all event listeners and creates contexts to pass down data to children components.
        ├── index.js      # Responsible for rendering the application.
        └── socket.js     # Establishes the Socket.IO connection for the frontend.
```
**Backend**
- User authentication and verification are handled through server-side sessions. Users do not send their IDs with each action, except during the initial login process.
- API calls are used for initial game creation and loading, providing verification checks.
- Game actions are processed through events, and the updated game state JSON object is sent to all players in the room whenever there is an update.
- Backend validations ensure that unauthorized users cannot join games in progress or bypass checks by manually entering URLs in the browser.
- Games are saved to the database at the end of each turn, while the game state is accessed through memory caching. The global room object stores all game state information.
- Game model objects have serialize/deserialize methods to enable bidirectional transfer of game state as a JSON object between the frontend and backend.

**Frontend**
- The App.js file serves as the main component and contains all event listeners. Received information is stored in contexts and accessed by child components that require it.
- The game state object holds crucial data related to the game. The backend removes any information related to the opponent's ship positions before sending it to the frontend.
- Upon receiving login verification from the backend, the user ID is stored in a session cookie, enabling access to protected routes.
- Game actions are emitted as events to the backend, with accompanying data sent as JSON and deciphered on the backend.

Some aspects are still undergoing development and are likely to change:

- Configuration settings are subject to revision before deployment.
- CORS is currently enabled for development purposes but may be removed in the future.
- Session management may transition from using separate files to writing sessions directly to the database.
- By now, you might be thinking, why does it look.. awful? Why yes, yes it does. This is because CSS has been put together very quickly (and poorly) just to see something on the front end. This will be tidied up later.

//TODO's
---

Here's a list of tasks organized based on the next steps to take:

### Important
- Containerize the app using Docker.
- Deploy the app using AWS or another hosting provider.
- Establish a CI/CD workflow to automate deployment as development progresses.

### In the pipeline
- Implement Cypress tests for the frontend.
- Add tests for event handling in the backend.
- Enhance validators to handle incoming JSON data from the frontend.

### Nice to have
- Enable users to manually place their ships.
- Improve the statistics section to provide more interesting data and introduce a leaderboard.
- Implement notifications for users when their opponent loads a game, instead of relying on API calls.
- Replace ship squares with actual ship graphics.
- Allow users to create their own custom ships.
- Enable users to have private games.
- Introduce game replays, allowing users to replay games at different speeds.
- Implement observer functionality, where users can see masked versions of both players' boards and join the chat.
