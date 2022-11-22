import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const GetGCD=(x:number, y:number)=>{
    let result  = 0

    if (y == 0){
        result = x
    }else{
        result = GetGCD(y, x % y)
    }

    return result

}


readInterface.question('1つ目の整数を入力してください',(x:string)=>{
    readInterface.question('2つ目の整数を入力してください', (y:string)=>{
        readInterface.close()
        const X = Number(x)
        const Y = Number(y)

        try{
            const result = GetGCD(X, Y)
            console.log(`${x}と${y}の最大公約数は${result}です`)
        }
        catch(e){
            console.log(e)
        }
    })

})