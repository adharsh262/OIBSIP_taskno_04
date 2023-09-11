let formEL=document.getElementById("formEl");
let mailInput=document.getElementById("emailInput");
let mailErrorMsg=document.getElementById("userNameErrorMsg");

let passwordInput=document.getElementById("passwordInput");
let passwordErrorMsg=document.getElementById("passwordErrorMsg");

function formvalidation() {
        mailInput.addEventListener("blur",function(event) {
            if(event.target.value==="") {
                mailErrorMsg.textContent="Required*";
            }else {
                mailErrorMsg.textContent="";
            }
        });
}

function clickLogin(event) {
    event.preventDefault();
    formvalidation();
}

formEL.addEventListener("submit",clickLogin);