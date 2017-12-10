// Create getCharacter13 function here
function getCharacter13(text) {
    return text[12];
}

// Create endsWithPastrami function here
function endsWithPastrami(text) {
    return text.endsWith("pastrami.");
}

// Create includesTurducken function here
function includesTurducken(text) {
    return (text.search(/turducken/i) > -1)
}

// Create firstShankle function here
function firstShankle(text) {
    return text.search(/shankle/i);
}

// Create yayBacon function here
function yayBacon(text) {
    return text.replace(/bacon/gi, "YAY BACON!");
}

// Create baconCount function here
function baconCount(text) {
    return text.match(/bacon/gi).length;
}


// Don't change any of the code below
test.getCharacter13 = getCharacter13;
test.endsWithPastrami = endsWithPastrami;
test.includesTurducken = includesTurducken;
test.firstShankle = firstShankle;
test.yayBacon = yayBacon;
test.baconCount = baconCount;