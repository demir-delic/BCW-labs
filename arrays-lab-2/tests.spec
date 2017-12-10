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

    describe('separateByGender', () => {
        it('Exists', () => {
            assert.isDefined(test.separateByGender);
        });
        it('Is A Function', () => {
            assert.isFunction(test.separateByGender);
        });
        it('Creates Separate Gender Arrays', () => {

            test.separateByGender(test.data);

            assert.isDefined(test.males, 'test.males is not defined.');
            assert.isDefined(test.females, 'test.females is not defined.');
            assert.isArray(test.males, 'test.males is not an array.');
            assert.isArray(test.females, 'test.females is not an array.');
            assert.equal(test.males.length, 3, 'test.males is the wrong length.');
            assert.equal(test.females.length, 7, 'test.females is the wrong length.');
        });
    });

    describe('lastNameSort', () => {
        it('Exists', () => {
            assert.isDefined(test.lastNameSort);
        });
        it('Is A Function', () => {
            assert.isFunction(test.lastNameSort);
        });
        it('Sorts The Contacts By Last Name', () => {

            test.lastNameSort(test.data);

            assert.isDefined(test.data, 'test.data is not defined.');
            assert.isArray(test.data, 'test.data is not an array.');
            assert.equal(test.data[0].lastName, 'Alexander', 'test.data is not sorted by last name.');
            assert.equal(test.data[9].lastName, 'Welch', 'test.data is not sorted by last name.');
        });
    });

}