it("with valid credentials, returns username", () => {
  cy.intercept('POST', '/auth/login', { username: "admiral_1" }).as("loginRequest")
  cy.get('[data-cy="username"]').type("admiral_1");
  cy.get('[data-cy="password"]').type("password");
  cy.get('[data-cy="login-submit"]').click();
  cy.wait('@loginRequest').then( interception => {
    expect(interception.response.body.username).to.eq("admiral_1")
  })
});

it("with invalid password, returns an incorrect password message", () => {
  cy.intercept('POST', '/auth/login', { error: "admiral_1" }).as("loginRequest")
  cy.mount(<LoginForm />)
  cy.get('[data-cy="username"]').type("admiral_1");
  cy.get('[data-cy="password"]').type("passwordX");
  cy.get('[data-cy="login-submit"]').click();
  cy.url().should("include", "/login");
  cy.get('[data-cy="error-message"]').should('contain.text', "Incorrect password.");
});