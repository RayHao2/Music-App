console.log('HELLO')
const audioBox = document.getElementById('audio-box') //get the div audio-box
const audioBox2 = document.getElementById('audio-box-2')
const selectForm = document.getElementById('selectForm')

let max = 6
let min = 0
let first = Math.floor(Math.random() * (max-min) + min)
let second = Math.floor(Math.random() * (max-min) + min)
console.log(first)
console.log(second)

const handleGetData = () =>{
    $.ajax({
    type: 'GET',
    url: `/json/${first}/${second}`,
    success: function(response)
    {

        //getting all the data and display in the console
        const firstData = response.firstAudio 
        const secondData = response.secondAudio
        console.log(firstData)
        console.log(secondData)
        firstData.map(post=>{
            console.log(post)
            audioBox.innerHTML =
            //how to get the location right?
            `
            <div class="card p-3 mt-3 mb-3">
                <h> Audio ID: ${first+1}</h>
                <audio controls>
                <source src= ${post.location} type="audio/wav"> 
                </audio>
            </div>
            `
        })
        secondData.map(post=>{
            console.log(post)
            audioBox2.innerHTML =
            //how to get the location right?
            `
            <div class="card p-3 mt-3 mb-3">
                <h> Audio ID: ${second+1}</h>
                <audio controls>
                <source src= ${post.location} type="audio/wav"> 
                </audio>
            </div>
            `
        })
        


},//end of success
    error:function(error){
        console.log(error)


    }//end of error

})//ned of ajax


}

//function that sumbit a form of user chocing audio
const createForm = () =>{
    selectForm.innerHTML += 
        `<div id ="form">
        <form>
            <input type="submit" value="Submit">
        </form>
        </div>`


}

//call so that web can loaded when enter
handleGetData()
createForm()
//event listenrs
selectForm.addEventListener('click', ()=>{
    first = Math.floor(Math.random() * (max-min) + min)
    second = Math.floor(Math.random() * (max-min) + min)
    handleGetData()
})