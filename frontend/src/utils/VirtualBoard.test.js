const allowed_ships = {
  Destroyer: 1,
  Cruiser: 0,
  Battleship: 1,
  AircraftCarrier: 2,
};

const VirtualBoard = require("./VirtualBoard");

describe("VirtualBoard class", () => {
  let vb;

  beforeEach(() => {
    vb = new VirtualBoard(10, allowed_ships);
  });

  test("initializes", () => {
    expect(vb.ships).toEqual([]);
    expect(vb.boardSize).toEqual(10);
    expect(vb.allowedShips).toEqual(allowed_ships);
    expect(vb.existingPositions).toEqual([]);
  });

  test("detects clashing pieces if piece already in existing coordinates", () => {
    vb.existingPositions = [
      [0, 0],
      [0, 1],
    ];
    expect(
      vb.isClashing([
        [0, 1],
        [0, 2],
      ])
    ).toEqual(true);
  });

  test("does not return true if there is no clashing pieces", () => {
    vb.existingPositions = [
      [0, 0],
      [0, 1],
    ];
    expect(
      vb.isClashing([
        [0, 2],
        [0, 3],
      ])
    ).toEqual(false);
  });

  test("when a ship is placed, its coordinates are added to existing positions", () => {
    vb.existingPositions = [[11, 11]];
    const result = vb.placeShip("AircraftCarrier");
    expect(result).toEqual(true);
    expect(vb.existingPositions.length).toEqual(6);
    expect(vb.ships[0].coordinates.length).toEqual(5);
  });
});
