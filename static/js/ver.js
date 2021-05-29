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
    // console.log(e.scrollPos)
    if(e.scrollPos > 0){
        navBar.classList.add('sticky');
    }else if(e.scrollPos == 0){
        navBar.classList.remove('sticky');
    }

    // INFO
    if(e.scrollPos > 410){
        document.querySelector('.info_tab').setAttribute('style', 'top: 0; opacity: 100%;');
    }

    // DO-LIST
    doList = document.querySelectorAll('.doList-itm')
    doListM = 400
    if(e.scrollPos > doList[0].offsetTop - doList[0].offsetHeight - doListM){
        doList[0].classList.add('scrollActive');
    }
    if(e.scrollPos > doList[1].offsetTop - doList[1].offsetHeight - doListM){
        doList[1].classList.add('scrollActive');
    }
    if(e.scrollPos > doList[2].offsetTop - doList[2].offsetHeight - doListM){
        doList[2].classList.add('scrollActive');
    }
    if(e.scrollPos > doList[3].offsetTop - doList[3].offsetHeight - doListM){
        doList[3].classList.add('scrollActive');
    }
});

window.onload = ()=>{
    setTimeout(() => {
        navBar.setAttribute('style', 'top: 0;');
    }, 2000);
};
