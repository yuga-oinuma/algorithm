// p101

const InsertionSort = (datas: Array<number>) => {

    for (let i = 1; i < datas.length; i++) {
        for (let j = i; j > 0; j--) {
            if (datas[j - 1] <= datas[j]) {
                break
            }
            const temp = datas[j - 1]
            datas[j - 1] = datas[j]
            datas[j] = temp
        }
    }

    return datas
}

const dispArray = (datas: Array<number>) => {
    for (let value of datas) {
        console.log(`${value}`)
    }
}


const DATAS = [35, 80, 49, 54, 11, 78, 92, 21, 67, 45]

const sortedDatas = InsertionSort([...DATAS])
/*
other method
const sortedDatas = [...DATAS].sort()
*/

console.log("ソートする前の要素値の並び")
dispArray(DATAS)

console.log("ソートした後の要素の並び")
dispArray(sortedDatas)
