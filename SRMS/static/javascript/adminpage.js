
const down = document.getElementById('down');
const up = document.getElementById('up');

function toggleShowUp(){
    down.style.visibility = 'hidden';   
    up.style.visibility = 'visible';   
}
function toggleShowDown(){
    up.style.visibility = 'hidden';   
    down.style.visibility = 'visible';   
}



// Left Nav Button
const LefttoggleButton = document.getElementsByClassName('nav-logo')[0]
const LeftNavbarActive = document.getElementsByClassName('side-nav')[0]

LefttoggleButton.addEventListener('click', () => {
    LeftNavbarActive.classList.toggle('active')

})

// On big screen Profile pic
const profileToggle = document.getElementsByClassName('profile-pic')[0]
const ProfileNavActive = document.getElementsByClassName('right-content')[0]

profileToggle.addEventListener('click', () => {
    ProfileNavActive.classList.toggle('active')
    // alert('working')
        })


// Make admin profile form editable

function edit(){
    document.getElementById('username').disabled = false;
    document.getElementById('email').disabled = false;
    document.getElementById('first_name').disabled = false;
    document.getElementById('last_name').disabled = false;
}

// document.getElementById('id_password1').required = false;
// document.getElementById('id_password2').required = false;


// Active Left side Navigation bar
const activePage = window.location.pathname;
const navLinks = document.querySelectorAll('nav a').
forEach(link => {
    if (link.href.includes(`${activePage}`)){
        link.classList.add('active');
    }
    console.log(link.href)
})

// For active Navigation bar on left side
const active_navbar = document.getElementsByClassName('sidenav')[0]
const left_nav_bar = document.getElementsByClassName('side-nav')[0]

active_navbar.addEventListener('click', () => {
    left_nav_bar.classList.toggle('active')
})




// For student list SEARCH BAR FILTER
function myFunction() {
  var input, filter, table, tr, td, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  table = document.getElementById("myTable");
  tr = table.getElementsByTagName("tr");
  for (i = 0; i < tr.length; i++) {
    td = tr[i].getElementsByTagName("td")[1];
    if (td) {
      txtValue = td.textContent || td.innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        tr[i].style.display = "";
      } else {
        tr[i].style.display = "none";
      }
    }       
  }
}

// Add student Form validation!
const form = document.getElementById('formm');
const fullname = document.getElementById('fullname')
const address = document.getElementById('address')
const age = document.getElementById('age')
const phone = document.getElementById('phone')

form.addEventListener('submit' , (e) => {
    if(addresscheck()){
        if(fullnamecheck()){
            if(phonecheck()){
                if(agecheck()){
                    return true;
                }
                else{
                    e.preventDefault()
                }
            }
            else{
                e.preventDefault()
            }
        }
        else{
            e.preventDefault()
        }
    }
    else{
        e.preventDefault()
    }
    
})

//  For Fullname
function fullnamecheck(){

// Getting values from input
const fullnameValue = fullname.value;

    // fullname
    if(fullnameValue != ''){

        if (fullnameValue.length >= 3){

            if (isNaN(fullnameValue)){
                leftsuccess(fullname)
                var fname_point = 1;
                return true;
            }
            else{
                lefterror(fullname, '*Name cannot include number!*')
                return false;
            }
        }
        else{
            lefterror(fullname, '*Name must at least contain 3 letters!*')
            return false;
        }
    }
    else{
        lefterror(fullname, '*This field is required!*')
        return false;
    }

}

// For address
function addresscheck(){

    const addressValue = address.value;

    if(addressValue != ''){
        
        if( isNaN(addressValue)){
            leftsuccess(address)
            var address_point = 1;
            return true;
        }
        else{
                    lefterror(address, '*Address cannot include numbers!*')
                    return false;
        }
    }
    else{
        lefterror(address, '*This field is required!*')
        return false;
    }

}

// For Phone
function phonecheck(){

    const phoneValue = phone.value;
    // Phone
    if(!isNaN(phoneValue)){
        
        if(phoneValue != ''){
            
            if(phoneValue.charAt(0) == 9 && phoneValue.charAt(1) == 8){
                    
                
                if(phoneValue.length == 10){
                    leftsuccess(phone)
                    var phone_point = 1;
                    return true;
                }
                else{
                    righterror(phone, '*Phone must be exactly 10 digit!*')    
                    return false;   
                }

            }
            else{
                righterror(phone, '*Phone number starts with (98)!*')
                return false;
            }
        }
        else{
            righterror(phone, '*This field is required!*') 
            return false;
        }
    }
    else{
        righterror(phone , '*Phone cannot include character!*')
        return false;
    }
}

// For Age
function agecheck(){
    const ageValue = age.value;

    if (ageValue != ''){

        for (let i = 0; i < ageValue.length; i++) {
            if(isNaN(ageValue.charAt(i))){
                lefterror(age, '*Age cannot include characters!*')
                return false;
            }
            else{
                leftsuccess(age)
                return true;
            }
        }
    }
    else{
        lefterror(age, '*This field is required!*')
        return false;
    }


}



function lefterror(input, message){
    const formcontrol = input.parentElement;
    const small = formcontrol.querySelector('small');

    small.innerText = message;

    formcontrol.className = 'left-form error'

}
function righterror(input, message){
    const formcontrol = input.parentElement;
    const small = formcontrol.querySelector('small');

    small.innerText = message;

    formcontrol.className = 'right-form error'

}
// function leftsuccess(input){
//     alert('leftcakked')
//     const formcontrol = input.parentElement;
//     const small = formcontrol.querySelector('small')

//     small.innerText = 'success'

//     formcontrol.className = 'left-form error'

// }
function leftsuccess(input){
    const formcontrol = input.parentElement;

    formcontrol.className = 'left-form success'
}
function rightsuccess(input){
    const formcontrol = input.parentElement;

    formcontrol.className = 'right-form success'
}



setTimeout(function () {
            $('#invalid').fadeOut('fast');
        }, 3000);