const intro = document.querySelector(".wrapper");
const controller = new ScrollMagic.Controller();

// set desired animation time long enough so that it doesn't skip frames when scrolling fast.
const animationTime = 5000;
// initialise scrollmagic scene
let scene = new ScrollMagic.Scene({
    duration: animationTime,
    triggerElement: intro,
    triggerHook: 0,
})
//   .setPin(intro)
  .addTo(controller)
//   .addIndicators()
;

const elem = document.getElementById("lottie");
const animateData = {
    container: elem,
    renderer: "svg",
    loop: false,
    autoplay: true,
    rendererSettings: { progressiveLoad: false },
    path: jsonPath, // path to json file
};


// const textTitle = document.querySelector('.title');
// const textAnim = TweenMax.fromTo(textTitle, 3, { opacity: 0, top: '60%' }, { opacity: 1, top: '50%' });
// let scene2 = new ScrollMagic.Scene({
//   duration: 2500,
//   triggerElement: document.querySelector('.wrapper_2'),
//   triggerHook: 0
// })
//   .setTween(textAnim)
//   .setPin(document.querySelector('.wrapper_2'))
//   .addTo(controller)
//   .addIndicators();


// initalise bodymovin
let anim;
anim = lottie.loadAnimation(animateData);

let delay = 0;
let heightPerFrame = 0;

var textVar = document.querySelector('.title');
scene.on("update", (e) => {
    // heightPerFrame = anim.totalFrames / animationTime; // if total animation duration === total frames, then 1px height scroll = 1 frame moved
    // delay = Math.round(e.scrollPos * heightPerFrame);
    // console.log(e.scrollPos, delay, e.scrollPos * heightPerFrame);
    // if(delay > 73){
    //     anim.goToAndStop(73, true);
    // }else{
    //     anim.goToAndStop(delay, true);
    // }
    console.log(e.scrollPos)
    if(e.scrollPos > 490){
        textVar.setAttribute('style', 'opacity: 100%; top: 30%;')
    }
});

