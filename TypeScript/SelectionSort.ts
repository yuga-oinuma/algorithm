const datas = [35, 80, 21, 54, 11, 45, 92, 39]
let valueMin: number

const dispArray = () => {
    for (let value of datas) {
        console.log(`${value}`)
    }
}

console.log("ソートする前の要素値の並び")
dispArray()

for (let i = 0; i < datas.length - 1; i++) {
    let indexMin: number = i
    for (let j = i + 1; j < datas.length; j++) {
        if (datas[j] < datas[indexMin]) {
            indexMin = j
        }
    }
    valueMin = datas[indexMin]
    datas[indexMin] = datas[i]
    datas[i] = valueMin
}

console.log("ソートした後の要素の並び")
dispArray()

//other method
// console.log("ソートする前の要素値の並び")
// dispArray()
// datas.sort()
// console.log("ソートする後の要素値の並び")
// dispArray()


