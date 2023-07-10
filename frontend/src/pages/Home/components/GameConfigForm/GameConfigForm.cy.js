import GameConfigForm from "./GameConfigForm";

describe("GameConfigForm", () => {
  it('calls backend server with user game configurations and navigates to the page', () => {
    cy.mount(<GameConfigForm />);
    cy.get('[data-cy="board-size"]').type(9)
    cy.get('[data-cy="destroyer"]').type(2)
    cy.get('[data-cy="battleship"]').type(0)
    cy.get('[data-cy="p2-starts"]').click()
    cy.get('[data-cy="gameconfig-submit"]').click()
    // The test should check for these things now:
    // Are we transmitting the right data?
    // Are we emitting the right data?
  })

  it("with too big board, displays must be less than error", () => {
    cy.mount(<GameConfigForm />);
    cy.get('[data-cy="board-size"]').type(17)
    cy.get('[data-cy="error-message"]').should('contain.text', "Must be 16 or less");
  });

  it("with too small board, displays must be at least error", () => {
    cy.mount(<GameConfigForm />);
    cy.get('[data-cy="board-size"]').type(4)
    cy.get('[data-cy="error-message"]').should('contain.text', "Must be at least 5");
  });

  it("with negative ships, displays cant have negative ships error", () => {
    cy.mount(<GameConfigForm />);
    cy.get('[data-cy="destroyer"]').type(-1)
    cy.get('[data-cy="error-message"]').should('contain.text', "Cant have negative ships");
  });

  it("with too many ships, displays lets not go crazy error", () => {
    cy.mount(<GameConfigForm />);
    cy.get('[data-cy="destroyer"]').type(6)
    cy.get('[data-cy="error-message"]').should('contain.text', "Lets not go crazy captain");
  });
})
