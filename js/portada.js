var n = 0;
function fondo(){
    var portada = document.getElementById("imagenPortada");
    if (n == 0) {
        portada.setAttribute("src","/img/img0.jpeg");
    }
    else if (n == 1) {
        portada.setAttribute("src","/img/img1.jpeg");
    } 
    else if (n == 2) {
        portada.setAttribute("src","/img/img2.jpeg");
    }   
    else if (n == 3) {
        portada.setAttribute("src","/img/img3.jpeg");
    }     
    if (n == 3) {
        n=0;
    }
    n+=1;
}
$(document).ready(function(){
    setInterval(fondo,4000)
})