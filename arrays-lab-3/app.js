
// Create uniqueWords function here
function uniqueWords(data) {
    var regex = /[,;:_'"\.\?!]/g;

    data = data.replace(regex, "");
    data = data.replace(/<br>/g, " ");

    data = data.toLowerCase();

    var words = data.split(" ");

    var unique = [];

    for (var i = 0; i < words.length; i++) {
        if (words.indexOf(words[i]) === words.lastIndexOf(words[i])) { unique.push(i); }
    }

    return unique;
}

// Don't change any of the code below
test.uniqueWords = uniqueWords;