document.addEventListener("mousemove", function(event) {
    let mouseX = event.clientX;
    let mouseY = event.clientY;
    let vw = window.innerWidth;
    let tolerating = 50;
    
    let filter = document.querySelector("#filter");
    let moveDownAndGoBrr = document.querySelector("#filter div");
    let waving = document.querySelector("#filter path");
    if (mouseX > vw / 2 - tolerating && mouseX < vw / 2 + tolerating && mouseY < tolerating) {
        filter.style.display = "block";
        moveDownAndGoBrr.style.animationPlayState = "running";
        waving.style.animationPlayState = "running";
    }
});

window.onload = function() {
    setTimeout(function() {
        let loader = document.getElementById("loader");
        loader.style.opacity = 0;
        loader.addEventListener("transitionend", function() {
            loader.style.display = "none";
        });
    }, 100);
}