// 유효성 검증 - 입력을 정확하게 하도록 제한하는 절차
function checkMember(){
    var form = document.regForm;
    var id = form.memberid.value;
    var pwd1 = form.passwd.value;
    var pwd2 = form.passwd_confirm.value;
    var name = form.name.value;
    var date = form.reg_date.value;

    var regEx = /^[0-9A-Za-z]{4,8}$/;
    if(id.length != 5){
        alert("아이디는 5자만 입력가능합니다.");
        form.id.select();
        return false;
    }else if(!regEx.test(pwd1)){
        alert("패스워드는 4자에서 8자까지 영문, 숫자포함 입력해주세요.");
        form.pwd1.select();
        return false;
    }else if(pwd1 != pwd2){
        alert("패스워드가 동일하지 않습니다.");
        form.pwd2.select()
        return false;
    }else if(name == ''){
        alert("이름은 필수 입력항목입니다.");
        form.name.focus()
        return false;
    }else if(date == ''){
        alert("가입일은 필수 입력항목입니다.");
        form.date.focus()
        return false;
    }else{
        form.submit();
    }
}