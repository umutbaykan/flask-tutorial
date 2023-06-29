class VirtualBoard {
  constructor(boardSize, allowedShips) {
    this.boardSize = boardSize;
    this.shipSizes = {
      Destroyer: 2,
      Cruiser: 3,
      Battleship: 4,
      AircraftCarrier: 5,
    };
    this.allowedShips = allowedShips;
    this.ships = [];
  }

  generateRandomValues = () => {
    const orientation = Math.random() >= 0.5;
    const x = Math.floor(Math.random() * this.boardSize);
    const y = Math.floor(Math.random() * this.boardSize);
    return { orientation, x, y };
  };

  generateShipCoordinates = (startingPosition, orientation, size) => {
    const shipCoordinates = [];
    let [x, y] = startingPosition;
    for (let i = 0; i < size; i++) {
      if (orientation) {
        shipCoordinates.push([x + i, y]);
      } else {
        shipCoordinates.push([x, y + i]);
      }
    }
    return shipCoordinates;
  };

  retrieveShipCoordinates = () => {
    return;
  };

  checkIfShipCanFit = (startingPosition, orientation, shipSize) => {
    let [x, y] = startingPosition;
    if (orientation) {
      return x + shipSize <= this.boardSize;
    } else {
      return y + shipSize <= this.boardSize;
    }
  };

  checkForClash = () => {};

  placeShip = (shipName) => {
    const shipSize = this.shipSizes[shipName];
    const { orientation, x, y } = this.generateRandomValues(this.boardSize);
    const canFit = this.checkIfShipCanFit([x, y], orientation, shipSize);
    if (canFit) {
      this.ships.push(
        this.generateShipCoordinates([x, y], orientation, shipSize)
      );
      this.checkForClash();
    }
  };

  randomize = () => {
    Object.keys(this.allowedShips).forEach((shipName) => {
      for (let i = 0; i < this.allowedShips[shipName]; i++) {
        //   while (true) {
        //     if (placeShip(grid, shipName)) {break};
        //   }
        this.placeShip(shipName);
      }
    });
  };
}

const allowed_ships = {
  Destroyer: 1,
  Cruiser: 0,
  Battleship: 1,
  AircraftCarrier: 2,
};

const vb = new VirtualBoard(10, allowed_ships);
vb.randomize();
console.log(vb.ships);

// define starting position and orientation
// check if ship can fit on board on sheer size
// if ok, pass the starting position and size inside to generate coordinates
// check if a ship is already there
// if it is, go back to step one

// if not, move onto the next ship
