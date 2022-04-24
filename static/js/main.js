var a=1
 let qnt=document.getElementById('qnt').value=a;

 
 
let inc=document.getElementById('inc');
inc.addEventListener('click', function inc(){
 a=a+1
 document.getElementById('qnt').value=a;
})
let dec=document.getElementById('dec');
dec.addEventListener('click', function inc(){
    if(a<1 ){
       console.log('ok')
    }
   else{
 
   a= --a
   document.getElementById('qnt').value=a;
   }
})

// icons
let fave=document.getElementById('fave');
fave.addEventListener('click', function(){
   fave.classList.remove("bi-heart")
   fave.classList.add("bi-heart-fill")
   fave.classList.add("text-danger")
})
// add to card
