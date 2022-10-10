import { reverse } from "dns"

// p97
const datas = [35, 80, 21, 54, 11, 45, 92, 39]

const BubbleSort = (datas: Array<number>) => {
    for (let i = datas.length - 1; i > 0; i--) {
        for (let j = 0; j < datas.length; j++) {
            if (datas[j] < datas[j + 1]) {
                const temp = datas[j]
                datas[j] = datas[j + 1]
                datas[j + 1] = temp
            }
        }
    }
    return datas
}

const dispArray = (datas: Array<number>) => {
    for (let value of datas) {
        console.log(`${value}`)
    }
}

console.log("ソートする前の要素値の並び")
dispArray(datas)

const sortedDatas = BubbleSort(datas)
/*
other method
const sortedDatas = datas.sort().reverse()
*/

console.log("ソートした後の要素の並び")
dispArray(datas)

