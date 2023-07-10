import SignUpForm from "./SignUpForm";

describe("Sign up form frontend validations", () => {
  it("with missing password, displays password required error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Password is required.");
  });

  it("with missing username, displays required error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Required");
  });

  it("with missing confirm password, displays confirm password required error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Confirm password is required.");
  });

  it("with too short username, displays must be at least 3 characters error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("hi");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="confirm-password"]').type("password");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Must be at least 3 characters.");
  });

  it("with too long username, displays must be at least 3 characters error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("ThisIsReallyTooLongNow");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="confirm-password"]').type("password");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Must be 15 characters or less");
  });

  it("with too short password, displays must be at least 8 characters error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="password"]').type("passwor");
    cy.get('[data-cy="confirm-password"]').type("passwor");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Password must be at least 8 charaters.");
  });

  it("with non matching passwords, displays passwords must match error", () => {
    cy.mount(<SignUpForm />)
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="confirm-password"]').type("passwoyr");
    cy.get('[data-cy="signup-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Password must match.");
  });
});
