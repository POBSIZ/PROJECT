var eventList = '';
var timeList = '';
var csrf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
const getView = (viewData)=>{
    $.ajax({
        type: "POST",
        url: "view/",
        headers:{"X-CSRFToken": csrf_token},
        data: viewData,
        dataType: 'json',
        success: function (response) {
            var apiTest = "";
            // var temp1 = JSON.parse(response.time)
            console.log(response.time[0])
            for (var i = 0; i < response.time.length; i++) {
                apiTest += "<p> 이벤트 시간 : " + response.time[i].o_time + "<br>"
                apiTest += "예약자 : " + response.time[i].username + "<br>"
                apiTest += "만든 날짜 : " + response.time[i].create_time + "</p>"
            }
            $('#test').html(apiTest);
            $('.remain').html(response.remain);
            // $('#test').html(temp1);
            console.log('object :>> ', response);
        },
    });
}

// RESV NAV CHANGER
const nav = document.querySelector('.navBar');
const resvTab = document.querySelector('.resv-wrapper');
const exitBtn = document.querySelector('.resv-close');
exitBtn.addEventListener('click', ()=>{
    resvTab.classList.remove('open');
    nav.setAttribute('style', 'z-index: 10;');
});



// 이벤트 선택용 함수
const eventActive = ()=>{
    eventItem = document.querySelectorAll('.event-itm');
    resvDetail = document.querySelector('.resv-detail');
    eventItem.forEach(item=>{
        item.addEventListener('click', ()=>{
            selItem = document.querySelectorAll('.selItm');
            if(selItem.length > 0){
                eventItem.forEach(iitm=>{iitm.classList.remove('selItm')});
                $('.resv-list').html('');
            }
            item.classList.toggle('selItm');
            eventTitle = item.children[0].innerHTML;
            
            for(var el in eventList){
                if(eventList[el]['fields']['o_event_title'] == eventTitle){
                    $('.resv-remain.remain').html(eventList[el]['fields']['remain'])
                    resvListItm = `<p>${timeList[el]['fields']['f_person']}</p>` 
                    $('.resv-list').append(resvListItm);
                }
            }       

            resvDetail.classList.add('detOn');
                 
            // console.log('eventTitle :>> ', eventTitle);
            // console.log('eventList :>> ', eventList);
        });
    });
}



// CHANGE YMD
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
            a_year = year.innerHTML;
            a_month = month.innerHTML;
            a_day = i.children[0].innerHTML;
            a_day = a_day.replace(/(\r\n\t|\n|\r\t)/gm,"");
            a_day = a_day.trim();
            data = {
                'a_ymd': `${a_year}-${a_month}-${a_day}`,
                'a_year': a_year,
                'a_month': a_month,
                'a_day': a_day,
            }
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
                getView(data);
                eventActive();
                nav.setAttribute('style', 'z-index: 0;');
            }else{
                i.classList.add('selected');
                selDate.push([year.innerHTML, month.innerHTML, i.innerHTML]);
                resvTab.classList.add('open');
                changeYMD(i.children[0]);
                getView(data);
                eventActive();
                nav.setAttribute('style', 'z-index: 0;');
            }
        });
    });
};



// RESV POST
const postBtn = document.querySelector('.purchase');
postBtn.addEventListener('click', ()=>{
    console.log('object :>> ');
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    const day = document.querySelector('.resv-day');
    const time = document.querySelector('.time');
    a_year = year.innerHTML;
    a_month = month.innerHTML;
    a_day = day.innerHTML;
    a_day = a_day.replace(/(\r\n\t|\n|\r\t)/gm,"");
    a_day = a_day.trim();
    a_time = time.value;
    data = {
        'a_ymd': `${a_year}-${a_month}-${a_day}`,
        'a_year': a_year,
        'a_month': a_month,
        'a_day': a_day,
        'a_time': a_time,
    }
    $.ajax({
        type: "POST",
        url: "resv/",
        headers:{"X-CSRFToken": csrf_token},
        data: data,
        dataType: "json",
        success: function (response) {
            if(response.remain == false){
                alert('이미 예약이 되어있습니다.')
            }else if(response.remain == true){
                alert('예약이 불가합니다.')
            }else{
                $('.remain').html(response.remain);
            }
        },
        error: function (request, status, error) { },
    });
});

// RESV CANCEL
const cancelBtn = document.querySelector('.cancel');
cancelBtn.addEventListener('click', ()=>{
    const year = document.querySelector('.year');
    const month = document.querySelector('.month');
    const day = document.querySelector('.resv-day');
    const time = document.querySelector('.time');
    a_year = year.innerHTML;
    a_month = month.innerHTML;
    a_day = day.innerHTML;
    a_day = a_day.replace(/(\r\n\t|\n|\r\t)/gm,"");
    a_day = a_day.trim();
    a_time = time.value;
    data = {
        'a_ymd': `${a_year}-${a_month}-${a_day}`,
        'a_year': a_year,
        'a_month': a_month,
        'a_day': a_day,
        'a_time': a_time,
    }
    $.ajax({
        type: "POST",
        url: "cancel/",
        headers:{"X-CSRFToken": csrf_token},
        data: data,
        dataType: "json",
        success: function (response) {
            if(response.remain == false){
                alert('이미 예약이 취소 되어있습니다.')
            }else{
                $('.remain').html(response.remain);
            }
        },
        error: function (request, status, error) { },
    });
});


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