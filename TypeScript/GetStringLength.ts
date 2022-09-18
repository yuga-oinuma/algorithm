// p76
const GetStringLength =async()=>{
    let len:number = 0
    let data:Array<string>=[]

    const readInterface = require(`readline/promises`).createInterface({
        input: process.stdin,
        output: process.stdout
    })

    console.log('文字列を入力してください')
    data = [...(await readInterface.question('>'))]

    while(typeof(data[len])!=="undefined"){
        len ++
    }

    readInterface.close()
    return len
}

(async()=>{
    const result = await GetStringLength()
    console.log(`文字長 = ${result}`)
})();


// const otherMethod =async()=>{
//     console.log('文字列を入力してください')
//     const data:string = await readInterface.question('>')

    
//     console.log(`文字長 = ${data.length}`)
//     readInterface.close()

//     return
// }

// otherMethod()