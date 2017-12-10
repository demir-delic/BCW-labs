test.tests = ()=> {
    
        describe('square', () => {
            it('Is A Function', () => {
                assert.isFunction(test.square);
            });
            it('Returns The Square Of A Number', () => {
                assert.equal(test.square(2), 4);
                assert.equal(test.square(3), 9);
                assert.equal(test.square(4), 16);
                assert.equal(test.square(5), 25);
            });
        });
    
        describe('add', () => {
            it('Is A Function', () => {
                assert.isFunction(test.add);
            });
            it('Returns The Sum Of Two Numbers', () => {
                assert.equal(test.add(1, 2), 3);
                assert.equal(test.add(10, 12), 22);
                assert.equal(test.add(25, 25), 50);
            });
        });
    
        describe('difference', () => {
            it('Is A Function', () => {
                assert.isFunction(test.difference);
            });
            it('Returns The Difference Of Two Numbers', () => {
                assert.equal(test.difference(5, 10), 5);
                assert.equal(test.difference(10, 5), 5);
                assert.equal(test.difference(10, 13), 3);
                assert.equal(test.difference(13, 10), 3);
            });
        });
    
        describe('formula', () => {
            it('Is A Function', () => {
                assert.isFunction(test.formula);
            });
            it('Returns The Difference Of The Square Of One Number And The Sum Of Two Numbers', () => {
                assert.equal(test.formula(2, 3, 4), 3);
                assert.equal(test.formula(5, 6, 7), 12);
                assert.equal(test.formula(8, 9, 10), 45);
            });
        });
    
        describe('total', () => {
            it('Is A Function', () => {
                assert.isFunction(test.total);
            });
            it('Returns The Sum Of Multiple Numbers', () => {
                assert.equal(test.total(2, 3), 5);
                assert.equal(test.total(2, 3, 4), 9);
                assert.equal(test.total(2, 3, 4, 5), 14);
            });
        });
    
        describe('fullName', () => {
            it('Is A Function', () => {
                assert.isFunction(test.fullName);
            });
            it('Returns Two String Concatenated With A Space Between Them', () => {
                assert.equal(test.fullName('Wonder', 'Woman'), 'Wonder Woman');
                assert.equal(test.fullName('Mighty', 'Mouse'), 'Mighty Mouse');
            });
        });
    
        describe('longestName', () => {
            it('Is A Function', () => {
                assert.isFunction(test.longestName);
            });
            it('Returns The Longest Name As Determined By Comparing Combinations Of Three Strings', () => {
                assert.equal(test.longestName('Joe', 'King', 'Kong'), 'King Kong'); //midLast
                assert.equal(test.longestName('Mecha', 'Godzilla', 'Tim'), 'Mecha Godzilla'); //firstMid
                assert.equal(test.longestName('Kelly', 'Git', 'Kraken'), 'Kelly Kraken'); //firstLast
            });
        });
    
    }
    