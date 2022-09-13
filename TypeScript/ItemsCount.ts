//p61
const ENDDATA = -1

const ItemsCount = () => {
    const array: number[] = [54, 20, 88, 30, 71, ENDDATA]
    let count: number = 0
    let i = 0

    while (array[i] !== ENDDATA) {
        count++
        i++
    }

    console.log(`有効数データ数 = ${count}`)

}

ItemsCount()