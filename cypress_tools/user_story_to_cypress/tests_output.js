describe('App', {tags: ['@critical']}, () => {
it('User will be able to navigate to the App', {tags:[]}, () => {
// Step 1 login as user

// Step 2 verify thing

});

it('User will be able to see dashboard', {tags:['@tag1', '@tag2']}, () => {
// Step 1 Open app

// Step 2 click a thing

// Step 3 verify another thing

// Step 4 its a step

});


});

describe('App - Area 2', {tags: []}, () => {
beforeEach(() = {
cy.login({url: '/area2'});

});

it('User will be able to navigate to Smart Inbox', {tags:[]}, () => {
// Step 1 verify thing was there

});


});

