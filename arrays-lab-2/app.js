
// Create separateByGender function here
function separateByGender (data) {
    test.males = [];
    test.females = [];
    data.forEach(item => { (item.gender === "Male") ? test.males.push(item) : test.females.push(item); })
}


// Create lastNameSort function here

function lastNameSort (data) {
    //data.sort((a, b) => { return a.lastName.localeCompare(b.lastName); });
    data.sort((a, b) => { return (a.lastName > b.lastName) ? 1 : 0; })
}


// Don't change any of the code below
test.separateByGender = separateByGender;
test.lastNameSort = lastNameSort;