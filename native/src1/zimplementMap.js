

function map(arr, fn) {
  const newArr = []

  arr.forEach(function(val) {
    newArr.push(fn(val))
  })

  return newArr
}

function multTwo(num){return num *2}

const arr =[3,6,9,12]

console.log(map(arr,multTwo))

//______________imitating map  - mymap

//recieves array and func
function mymap (arr, fn){
//declare empty array newArr
const newArr=[]
//forEach value in array  implement anon func that pushes result in newArr
arr.forEach(function(val) {
    newArr.push(fn(val))
} )
//return newArr
return newArr

}


function myMap(arr, fn){
    newArr=[]
    arr.forEach(function(val){
        newArr.push(fn(val))
    })
    return newArr
}
console.log(myMap(arr,multTwo))