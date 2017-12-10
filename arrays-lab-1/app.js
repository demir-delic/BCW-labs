
// Create allAreLegalAge function here
function allAreLegalAge (data) {
    return data.every(item => { return item.age >= 21; })
}

// Create femaleFilter function here
function femaleFilter (data) {
    return data.filter(item => { return item.gender === "Female"; })
}

// Create overFiftyFilter function here
function overFiftyFilter (data) {
    return data.filter(item => { return item.age > 50; })
}

// Create findFirstThomas function here
function findFirstThomas (data) {
    return data.find(item => { return item.firstName === "Thomas"; })
}

// Create fullNames function here
function fullNames (data) {
    return data.map(item => { return `${item.firstName} ${item.lastName}`; })
}


// Don't change any of the code below
test.allAreLegalAge = allAreLegalAge;
test.femaleFilter = femaleFilter;
test.overFiftyFilter = overFiftyFilter;
test.findFirstThomas = findFirstThomas;
test.fullNames = fullNames;