function addLike(button) {
  let noun = document.querySelector(".noun")
    noun.innerText="Nizar" 
    let count = parseInt(button.getAttribute('data-likes')) || 0;
    
    
    count++;
    
    
    button.setAttribute('data-likes', count);
    
    
    alert(  count + " "+ "Ninja was liked" );
    
    button.innerText = count + " likes";
}