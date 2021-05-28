function idCheck(){
    if(!$('#username').val()){
        alert("ID를 입력해 주세요.");
        return;
    }
    
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/account/user_register_idcheck/",
        data: {
            'username' : $('#username').val(),
            'csrfmiddlewaretoken' : $("input[name=csrfmiddlewaretoken]").val()
        },
        success: function(response){
            $('#idcheck-result').html(response);
        },
    });
}

function changeEmailDomain() {
    $('#email_domain').val($('#email_selection').val());
}

function cancelMenberRegister() {
    var result = confirm("회원가입을 취소하시겠습니까?");
    
    if(result){
        $(location).attr('href', 'account:login');
    }
}

function UserRegister() {
    if(!$('#username').val()){
        alert("아이디를 입력해 주시기 바랍니다.");
        return;
    }
    if(!$('#IDCheckResult').val()){
        alert("ID 중복체크를 먼저 진행해 주시기 바랍니다.");
        return;
    }
    if(!$('#password').val()){
        alert("비밀번호를 입력해 주시기 바랍니다.");
        return;
    }
    if($('#password').val() != $('#passwordcheck').val()){
        alert("비밀번호가 일치하지 않습니다.");
        return;
    }
    if(!$('#realname').val()){
        alert("이름을 입력해 주시기 바랍니다.");
        return;
    }
    if(!$('#phone1').val() || !$('#phone2').val() || !$('#phone3').val()){
        alert("전화번호를 올바르게 입력해 주시기 바랍니다.");
        return;
    }
    if(!$('#email_id').val() || !$('#email_domain').val()){
        alert("이메일을 올바르게 입력해주시기 바랍니다.");
        return;
    }
    if(!$('#birth').val()){
        alert("생일을 입력해주시기 바랍니다.");
        return;
    }
    
    $('#phone').val($('#phone1').val() + "-" + $('#phone2').val() + "-" + $('#phone3').val());
    $('#email').val($('#email_id').val() + "@" + $('#email_domain').val());
    
    $('#register_form').submit();
}

