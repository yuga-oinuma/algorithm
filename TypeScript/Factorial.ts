import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const Factorial=(n:number)=>{

    if(n < 0){
        throw new Error('1以上の整数を入力してください')
    }
    let result:number
    if(n == 1){
        result = 1
    }else{
        result = n * Factorial(n - 1)
    }

    return result
}

readInterface.question('整数を入力してください',(n:string)=>{
    readInterface.close()

    const N = Number(n)

    try{
        const result = Factorial(N)
        console.log(`${N}の階乗は${result}です`)
    }
    catch(e){
        console.log(e)
    }
})