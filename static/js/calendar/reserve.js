const nav = document.querySelector('.navBar');
const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', ()=>{
    resvTab.classList.remove('open');
    nav.setAttribute('style', 'z-index: 10;');
});


const o_year = document.querySelector('.year');
const o_month = document.querySelector('.month');
const year = document.querySelector('.resv-year');
const month = document.querySelector('.resv-month');
const day = document.querySelector('.resv-day');
const changeYMD = (d)=>{
    year.textContent = o_year.textContent;
    month.textContent = o_month.textContent;
    day.textContent = d.textContent;
}

// 날짜별로 이벤트 등록용 함수 및 변수
const selDate = []
const dateFunc = ()=>{
    const dates = document.querySelectorAll('.date');
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    dates.forEach((i)=>{
        // console.log('DATE LOAD')
        i.addEventListener('click', ()=>{
            if(i.classList.contains('other') || i.classList.contains('selected')){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                i.classList.remove('selected');
                selDate.length=0;
            }else if(selDate.length > 0){
                dates.forEach((ig)=>{ig.classList.remove('selected');});
                selDate.length=0;
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
                changeYMD(i.children[0]);
                nav.setAttribute('style', 'z-index: 0;');
            }else{
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
                changeYMD(i.children[0]);
                nav.setAttribute('style', 'z-index: 0;');
            }
        });
    });
};

// 초기화 함수 
const reset = ()=>{
    selDate.length=0;
    dateFunc();
}

// 로드시 Nav 버튼들 이벤트 등록 및 초기화
window.onload=()=>{
    const navBtn = document.querySelectorAll('.nav-btn');
    navBtn.forEach(inf=>{
        // console.log('NAV LOAD');
        if(inf.classList.contains('go-prev')){
            inf.addEventListener('click', ()=>{prevMonth(); reset();});
        }else if(inf.classList.contains('go-today')){
            inf.addEventListener('click', ()=>{goToday(); reset();});
        }else if(inf.classList.contains('go-next')){
            inf.addEventListener('click', ()=>{nextMonth(); reset();});
        }
    });
    reset();
}

