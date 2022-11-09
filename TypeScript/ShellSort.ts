// p106
const ShellSort = (datas: Array<number>) => {
    let span = datas.length / 2
    while (span > 0) {
        for (let i = 0; i < span; i++) {
            datas = InsertionSort(datas)
        }
        span /= 2
    }
    return datas
}

const InsertionSort = (datas: Array<number>) => {
    for (let i = 1; i < datas.length; i++) {
        let temp = datas[i]
        let j = i - 1
        while (j >= 0 && datas[j] > temp) {
            datas[j + 1] = datas[j]
            j -= 1
        }
        datas[j + 1] = temp
    }
    return datas
}

let datas: number[] = new Array
for (let i = 0; i < 10; i++) {
    datas.push(Math.floor(Math.random() * 100))
}

const sortedNums = ShellSort(datas.concat())

console.log('ソート前の要素の並び')
console.log(datas)
console.log('ソート後の要素の並び')
console.log(sortedNums)

