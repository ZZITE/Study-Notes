import { Equal, Expect } from "./utils"

// 期望是一个 string 类型
// type HelloWorld = any
// 你需要使得如下这行不会抛出异常
type test = Expect<Equal<HelloWorld, string>>

// answer 
type HelloWorld = string;