var Student = /** @class */ (function () {
    function Student(firstName, middleInitial, lastName) {
        this.firstName = firstName;
        this.middleInitial = middleInitial;
        this.lastName = lastName;
        this.fullName = firstName + '' + middleInitial + '' + lastName;
    }
    return Student;
}());
function greeter(person) {
    return 'hellow,' + person.firstName + '' + person.lastName;
}
var user = new Student('jane', 'M.', 'User');
console.log(greeter(user));
var list = [1, 2, 3];
var list2 = [1, 2, 3, 'sd'];
var someValue = 'sddd';
var strLength = someValue.length;
var aa = "ad";
var age = 13;
var message = aa + " is " + (age + 1) + " years old";
console.log(message);
