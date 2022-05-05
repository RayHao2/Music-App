console.log('HELLO')
const audioBox = document.getElementById('audio-box') //get the div audio-box
const audioBox2 = document.getElementById('audio-box-2')


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


function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
const sumbitbutton = document.getElementById('sumbitbutton')
const ids = document.getElementById('ids')
//function that sumbit a form of user chocing audiovar 
const createForm = () =>{

    ids.innerHTML = 
        `<select id="ids" name="ids"> 

        <option value ="first"> ${first+1} </option>
        <option value ="second"> ${second+1} </option>
        </select>`
    sumbitbutton.innerHTML =
        `
        <button button="sumbit" value="sumbit" id="sumbitbutton"> sumbit </button>
        `
    


}


//call so that web can loaded when enter
handleGetData()
createForm()
//event listenrs
sumbitbutton.addEventListener('click', ()=>{
    first = Math.floor(Math.random() * (max-min) + min)
    second = Math.floor(Math.random() * (max-min) + min)
    handleGetData()
    createForm()

})