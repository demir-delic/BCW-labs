test.tests = () => {
    describe('Test Data', () => {
        it('Exists', () => {
            assert.isDefined(test.data);
        });
        it('Is A String', () => {
            assert.isString(test.data);
        });
        it('Contains 6556 Characters', () => {
            assert.equal(test.data.length, 6556);
        });
    });

    describe('uniqueWords', () => {
        it('Exists', () => {
            assert.isDefined(test.uniqueWords);
        });
        it('Is A Function', () => {
            assert.isFunction(test.uniqueWords);
        });
        it('Returns An Array Of 274 Words', () => {

            var words = test.uniqueWords(test.data);

            assert.isDefined(words, 'test.uniqueWords did not return anything.');
            assert.isArray(words, 'test.uniqueWords did not return an array.');
            assert.equal(words.length, 274, 'test.uniqueWords returned an array with the wrong length.');
        });
    });

}