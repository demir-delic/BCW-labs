test.tests = ()=> {
    describe('Test Data', ()=> {
        it('Exists', () => {
            assert.isDefined(test.data);
        });
        it('Is An Array', () => {
            assert.isArray(test.data);
        });
        it('Contains 5 Strings', () => {
            assert.isTrue(test.data.length === 5);
        });
    });

    describe('getCharacter13', () => {
        it('Exists', () => {
            assert.isDefined(test.getCharacter13);
        });
        it('Is A Function', () => {
            assert.isFunction(test.getCharacter13);
        });
        it('Returns The 13th Character', () => {
            assert.equal(test.getCharacter13(test.data[0]), 'k');
            assert.equal(test.getCharacter13(test.data[1]), 'u');
            assert.equal(test.getCharacter13(test.data[2]), ' ');
            assert.equal(test.getCharacter13(test.data[3]), 'h');
            assert.equal(test.getCharacter13(test.data[4]), 't');
        });
    });

    describe('endsWithPastrami', () => {
        it('Exists', () => {
            assert.isDefined(test.endsWithPastrami);
        });
        it('Is A Function', () => {
            assert.isFunction(test.endsWithPastrami);
        });
        it('Returns True If Argument Ends With Pastrami', () => {
            assert.equal(test.endsWithPastrami(test.data[0]), true);
            assert.equal(test.endsWithPastrami(test.data[1]), false);
            assert.equal(test.endsWithPastrami(test.data[2]), false);
            assert.equal(test.endsWithPastrami(test.data[3]), true);
            assert.equal(test.endsWithPastrami(test.data[4]), false);
        });
    });

    describe('includesTurducken', () => {
        it('Exists', () => {
            assert.isDefined(test.includesTurducken);
        });
        it('Is A Function', () => {
            assert.isFunction(test.includesTurducken);
        });
        it('Returns True If Argument Includes Turducken', () => {
            assert.equal(test.includesTurducken(test.data[0]), false);
            assert.equal(test.includesTurducken(test.data[1]), true);
            assert.equal(test.includesTurducken(test.data[2]), false);
            assert.equal(test.includesTurducken(test.data[3]), true);
            assert.equal(test.includesTurducken(test.data[4]), true);
        });
    });

    describe('firstShankle', () => {
        it('Exists', () => {
            assert.isDefined(test.firstShankle);
        });
        it('Is A Function', () => {
            assert.isFunction(test.firstShankle);
        });
        it('Returns The Index Of The First Shankle', () => {
            assert.equal(test.firstShankle(test.data[0]), 8);
            assert.equal(test.firstShankle(test.data[1]), 0);
            assert.equal(test.firstShankle(test.data[2]), -1);
            assert.equal(test.firstShankle(test.data[3]), -1);
            assert.equal(test.firstShankle(test.data[4]), 49);
        });
    });

    describe('yayBacon', () => {
        it('Exists', () => {
            assert.isDefined(test.yayBacon);
        });
        it('Is A Function', () => {
            assert.isFunction(test.yayBacon);
        });
        it('Returns Argument With Bacon Replaced', () => {
            
            var regex = /YAY BACON!/gi;

            assert.equal(countSubstring(test.yayBacon(test.data[0]), regex), 2);
            assert.equal(countSubstring(test.yayBacon(test.data[1]), regex), 2);
            assert.equal(countSubstring(test.yayBacon(test.data[2]), regex), 3);
            assert.equal(countSubstring(test.yayBacon(test.data[3]), regex), 2);
            assert.equal(countSubstring(test.yayBacon(test.data[4]), regex), 2);
        });
    });

    describe('baconCount', () => {
        it('Exists', () => {
            assert.isDefined(test.baconCount);
        });
        it('Is A Function', () => {
            assert.isFunction(test.baconCount);
        });
        it('Returns The Count Of Bacon In Argument', () => {            
            assert.equal(test.baconCount(test.data[0]), 2);
            assert.equal(test.baconCount(test.data[1]), 2);
            assert.equal(test.baconCount(test.data[2]), 3);
            assert.equal(test.baconCount(test.data[3]), 2);
            assert.equal(test.baconCount(test.data[4]), 2);
        });
    });

}

function countSubstring(text, regex) {
    return text.match(regex).length;
}