## Array Accessors Lab

---

### Goal
* The goal of this lab is to find all the unique words in Edgar Allen Poe's "The Raven".

### Tips
* Use string and array methods to complete each task (<a href="https://www.w3schools.com/jsref/jsref_obj_string.asp" target="_blank">String Reference</a>, <a href="https://www.w3schools.com/jsref/jsref_obj_array.asp" target="_blank">Array Reference</a>).
* Create the function in the app.js file.
* Make sure the function receives one parameter. Example: `function someFunction(data) { ... }`

### Tasks

* Create a function named `uniqueWords` that accepts a string parameter and returns an array of the unique words.
* Follow these steps:
    1. Remove all punctuation from the text: (, ; : _ ' " . ? !). Use `/\./g` to find periods and `/\?/g` to find question marks.
    2. Replace all `<br>` tags with a space.
    3. Convert the entire text to lower case.
    4. Split the text into an array using the spaces as the delimiters.
    5. For each word in the array, find the first and last index of the word in the array. If the first and last index values are equal, the word is unique; push it into an array of unique words.
    6. Sort and return the array of unique words.