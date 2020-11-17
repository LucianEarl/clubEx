
console.log('Hello World')

// gets all stars from video HTML
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

console.log("This is", one)

const star = [one, two, three, four, five]

star.forEach(item=> item.addEventListener('mouseover', (event)=> {
    console.log(event.target)
}));