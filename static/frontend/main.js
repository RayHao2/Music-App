console.log('HELLO')
const aduiosBox = document.getElementById('audio-box') //get the div audio-box
const nextBtn = document.getElementById('next-btn')

let visible = 3
const handleGetData = () =>{
    $.ajax({
    type: 'GET',
    url: `/home/json/${visible}/`,
    success: function(response)
    {
        max_size = response.max
        //getting all the data and display in the console
        const data = response.data 
        data.map(post=>{
            console.log(post)
            aduiosBox.innerHTML +=
            `
            <div class="card p-3 mt-3 mb-3">
                <audio controls>
                <source src= ${post.location} type="audio/wav"> 
                </audio>


            </div>
            `
        
        })
        //check if the display size reach maxium
        if(max_size){
            console.log('done')
        }
    },
    error:function(error){
        console.log(error)
    }
    })

}

handleGetData()
//event listenrs
nextBtn.addEventListener('click', ()=>{
    visible += 3
    handleGetData()

})