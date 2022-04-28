/// <reference types="cypress" />


describe('R8UC1A', () => {
    before(() => {
        cy.visit('localhost:3000')
        cy.contains("Have no account yet? Click here to sign up.").click()
        cy.get('.inputwrapper #email').type('test@test.com')
        cy.get('.inputwrapper #firstname').type('test')
        cy.get('.inputwrapper #lastname').type('test')
        cy.contains("Sign Up").click()
    })

    beforeEach(() => {
        cy.visit('localhost:3000')
        cy.get('.inputwrapper #email').type('test@test.com')
        cy.get('.submit-form').find('input[type=submit]').click()
    })

    it('Should be in task creator view', () => {
        cy.get('.inputwrapper #title').type('testTask')
        cy.contains('Create new Task').click()
        cy.contains('testTask').click()
        cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('newTodo')
        cy.contains('Add').click()
        cy.get('div').get('.todo-list').find('todos')
    })

})
