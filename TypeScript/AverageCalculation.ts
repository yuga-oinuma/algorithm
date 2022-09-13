// p63
const AverageCalculation = (datas: Array<number>) => {
    let sum: number = 0
    let count: number = 0
    let average: number = 0.0
    for (const data of datas) {
        sum += data
        count++
    }

    if (count !== 0) {
        average = sum / count
    }

    return { sum, count, average }
}

const datas = [54, 20, 88, 30, 71, 29, 44, 9]
const result = AverageCalculation(datas)

console.log(`合計値 = ${result.sum}, 有効データ数 = ${result.count}, 平均値 = ${result.average} `)

// const sum = datas.reduce((a, x) => { return a + x }, 0)
// console.log(`合計値 = ${sum}, 有効データ数 = ${datas.length}, 平均値 = ${sum / datas.length} `)