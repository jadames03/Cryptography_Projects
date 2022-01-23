function encrypt(string, number) {
    // creating a func and passing two parameters...string and number(parameter for shifting throughout string).
    var alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    // initializig alphabet to a string of all 26 letters in the alphabet
    var encodedStr = '';
    // initializing encodedStr to an empty string

    if(number > 26){
        number = number % 26;
    }
    /* only 26 letters in the alphabet. if number is greater than 26...then we will mod it.
       so if we wanted to shift our string more than 26 times. it will always have a range from 0-26*/
    var i = 0;
    // setting our counter to 0
    while (i < string.length) {
        // a loop that executes i number of times depending on string length
        if (alphabet.indexOf(string[i]) !== -1) {
            // finding alphabet index
            const alphabetIndex = alphabet.indexOf(string[i]);
            // storing that index inside of alphabetIndex
            if (alphabet[alphabetIndex + number]) {
                // when alphabet index is in range
                encodedStr += alphabet[alphabetIndex + number];
                // append to our empty string
            }
            else {
                // when alphabet index is not in range
                encodedStr += alphabet[alphabetIndex + number - 26]
                // append to our empty string
            }
        }
        i++
        // add 1 to the counter
    }
    return encodedStr;
    // return the empty string that should not be empty anymore :)
}

console.log(encrypt('HSQRGL',2));
// log our output