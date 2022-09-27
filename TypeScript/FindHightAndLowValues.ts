//p79

import * as readline from 'readline'
const MAX = 9999
const MIN = -9999
const datas = [20, 29, 30, 44, 51, 66, 72, 78, 80, 87]

const FindHighAndLowValues = () => {
    const readInterface = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    })

    console.log('数値M (1~100)を指定してください')
    const data = readInterface.question('>', (data) => {
        const high = higher(Number(data))
        const low = lower(Number(data))
        console.log(`${data}より大きい値は`)
        if (high == MAX) {
            console.log('ありませんでした')
        } else {
            console.log(`${high}です。`)
        }

        console.log(`${data}より小さい値は`)
        if (low == MIN) {
            console.log('ありませんでした')
        } else {
            console.log(`${low}です。`)
        }

        readInterface.close()
    })

}


const higher = (data: number) => {
    datas[datas.length + 1] = MAX
    let i = 0
    while (datas[i] <= data) {
        i++
    }
    return datas[i]
}

const lower = (data: number) => {
    datas[datas.length + 1] = MIN
    let i = 0
    while (datas[i] >= data) {
        i++
    }
    return datas[i]
}

FindHighAndLowValues()

// const otherMethod = () => {
//     const readInterface = readline.createInterface({
//         input: process.stdin,
//         output: process.stdout
//     })

//     console.log('数値M (1~100)を指定してください')
//     readInterface.question('>', (data) => {
//         const high = datas.find(value => {
//             return value >= Number(data)
//         })

//         const low = datas.find(value => {
//             return value <= Number(data)
//         })

//         console.log(`${data}より大きい値は`)
//         if (typeof (high) == 'undefined') {
//             console.log('ありませんでした')
//         } else {
//             console.log(`${high}です。`)
//         }

//         console.log(`${data}より小さい値は`)
//         if (typeof (low) == 'undefined') {
//             console.log('ありませんでした')
//         } else {
//             console.log(`${low}です。`)
//         }

//         readInterface.close()
//     })
// }

// otherMethod()