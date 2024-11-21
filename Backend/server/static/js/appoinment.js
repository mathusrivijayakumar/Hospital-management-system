const form = document.querySelector('#form');
const date=document.querySelector('#date')
const time=document.querySelector('#time')
const desc=document.querySelector('#desc')

form.addEventListener('submit',(e)=>{
    
    if(!validateInputs()){
        e.preventDefault();
    }
})

function validateInputs(){
    const dateVal = date.value.trim()
    const timeVal = time.value.trim()
    let success = true

    datearray=dateVal.split("-")
    timearray=timeVal.split(":")

    if(dateVal==='')
    {
        success= false;
        setError(date,'Enter a valid Date')
    }
    else if(datearray[0].length!=2||datearray[1].length!=2||datearray[2].length!=4)
    {
        success= false;
        setError(date,'Please enter Date')
    }
    else
    {
        setSuccess(date)
    }

    if(timeVal==='')
    {
        success= false;
        setError(time,'Enter a valid Time')
    }
    else if(timearray[0].length!=2||timearray[1].length!=2)
    {
        success= false;
        setError(time,'Please enter Time')
    }
    else
    {
        setSuccess(time)
    }

    if(desc===''){
        success=false;
        setError(desc,"Desc required")
    }
    else{
        setSuccess(desc)
    }

    return success
}

function setError(element,message){
    const inputGroup = element.parentElement;
    const errorElement = inputGroup.querySelector('.error')

    errorElement.innerText = message;
    inputGroup.classList.add('error')
    inputGroup.classList.remove('success')
}

function setSuccess(element){
    const inputGroup = element.parentElement;
    const errorElement = inputGroup.querySelector('.error')

    errorElement.innerText = '';
    inputGroup.classList.add('success')
    inputGroup.classList.remove('error')
}