describe("login", () => {
  it("with valid credentials, returns username", () => {
    cy.intercept('POST', '/auth/login', { username: "admiral_1" }).as("loginRequest")
    cy.visit('/login')
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="login-submit"]').click();
    cy.wait('@loginRequest').then( interception => {
      expect(interception.response.body.username).to.eq("admiral_1")
    })
    cy.url().should("include", "/");
  });

  it("with invalid password, returns an incorrect password message", () => {
    cy.intercept('POST', '/auth/login', { error: "Incorrect password." }).as("loginRequest")
    cy.visit('/login')
    cy.get('[data-cy="username"]').type("admiral_1");
    cy.get('[data-cy="password"]').type("passwordX");
    cy.get('[data-cy="login-submit"]').click();
    cy.wait('@loginRequest')
    cy.url().should("include", "/login");
    cy.get('[data-cy="error-message"]').should('contain.text', "Incorrect password.");
  });

  it("with invalid username, returns an incorrect password message", () => {
    cy.intercept('POST', '/auth/login', { error: "Incorrect username." }).as("loginRequest")
    cy.visit('/login')
    cy.get('[data-cy="username"]').type("admiral_X");
    cy.get('[data-cy="password"]').type("password");
    cy.get('[data-cy="login-submit"]').click();
    cy.wait('@loginRequest')
    cy.url().should("include", "/login");
    cy.get('[data-cy="error-message"]').should('contain.text', "Incorrect username.");
  });
});