function scrolltypecomment () { 
    document.querySelector('#type-comment').scrollIntoView({
        behavior: 'smooth'
    });
}

function successalert (param) { 
    var alert = document.getElementsByClassName('alert-success')[0];
    alert.innerHTML = param;
    alert.className = 'alert alert-success fade show';
    setTimeout(function(){
        document.getElementsByClassName('alert-success')[0].className = 'alert alert-success fade d-none';
    }, 2000);
}

function faildalert(param) { 
    var alert = document.getElementsByClassName('alert-danger')[0];
    alert.innerHTML = param;
    alert.className = 'alert alert-danger fade show';
    setTimeout(function(){
        document.getElementsByClassName('alert-danger')[0].className = 'alert alert-danger fade d-none';
    }, 2000);
}

function copyurl(){
    var url = document.getElementsByClassName('blog-url')[0];
    var inp = document.createElement('input');
    document.body.appendChild(inp)
    inp.value = url.textContent
    inp.select();
    document.execCommand('copy',false);
    inp.remove();
    successalert('آدرس با موفقیت کپی شد.');
}

function sendcommect (blog_id) {
    var comment = document.getElementsByClassName('comment-textarea')[0];
    var parent_id = document.getElementById('parentid').value;
    if (comment.value.length > 0) {
        $.ajax({
            url: '/blogs/blog-comment/',
            method: 'POST',
            data: {
                "text": comment.value,
                "blog_id": blog_id,
                "parent_id": parent_id,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            },
            success: function (data) {
                document.getElementById('type-comment').innerHTML = data;
                $('.comment-count')[0].innerHTML = parseInt($('.comment-count')[0].innerHTML) + 1;
            }
        });
        successalert('نظر شما با موفقیت ثبت شد.');
    }
    else {
        faildalert('نظر شما ثبت نشد.');
    }
}

function anwsercomment (comment_id) {
    var parentid = document.getElementById('parentid');
    parentid.value = comment_id;
    scrolltypecomment();
}