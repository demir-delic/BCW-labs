
// Create square function here
function square(a) {
    return a * a;
}

// Create add function here
function add(a, b) {
    return a + b;
}

// Create difference function here
function difference(a, b) {
    if (a > b) {
        return a - b;
    }
    else {
        return b - a;
    }
}

// Create formula function here
function formula (a, b, c) {
    var sq = square(a);
    var sum = add(b, c);
    return difference(sq, sum);
}

// Create total function here
function total () {
    var sum = 0;
    for (var i = 0; i < arguments.length; i++){
        sum += arguments[i];
    }
    return sum;
}

// Create fullName function here
function fullName (first, last) {
    return `${first} ${last}`;
}

// Create longestName function here
function longestName (first, middle, last) {
    var firstMid = fullName(first, middle);
    var midLast = fullName(middle, last);
    var firstLast = fullName(first, last);

    if ((firstMid.length > midLast.length) && 
        (firstMid.length > firstLast.length)) {
        return firstMid;
    }
    else if ((midLast.length > firstMid.length) && 
             (midLast.length > firstLast.length)) {
        return midLast;
    }
    else {
        return firstLast;
    }
}


// Don't change any of the code below
var square;
var add;
var difference;
var formula;
var total;
var fullName;
var longestName;

test.square = square;
test.add = add;
test.difference = difference;
test.formula = formula;
test.total = total;
test.fullName = fullName;
test.longestName = longestName;