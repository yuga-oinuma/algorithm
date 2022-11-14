import * as readline from 'readline'

const readInterface = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

const SearchStr=(sentence: string, target: string)=>{
    let result = -1
    let i:number = 0
    let j:number = 0

    while (typeof(sentence[i]) != 'undefined' && typeof(target[j]) != 'undefined'){
        if (sentence[i] == target[j]){
            i ++
            j ++
        }
        else{
            i = i - j + 1
            j = 0
        }
    }

    result = i - j
    
    return result

}


console.log('探索される文字列を入力してください')
readInterface.question('>', (sentence: any) =>{
    console.log('探索する部分文字列を入力してください\n>')
    readInterface.question('',(target:any) =>{
        if (typeof(sentence) != 'undefined'){
            readInterface.close()
            const result = SearchStr(sentence, target)
            if (result == -1) {
                console.log("目的の値は見つかりませんでした")
            } else {
                console.log(`目的の値の添え字は${result}です。`)
            }

        }
    
    
    })
})
    
    





