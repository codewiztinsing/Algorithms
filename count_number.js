// this draft code when we agree i provide you fully code
// that means the full code going be to you


let html_1 = `

<div>
    <h1>this first html</h1>
</div>
`



let html_2 = `

<div>
    <h1>this second html</h1>
</div>
`


let html_3 = `

<div>
    <h1>this thrid html</h1>
</div>
`

let list_varibale = [html_1,html_2,html_3]

let index = 0;
const myfunct = (mylist) => {
    while(index < mylist.length){
        console.log(mylist[index]);
        index ++;
        if(index == mylist.length){
            index = 0;
        }
        
    }
}


myfunct(list_varibale)