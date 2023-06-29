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
    this.existingPositions = [];
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

  checkIfShipCanFit = (startingPosition, orientation, shipSize) => {
    let [x, y] = startingPosition;
    if (orientation) {
      return x + shipSize <= this.boardSize;
    } else {
      return y + shipSize <= this.boardSize;
    }
  };

  isClashing = (coords) => {
    const clash = coords.some((coordinate) =>
      this.existingPositions.some((existingCoord) =>
        existingCoord.every((value, index) => value === coordinate[index])
      )
    );
    return clash;
  };

  generatePlaceableShip = (shipName) => {
    let coords;
    const shipSize = this.shipSizes[shipName];
    let notFit = true;
    while (notFit) {
      const { orientation, x, y } = this.generateRandomValues(this.boardSize);
      const canFit = this.checkIfShipCanFit([x, y], orientation, shipSize);
      if (canFit) {
        coords = this.generateShipCoordinates([x, y], orientation, shipSize);
        notFit = false;
      }
    }
    return coords;
  };

  placeShip = (shipName) => {
    const shipCoordsToCheck = this.generatePlaceableShip(shipName);

    if (this.isClashing(shipCoordsToCheck)) {
      return false;
    } else {
      this.existingPositions = this.existingPositions.concat(shipCoordsToCheck);
      this.ships.push({
        name: shipName,
        coordinates: shipCoordsToCheck,
      });
      return true;
    }
  };

  randomize = () => {
    Object.keys(this.allowedShips).forEach((shipName) => {
      for (let i = 0; i < this.allowedShips[shipName]; i++) {
        let notPlaced = true;
        while (notPlaced) {
          if (this.placeShip(shipName)) {
            notPlaced = false;
          }
        }
      }
    });
  };
}

module.exports = VirtualBoard;
