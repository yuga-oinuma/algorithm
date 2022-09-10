// p71
const FindMinimumValue = (datas: Array<number>) => {
    let min = 9999999

    for (const data of datas) {
        if (min > data) {
            min = data
        }
    }
    return min
}

const datas = [540, -238, 190, 22, -645, 832, 777, -542, 0, 395]
const result = FindMinimumValue(datas)

console.log(`最小値 = ${result}`)

console.log(`最小値 = ${Math.min(...datas)}`)