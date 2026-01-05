const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(() => {
    $("#message").fadeOut("slow");
}, 3000); 
//to set the time for the alert to disappear
// # is to search for 'message'
