

class Student {
  fullName: string;
  constructor(public firstName, public middleInitial, public lastName) {
    this.fullName = firstName + '' + middleInitial + '' + lastName;
  }
}
interface Person {
  firstName: string;
  lastName: string;
}
function greeter (person: Person) {
  return 'hellow,' + person.firstName + '' + person.lastName;
}
var user = new Student('jane', 'M.', 'User');

console.log(greeter(user));

let list: number[] = [1, 2, 3]

let list2: Array<number | string> = [1,2,3, 'sd']

let someValue: any = 'sddd' 
let strLength: number = (someValue as string).length

let aa: string = `ad`;
let age: number = 13;
let message: string = `${ aa } is ${ age + 1 } years old`
console.log(message)

function f([first, second]: [number, number]) {
  console.log(first);
  console.log(second);
}

let [first, ...rest] = [1, 2, 3, 4];
console.log(first);
console.log(rest);
let o = {
  a: 11,
  b: 2
}
let {a, b}: {a: number,  b: number} = o;
