import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const LinearSearch = (datas: Array<number>, target: any) => {
    let result = -1
    for (let i = 0; i < datas.length; i++) {
        if (datas[i] == Number(target)) {
            result = i
            break
        }
    }

    return result
}





const datas = [35, 80, 21, 54, 11, 92, 23, 2, 67, 45]

console.log('文字列を入力してください')
const target = readInterface.question('>', (target: any) => {
    const result = LinearSearch(datas, target)
    readInterface.close()
    if (result == -1) {
        console.log("目的の値は見つかりませんでした")
    } else {
        console.log(`目的の値の添え字は${result}です。`)
    }
})













