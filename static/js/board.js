function selectCategory(){
    $('#category').val($('#cateselect').val());
}

const post =()=>{
    console.log($('#category').val());
    if($('#category').val() == '-'){
        alert('카테고리를 선택해주세요!')
        return false;
    }else{
        return true;
    }
};  
