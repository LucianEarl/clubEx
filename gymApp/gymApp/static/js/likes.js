
console.log('Hello World')

// gets all stars from video HTML
const one = document.getElementById('first')
const two = document.getElementById('second')
const three = document.getElementById('third')
const four = document.getElementById('fourth')
const five = document.getElementById('fifth')

const form = document.querySelector('.rate-form')
const confirmBox = document.getElementById('confirm-box')

const csrf = document.getElementsByName('csrfmiddlewaretoken')


// loop function for stars when you mouseover them
const handleStarSelect = (size) => {
    const children = form.children
    for (let i=0; i < children.length; i++) {
        if(i <= size){
            children[i].classList.add('checked')
        } else {
            children[i].classList.remove('checked')
        }
    }
}




console.log("This is", one)

// creates checked star for ratings
const handleSelect = (selection) => {
    switch(selection){
        case 'first': {
            handleStarSelect(1)
            return
        }
        case 'second': {
            handleStarSelect(2)
            return
        }
        case 'third': {
            handleStarSelect(3)
            return
        }
        case 'fourth': {
            handleStarSelect(4)
            return
        }
        case 'fifth': {
            handleStarSelect(5)
            return
        }

    }
}

// if statement to stop error for having no start selected, also allows video page to be refreshed
if(one) {
    const star = [one, two, three, four, five]

    star.forEach(item=> item.addEventListener('mouseover', (event)=> {
        handleSelect(event.target.id)
    }));
}

