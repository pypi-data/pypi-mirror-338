//sync
const fs = require("fs")
const a = fs.readFileSync('./NewWrite.txt', "utf-8")
console.log(a)







//asyn
const fs = require("fs")
fs.readFile("./sample.txt", "utf-8",
(error, data)=>{
if(error){
    throw new Error('Error reading file!')
}
console.log(data)
}
)






//asyn_fun
const fs = require("fs").promises;
async function readFile(){
    try{
        const data = await fs.readFile("sample.txt", "utf-8");
        console.log(data);
    }
    catch(err){
        console.log(err);
    }
}
readFile()
