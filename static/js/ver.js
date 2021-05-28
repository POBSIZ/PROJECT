const intro = document.querySelector(".main");
const controller = new ScrollMagic.Controller();

const animationTime = 5000;
let scene = new ScrollMagic.Scene({
    duration: animationTime,
    triggerElement: intro,
    triggerHook: 0,
}).addTo(controller);

const elem = document.getElementById("lottie");
const animateData = {
    container: elem,
    renderer: "svg",
    loop: false,
    autoplay: true,
    rendererSettings: { progressiveLoad: false },
    path: jsonPath, 
};

let anim = lottie.loadAnimation(animateData);

const navBar = document.querySelector('.navBar');
scene.on("update", (e) => {
    console.log(e.scrollPos)
    if(e.scrollPos > 0){
        navBar.classList.add('sticky');
    }else if(e.scrollPos == 0){
        navBar.classList.remove('sticky');
    }

    // INFO
    if(e.scrollPos > 410){
        document.querySelector('.info_tab').setAttribute('style', 'top: 0; opacity: 100%;')
    }

    // DO-LIST
    if(e.scrollPos > 850){
        document.querySelectorAll('.doList-itm')[0].setAttribute('style', 'left: 0%; opacity: 100%;')
    }
    if(e.scrollPos > 1250){
        document.querySelectorAll('.doList-itm')[1].setAttribute('style', 'left: 0%; opacity: 100%;')
    }
    if(e.scrollPos > 1650){
        document.querySelectorAll('.doList-itm')[2].setAttribute('style', 'left: 0%; opacity: 100%;')
    }
    if(e.scrollPos > 2050){
        document.querySelectorAll('.doList-itm')[3].setAttribute('style', 'left: 0%; opacity: 100%;')
    }
});

window.onload = ()=>{
    setTimeout(() => {
        navBar.setAttribute('style', 'top: 0;');
    }, 2000);
};
