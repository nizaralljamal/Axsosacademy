function addLike() {
    let x = document.querySelector("#de")
    let count = parseInt(x.getAttribute('data-likes')) || x.innerText;
    
    
    count++;
    
    
    x.setAttribute('data-likes', count);
    
    
    // alert(  count + " "+ "Ninja was liked" );
    
    x.innerText = count ;

function addLike() {
    let x = document.querySelector("#de")
    let count = parseInt(x.getAttribute('data-likes')) || 0;
    
    
//     count++;
    
    
//     x.setAttribute('data-likes', count);
    
    
//     // alert(  count + " "+ "Ninja was liked" );
    
//     x.innerText = count + " fathi";
// }

