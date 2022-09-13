//p67
const FindMaximumValue = (datas: Array<number>) => {
    let max = datas[0]

    for (const data of datas) {
        if (max < data) {
            max = data
        }
    }

    return max
}

const datas = [540, -238, 190, 22, -645, 832, 777, -542, 0, 395]
const result = FindMaximumValue(datas)

console.log(`最大値 = ${result}`)

// console.log(`最大値 = ${Math.max(...datas)}`)