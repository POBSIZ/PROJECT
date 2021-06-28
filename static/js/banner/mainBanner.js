const textSlide = document.querySelector('.mainBanner_text-inner');
const imgSlide = document.querySelector('.mainBanner_img-inner');


var MstartX, MmoveX, MendX,
    MstartY, MmoveY, MendY;
$(".mainBanner_img-inner").on('mousedown',function(event){
    MstartX = event.pageX;
    MstartY = event.pageY;
    // console.log('X: ' + MstartX + ' Y: ' + MstartY)
});
$(".mainBanner_img-inner").on('mousemove',function(event){
    MmoveX = event.pageX;
    MmoveY = event.pageY;
    // console.log('X: ' + MmoveX + ' Y: ' + MmoveY)
    
    // imgSlide.setAttribute('style', `left: -${imgSlide.clientWidth - MmoveX}px`)

});
$(".mainBanner_img-inner").on('mouseup',function(event){
    MendX=event.pageX;
    MendY=event.pageY;
    // console.log('X: ' + MendX + ' Y: ' + MendY)
});

var startX, moveX, endX,
    startY, moveY, endY;
$(".mainBanner_img-inner").on('touchstart',function(event){
  startX = event.originalEvent.changedTouches[0].screenX;
  startY = event.originalEvent.changedTouches[0].screenY;
//   console.log('X: ' + startX + ' Y: ' + startY)
});
$(".mainBanner_img-inner").on('touchmove',function(event){
  moveX = event.originalEvent.changedTouches[0].screenX;
  moveY = event.originalEvent.changedTouches[0].screenY;
//   console.log('X: ' + moveX + ' Y: ' + moveY)
});
$(".mainBanner_img-inner").on('touchend',function(event){
   endX=event.originalEvent.changedTouches[0].screenX;
   endY=event.originalEvent.changedTouches[0].screenY;
//    console.log('X: ' + endX + ' Y: ' + endY)
});

const setNum = 2;
var currNum = 0;
const changeSlide = ()=>{
    if(currNum == setNum){
        currNum = 0;            
        textSlide.setAttribute('style', `left: -${currNum*100}%`);
        imgSlide.setAttribute('style', `left: -${currNum*100}%`);
    }else{
        textSlide.setAttribute('style', `left: -${currNum*100}%`);
        imgSlide.setAttribute('style', `left: -${currNum*100}%`);
        currNum += 1;
    }
}

setInterval(changeSlide, 1000);
// setTimeout(changeSlide, 20);