function showpass(obj){
    var password = document.getElementById(obj).type;

    if (password==='text'){
        document.getElementById(obj).type = 'password';
        document.getElementById(obj+'-icon').className = 'fa-solid fa-eye-slash';
    }
    if (password==='password'){
        document.getElementById(obj).type = 'text';
        document.getElementById(obj+'-icon').className = 'fa-solid fa-eye';
    }
}