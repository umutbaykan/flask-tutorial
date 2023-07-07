import LoginForm from "./LoginForm";

describe("Login form frontend validations", () => {
  it("with missing password, displays password required error", () => {
    cy.mount(<LoginForm />)
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="login-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Password is required.");
  });

  it("with missing username, displays required error", () => {
    cy.mount(<LoginForm />)
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="login-submit"]').click();
    cy.get('[data-cy="error-message"]').should('contain.text', "Required");
  });
});
