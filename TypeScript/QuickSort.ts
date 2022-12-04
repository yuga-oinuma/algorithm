
const QuickSort =(datas: Array<number>, head: number, tail:number)=>{

    if (head < tail) {

        let left = head + 1
        let right = tail

        while(true){
            while(left < tail && datas[head] > datas[left]){
                left++
            }
            while (datas[head] < datas[right]) {
                right--;
              }
        
              if (left >= right) {
                break;
              }
        
              const temp = datas[left];
              datas[left] = datas[right];
              datas[right] = temp;
        
              left++;
              right--;
        }
        const temp = datas[head];
        datas[head] = datas[right];
        datas[right] = temp;


        QuickSort(datas, head, right - 1)
        QuickSort(datas, right + 1, tail)
    }
    return datas
}

let datas: number[] = new Array
for (let i = 0; i < 10; i++) {
    datas.push(Math.floor(Math.random() * 100))
}

const result = QuickSort(datas.concat(), 0 , datas.length - 1)

console.log(`ソートする前の要素値の並び: ${datas}`)
console.log(`ソートする後の要素値の並び: ${result}`)