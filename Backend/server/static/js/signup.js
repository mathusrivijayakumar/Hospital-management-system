const form = document.querySelector('#form');
const fname=document.querySelector('#firstName')
const lname=document.querySelector('#lastName')
const username = document.querySelector('#username');
const email = document.querySelector('#email');
const password = document.querySelector('#password');
const contact=document.querySelector('#contact');
const address=document.querySelector('#address');
const zip=document.querySelector('#zip');


form.addEventListener('submit',(e)=>{
    
    if(!validateInputs()){
        e.preventDefault();
    }
})

function validateInputs(){
    const fnameVal = fname.value.trim()
    const lnameVal = lname.value.trim()
    const usernameVal = username.value.trim()
    const contactVal = contact.value.trim()
    const emailVal = email.value.trim();
    const passwordVal = password.value.trim();
    const addressVal = address.value.trim()
    const zipVal=zip.value.trim()
    let success = true

    if(usernameVal===''){
        success=false;
        setError(username,'Username is required')
    }
    else{
        setSuccess(username)
    }

    if(emailVal===''){
        success = false;
        setError(email,'Email is required')
    }
    else if(!validateEmail(emailVal)){
        success = false;
        setError(email,'Please enter a valid email')
    }
    else{
        setSuccess(email)
    }

    if(fnameVal===''){
        success = false;
        setError(fname,'First Name is required')
    }
    else if(!validatename(fnameVal)){
        success = false;
        setError(fname,'Name should contain only alphabets')
    }
    else{
        setSuccess(fname)
    }

    if(lnameVal===''){
        success = false;
        setError(lname,'Last Name is required')
    }
    else if(!validatename(lnameVal)){
        success = false;
        setError(lname,'Name should contain only alphabets')
    }
    else{
        setSuccess(lname)
    }

    if(addressVal===''){
        success=false;
        setError(address,'Address is required')
    }
    else{
        setSuccess(address)
    }

    if(zipVal===''){
        success = false;
        setError(zip,'Zip code is required')
    }
    else if(zipVal.length!=6){
        success = false;
        setError(zip,'Enter a valid zip code')
    }
    else if(!validatecontact(zipVal))
    {
        success=false;
        setError(zip,'Zip code should contain only numbers')
    }
    else{
        setSuccess(zip)
    }

    if(contactVal===''){
        success = false;
        setError(contact,'Contact number is required')
    }
    else if(contactVal.length!=10){
        success = false;
        setError(contact,'Enter a valid contact number')
    }
    else if(!validatecontact(contactVal))
    {
        success=false;
        setError(contact,'Contact sholud contain only numbers')
    }
    else{
        setSuccess(contact)
    }

    if(passwordVal === ''){
        success= false;
        setError(password,'Password is required')
    }
    else if(passwordVal.length<8){
        success = false;
        setError(password,'Password must be atleast 8 characters long')
    }
    else{
        setSuccess(password)
    }

    return success;

}
//element - password, msg- pwd is reqd
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

const validatename=(name)=>{
    return String(name)
    .toLowerCase()
    .match(
        /^[a-zA-Z]+$/
    );
};

const validatecontact=(number) => {
    return String(number)
    .match(
        /^[0-9]+$/
    );
};

const validateEmail = (email) => {
    return String(email)
      .toLowerCase()
      .match(
        /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
  };
  