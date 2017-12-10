test.tests = ()=> {
    describe('Test Data', ()=> {
        it('Exists', () => {
            assert.isDefined(test.data);
        });
        it('Is An Array', () => {
            assert.isArray(test.data);
        });
        it('Contains 10 Contacts', () => {
            assert.isTrue(test.data.length === 10);
        });
    });

    describe('allAreLegalAge', () => {
        it('Exists', () => {
            assert.isDefined(test.allAreLegalAge);
        });
        it('Is A Function', () => {
            assert.isFunction(test.allAreLegalAge);
        });
        it('Checks All Contact Ages', () => {
            assert.isTrue(test.allAreLegalAge(test.data));
        });
    });

    describe('femaleFilter', () => {
        it('Exists', () => {
            assert.isDefined(test.femaleFilter);
        });
        it('Is A Function', () => {
            assert.isFunction(test.femaleFilter);
        });
        it('Returns Only Females', () => {

            let females = test.femaleFilter(test.data);
            assert.isDefined(females, 'test.femaleFilter did not return anything.');
            assert.isArray(females, 'test.femaleFilter did not return an array.');

            let male = females.find(item => {
                return item.gender === 'Male';
            });

            assert.isUndefined(male, 'test.femaleFilter returned a Male.');
        });
    });

    describe('overFiftyFilter', () => {
        it('Exists', () => {
            assert.isDefined(test.overFiftyFilter);
        });
        it('Is A Function', () => {
            assert.isFunction(test.overFiftyFilter);
        });
        it('Returns Only Contacts Over 50', () => {

            let seniors = test.overFiftyFilter(test.data);
            assert.isDefined(seniors, 'test.overFiftyFilter did not return anything.');
            assert.isArray(seniors, 'test.overFiftyFilter did not return an array.');

            let nonSenior = seniors.find(item => {
                return item.age < 51;
            });

            assert.isUndefined(nonSenior, 'test.overFiftyFilter returned a contact younger than 51.');
        });
    });

    describe('findFirstThomas', () => {
        it('Exists', () => {
            assert.isDefined(test.findFirstThomas);
        });
        it('Is A Function', () => {
            assert.isFunction(test.findFirstThomas);
        });
        it('Returns The First Thomas', () => {

            let contact = test.findFirstThomas(test.data);
            assert.isDefined(contact, 'test.findFirstThomas did not return anything.');
            assert.isNotArray(contact, 'test.findFirstThomas returned an array. It should return a single object.');
            assert.equal(contact.lastName, 'Berry', 'test.findFirstThomas returned the wrong Thomas.');
        });
    });

    describe('fullNames', () => {
        it('Exists', () => {
            assert.isDefined(test.fullNames);
        });
        it('Is A Function', () => {
            assert.isFunction(test.fullNames);
        });
        it('Returns All Full Names', () => {

            let names = test.fullNames(test.data);
            assert.isDefined(names, 'test.fullNames did not return anything.');
            assert.isArray(names, 'test.fullNames did not return an array.');
            assert.equal(names.length, 10, 'test.fullNames returned an array with an incorrect length.');
            assert.equal(names[0], 'Billy Welch', 'test.fullNames returned invalid data.');
            assert.equal(names[3], 'Joan Day', 'test.fullNames returned invalid data.');
            assert.equal(names[7], 'Diane Alexander', 'test.fullNames returned invalid data.');
        });
    });

}