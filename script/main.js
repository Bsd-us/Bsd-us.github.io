let svgList = [
    'bem', 'bm', 'c2', 'c', 'gp', 'g', 'jb', 'lh', 'll', 'ltaddn', 'm', 'n', 'sg', 's', 'tco', 'tg', 'tpn', 'w', 'x' 
]

let background = document.querySelector("main");
for (let i = 0; i < 7000; i++) {
    let img = document.createElement("img");
    img.loading = "lazy";
    img.src = `svg/${svgList[Math.floor(Math.random() * svgList.length)]}.svg`;
    background.appendChild(img);
}

document.addEventListener("mousemove", function(event) {
    let mouseX = event.clientX;
    let mouseY = event.clientY;
    let vw = window.innerWidth;
    let tolerating = 50;
    
    if (mouseX > vw / 2 - tolerating && mouseX < vw / 2 + tolerating && mouseY < tolerating) {
        background.style.width = "70%";
    } else {
        background.style.width = "100%" ;
    }
});

window.onload = function() {
    let loader = document.getElementById("loader");
    loader.style.opacity = 0;
    loader.addEventListener("transitionend", function() {
        loader.style.zIndex = 0 ;
    });
}