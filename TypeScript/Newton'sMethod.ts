import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})


const NewtonsMethod = (value: number) =>{
    
    if(value < 0){
        throw new Error('1以上の整数を入力してください')
    }

    const MAXLOOP = 100
    const EV = 0.0000001
    
    let x0 = value
    let x1 = 0

    let delta = EV

    for(let i = 0; i < MAXLOOP && Math.abs(delta) >= EV; i++){

        delta = (x0 * x0 - value)/(2.0 * x0)
        x1 = x0 - delta
        x0 = x1
    }

    return x1
}

readInterface.question('平方根を求める数値を入力してください',(n:string)=>{
    readInterface.close()

    const value = Number(n)

    try{
        const result = NewtonsMethod(value)
        console.log(`${value}の平方根(近似値)は${result}です。`)
    }
    catch(e){
        console.log(e)
    }
})