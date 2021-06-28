// const intro = document.querySelector(".main");
// const controller = new ScrollMagic.Controller();

// const animationTime = 5000;
// let scene = new ScrollMagic.Scene({
//     duration: animationTime,
//     triggerElement: intro,
//     triggerHook: 0,
// }).addTo(controller);

// const elem = document.getElementById("lottie");
// const animateData = {
//     container: elem,
//     renderer: "svg",
//     loop: false,
//     autoplay: true,
//     rendererSettings: {
//         progressiveLoad: false
//     },
//     path: jsonPath,
// };

// let anim = lottie.loadAnimation(animateData);


var sts = 3;
window.onload = () => {
    
    document.addEventListener('scroll', function(e) {
        console.log(window.scrollY)
        // INFO
        if (window.scrollY > 150) {
            document.querySelector('.info_tab').setAttribute('style', 'top: 0; opacity: 100%;');
        }
    });
    

    if ($(window).width()+17 > 1000){sts = 3;}else{sts = 1;}

    $('.doList').slick({
        infinite: true,
        slidesToShow: sts,
        slidesToScroll: 1,
        arrows: false,
        autoplay: true,
        autoplaySpeed: 2000,
    });
    
    if(sts == 3){
        $('.doList').on('afterChange', function (event, slick, direction) {
            const active = document.querySelectorAll('.slick-active');
            const centPick = document.querySelectorAll('.centOn');
            const cent0 = active[0];
            const cent1 = active[1];
            if (centPick.length == 2) {
                centPick[1].classList.remove('centOn');
            }
            cent0.classList.remove('centOn');
            cent1.classList.add('centOn');
        });
    }

    var cent1s = document.querySelectorAll('.slick-active')[1];
    cent1s.classList.add('centOn');

}


