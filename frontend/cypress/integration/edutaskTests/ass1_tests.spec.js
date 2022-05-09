/// <reference types="cypress" />


describe('R8UC1', () => {

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
      if (response.status === 200) {
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
      url: 'http://localhost:5000/users/create',
      form: true,
      body: {
        email: 'test@test.com',
        firstName: 'test',
        lastName: 'test',
      },
    });

    // Create testTask
    // get user ID again so we can create a new task
    cy.request({
      url: 'http://localhost:5000/users/bymail/test@test.com',
      failOnStatusCode: false
    }).then((response) => {
      // Only create task if we found an account
      cy.log("status: ", response.status);
      if (response.status === 200) {
        var userData = response.body;
        var userId = userData._id.$oid;
        cy.log("userId: ", userId);
        // Create task
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/tasks/create',
          form: true,
          body: {
            title: 'testTask',
            description: '(add a description here)',
            userid: userId,
            url: '',
            todos: 'Watch video',
          },
        });
      }
    });

    // login
    cy.get('.inputwrapper #email').type('test@test.com');
    cy.get('.submit-form').find('input[type=submit]').click();
    // create task and open it
    cy.contains('testTask').click();
  });

  it('Test 1. Enter new todo "newTodo" and add it', () => {
    // create todo "newTodo"
    cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('newTodo');
    cy.contains('Add').click();
    cy.wait(500); // wait to let the list update
    // check that our todo exists
    cy.get('div').get('.todo-list').get('li').get('.todo-item')
      .each(($li, index, $lis) => { }).last().find('.editable').should('have.text', 'newTodo');
  });

  it('Test 2. Click add without typing a todo name', () => {
    // Try to create todo without entering a name
    cy.contains('Add').click();
    // Border should turn red since we have not entered any text.
    cy.get('div').get('.todo-list').get('li').get('.inline-form')
      .find('input[type=text]').should('have.css', 'border-color', 'red');
  });


});

describe('R8UC2: Test 1', () => {

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
      if (response.status === 200) {
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
      url: 'http://localhost:5000/users/create',
      form: true,
      body: {
        email: 'test@test.com',
        firstName: 'test',
        lastName: 'test',
      },
    });

    // Create testTask
    // get user ID again so we can create a new task
    cy.request({
      url: 'http://localhost:5000/users/bymail/test@test.com',
      failOnStatusCode: false
    }).then((response) => {
      // Only create task if we found an account
      cy.log("status: ", response.status);
      if (response.status === 200) {
        var userData = response.body;
        var userId = userData._id.$oid;
        cy.log("userId: ", userId);
        // Create task
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/tasks/create',
          form: true,
          body: {
            title: 'testTask',
            description: '(add a description here)',
            userid: userId,
            url: '',
            todos: 'Watch video',
          },
        }).then((response) => {
          var taskData = response.body[0];
          cy.log("taskData:", taskData);
          var taskId = taskData._id.$oid;
          var todoId = taskData.todos[0]._id.$oid;
          cy.log("taskId:", taskId);
          cy.log("todoId:", todoId);
          // Set the todo as DONE, so it's already struck-through when test visits task
          var todoUrl = "http://localhost:5000/todos/byid/" + todoId;
          cy.request({
            method: 'PUT',
            url: todoUrl,
            form: true,
            body: {
              data: "{'$set': {'done': true}}",
            },
          });
        });
      }
    });

    // login
    cy.get('.inputwrapper #email').type('test@test.com');
    cy.get('.submit-form').find('input[type=submit]').click();
    // Open testTask
    cy.contains('testTask').click();
  });

  it('Test 1. Click radio button to unstruck todo item', () => {
    // Mark last todo as done, struck-through.
    cy.get('.todo-list').find('.todo-item').find('.checker').click();
    // Uncheck it and assert if it worked.
    cy.get('.todo-list').find('.todo-item').find('.editable').should('have.css', "text-decoration", "none solid rgb(49, 46, 46)");
  });

});

describe('R8UC2: Test 2', () => {

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
      if (response.status === 200) {
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
      url: 'http://localhost:5000/users/create',
      form: true,
      body: {
        email: 'test@test.com',
        firstName: 'test',
        lastName: 'test',
      },
    });

    // Create testTask
    // get user ID again so we can create a new task
    cy.request({
      url: 'http://localhost:5000/users/bymail/test@test.com',
      failOnStatusCode: false
    }).then((response) => {
      // Only create task if we found an account
      cy.log("status: ", response.status);
      if (response.status === 200) {
        var userData = response.body;
        var userId = userData._id.$oid;
        cy.log("userId: ", userId);
        // Create task
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/tasks/create',
          form: true,
          body: {
            title: 'testTask',
            description: '(add a description here)',
            userid: userId,
            url: '',
            todos: 'Watch video',
          },
        });
      }
    });

    // login
    cy.get('.inputwrapper #email').type('test@test.com');
    cy.get('.submit-form').find('input[type=submit]').click();
    // create task and open it
    cy.contains('testTask').click();
  });

  it('Test 2. Click radio button to show struck-through on todo item', () => {
    // Mark last todo as done, struck-through.
    cy.get('.todo-list').find('.todo-item').find('.checker').click();
    // Assert if it worked.
    cy.get('.todo-list').find('.todo-item').find('.editable').should('have.css', "text-decoration", "line-through solid rgb(49, 46, 46)");
  });


});

describe('R8UC3: Test 1', () => {

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
      if (response.status === 200) {
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
      url: 'http://localhost:5000/users/create',
      form: true,
      body: {
        email: 'test@test.com',
        firstName: 'test',
        lastName: 'test',
      },
    });

    // Create testTask
    // get user ID again so we can create a new task
    cy.request({
      url: 'http://localhost:5000/users/bymail/test@test.com',
      failOnStatusCode: false
    }).then((response) => {
      // Only create task if we found an account
      cy.log("status: ", response.status);
      if (response.status === 200) {
        var userData = response.body;
        var userId = userData._id.$oid;
        cy.log("userId: ", userId);
        // Create task
        cy.request({
          method: 'POST',
          url: 'http://localhost:5000/tasks/create',
          form: true,
          body: {
            title: 'testTask',
            description: '(add a description here)',
            userid: userId,
            url: '',
            todos: 'Watch video',
          },
        });
      }
    });

    // login
    cy.get('.inputwrapper #email').type('test@test.com');
    cy.get('.submit-form').find('input[type=submit]').click();
    // create task and open it
    cy.contains('testTask').click();
  });

  it('Test 1. Click the X to remove the todo from the todo-list', () => {
    // Click the X on the todo item
    cy.get('.todo-list').find('.todo-item').find('.remover').click();
    cy.wait(500); // wait to let the list update
    // Assert if it was removed (list should be empty)
    cy.get('.todo-list').find('.todo-item').should('not.exist');
  });


});

