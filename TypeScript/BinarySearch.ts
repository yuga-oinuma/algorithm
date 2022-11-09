import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const BinarySearch=(datas: Array<number>, target: number)=>{
    let result:number = -1
    let head:number = 0
    let tail:number = datas.length - 1
    while(result == -1 && head <= tail){
        let middle:number = (head + tail)/2
        if( datas[middle] == target){
            result = middle
        }else if(datas[middle] < target){
            head = middle + 1
        }else{
            tail = middle -1
        }
    }

    return result
}


const datas:Array<number> = [2, 10, 21, 28, 33, 54, 60, 63, 71, 79, 82, 87, 88, 94, 97]

console.log('探索する値を入力してください')
const target = readInterface.question('>', (target: string) => {
    const result = BinarySearch(datas, Number(target))
    readInterface.close()
    if (result == -1) {
        console.log("目的の値は見つかりませんでした")
    } else {
        console.log(`目的の値の添え字は${result}です。`)
    }
})