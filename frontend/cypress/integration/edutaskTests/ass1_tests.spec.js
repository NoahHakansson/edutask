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

    it('When description is put into todo-description field, a new todo should be created', () => {
        cy.get('.inputwrapper #title').type('testTask')
        cy.contains('Create new Task').click()
        cy.contains('testTask').click()
        cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('newTodo')
        cy.contains('Add').click()
        cy.get('div').get('.todo-list').get('li').get('.todo-item').each(($li, index, $lis) => {}).last().should("have.text", "newTodo✖")
    })

    it('When no description is put into todo-description field, input-field border should turn red', () => {
        cy.get('.inputwrapper #title').type('testTask')
        cy.contains('Create new Task').click()
        cy.contains('testTask').click()
        cy.contains('Add').click()
        cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').should('be.required')
        cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').should("be.invalid")
    })

})
