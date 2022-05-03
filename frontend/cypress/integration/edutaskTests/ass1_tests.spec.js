/// <reference types="cypress" />


describe('R8UC1A', () => {

  // delete account and create a new one via the API, then visit the main page and login before each test.
  beforeEach(() => {
    cy.visit('localhost:3000');
    // get user ID so we can delete it if it exists.
    cy.request({
      url: 'http://localhost:5000/users/bymail/test@test.com',
      failOnStatusCode: false
    }).then((response) => {
        // Only delete account if we found an account
      cy.log("status: ", response.status);
      if (response.status === 200){
          var userData = response.body;
          var userId = userData._id.$oid;
          cy.log("userId: ", userId);
          // delete account
          var deleteUrl = "http://localhost:5000/users/" + userId;
          cy.request('DELETE', deleteUrl);
        }
    });

    // create new account
    cy.request({
      method: 'POST',
      url: 'http://localhost:5000/users/create', // baseUrl is prepend to URL
      form: true, // indicates the body should be form urlencoded and sets Content-Type: application/x-www-form-urlencoded headers
      body: {
        email: 'test@test.com',
        firstName: 'test',
        lastName: 'test',
      },
    });

    // login
    cy.get('.inputwrapper #email').type('test@test.com');
    cy.get('.submit-form').find('input[type=submit]').click();
  });

  it('Should be in task creator view', () => {
    cy.get('.inputwrapper #title').type('testTask');
    cy.contains('Create new Task').click();
    cy.contains('testTask').click();
    cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('newTodo');
    cy.contains('Add').click();
    cy.wait(500);
    cy.get('div').get('.todo-list').get('li').get('.todo-item').each(($li, index, $lis) => { }).last().should('have.text', 'newTodo✖');
  });

  it('test test test', () => {
    cy.get('.inputwrapper #title').type('testTask');
    cy.contains('Create new Task').click();
    cy.contains('testTask').click();
    cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('newTodo');
    cy.contains('Add').click();
    cy.wait(500);
    cy.get('div').get('.todo-list').get('li').get('.todo-item').each(($li, index, $lis) => { }).last().should('have.text', 'newTodo✖');
  });

});

