const SummaryCount = () => {
    const array = [54, 20, 88, 30, 71, 29, 44, 9, 100, 31]
    let sum = 0;

    for (const elem of array) {
        sum += elem
    }
    console.log(`合計=${sum}`)
}

SummaryCount()