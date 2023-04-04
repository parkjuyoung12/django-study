// 1. 글쓰기와 수정에서 쓸 수 있는 함수
//// 제목이 비어있거나 또는 5글자 이하라면 경고창 표시하고
//// 진행 멈춤
//// 글 내용이 비어있거나 10글자 이하라면 경고창 표시하고
//// 진행 멈춤
//// 제목이나 글 내용에 바보, 멍청이, 한조 들어있으면 경고창 표시하고
//// 진행 멈춤

function formValidate() {
    // alert('진입')
    var title = $("#title").val();
    var content = $("#content").val();

    if (title ==="" || title.length <= 5 ) {
       alert("제목은 6글자 이상 입니다.");
       return false;
    } 
    if (content ==="" || content.length <= 10 ) {
        alert("내용은 11글자 이상 입니다.");
        return false;
     } 

    // 금지어 체크
    var bad = ['바보', '멍청이', '한조'];
    
    for(var i=0; i <bad.length; i++) {
       if(title.includes(bad[i]) || content.includes(bad[i])) {
          alert(bad[i] + "(은)는 사용할 수 없는 단어입니다");
          return false;
       }
       
    }
     return true;
}

function validateReply() {
    console.log('접근 ')
    let aa = $("#replyTextWrite").val()
    alert(aa)
    // 2. 댓글에서 쓸 수 있는 함수
    //// 댓글 창 비어있으면 경고창 표시
    if(aa == "") {
        alert("댓글창이 비어있습니다.")
        return false;
    }
    return true;
}


