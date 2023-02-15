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

function sendcommect () {
    var comment = document.getElementsByClassName('comment-textarea')[0];
    if (comment.value.length > 0) {
    successalert('نظر شما با موفقیت ثبت شد.');
    }
    else {
        faildalert('نظر شما ثبت نشد.');
    }
}