import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const f =(x: number)=>{
    return x*x + 5.0 * x + 6.0
}

const TrapezoidalRule = (valueA:number, valueB:number) =>{

    const N = 10000

    const dx = (valueB - valueA)/N
    let s = (f(valueA) + f(valueB)) / 2.0

    for (let i = 1; i <= N -1; i++){
        s += f(valueA + dx * i)
    }

    s *= dx

    return s
}


readInterface.question('定積分する区間Aを入力してください',(n:string)=>{

    const valueA = Number(n)

    readInterface.question('定積分する区間Bを入力してください',(n:string)=>{
        readInterface.close()
    
        const valueB = Number(n)

        try{
            const result = TrapezoidalRule(valueA, valueB)
            console.log(`近似値は${result}です。`)
        }
        catch(e){
            console.log(e)
        }
    })
})

