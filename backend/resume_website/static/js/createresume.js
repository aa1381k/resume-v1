// function readURL(input,loc) {
//     console.log(input.files);
//    for (var i=0; i<input.files.length; i++) {
//         var reader = new FileReader();
//     // var image_tag_count = document.getElementsByClassName('images')[0];
//     // image_tag_count = image_tag_count.getElementsByTagName('img').length;
//
//         reader.onload = function (e) {
//
//             var new_image = document.createElement('img');
//             new_image.src = e.target.result;
//             new_image.className = 'd-block w-100';
//             var image = document.createElement('div');
//             image.className = 'carousel-item';
//             image.appendChild(new_image);
//             var image_section = document.getElementsByClassName("carousel-inner")[0];
//             image_section.appendChild(image);
//
//
//             document.getElementsByClassName('custom-file-remove')[0].style.display = 'block';
//
//         };
//
//
//         reader.readAsDataURL(input.files[i]);
//    }
//
//
// }

function changeicon(test, index) {
    var selected_value = test.options[test.selectedIndex].value;
    var icon = document.getElementsByClassName('user-social-media-item')[index].getElementsByClassName('item-inputs')[0].getElementsByTagName('i')[0];
    icon.className = 'fa-brands fa-' + selected_value;
    if (selected_value==''){
         icon.className = 'fa fa-globe';
    }
}

function addsocial() {
    var index = document.getElementsByClassName('user-social-media-item')
    console.log(index, 'this is index');
    index = index.length;
    var social = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'user-social-media','user-social-media-item','social')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'user-social-media','user-social-media-item','social')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'user-social-media')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs col-md-12"> <span><i class="fa fa-globe"></i></span> <div class="social-media-body col-md-12"> <select name="" id="" onchange="changeicon(this,${index})"> <option value="">نام شبکه اجتماعی</option> <option value="linkedin">لینکداین</option> <option value="twitter">توییتر</option> <option value="facebook">فیسبوک</option> <option value="instagram">اینستاگرام</option> <option value="telegram">تلگرام</option> <option value="github">گیت‌هاب</option> <option value="dribbble">دریبل</option> <option value="whatsapp">واتساپ</option> <option value="skype">اسکایپ</option> <option value="youtube">یوتیوب</option> <option value="stack-overflow">StackOverflow</option> </select> <div class="social-media-id">  <input type="text" name="" id="" placeholder="ID"> </div> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `social_${index}`;
    elem.setAttribute('name', `social_${index}`);
    elem.className = 'user-social-media-item col-md-10';
    elem.innerHTML = social;
    var element = document.getElementsByClassName('user-social-media')[0];
    element.appendChild(elem);
}

function addlang() {
    var index = document.getElementsByClassName('lang-item');
    index = index.length;
    var lang = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'lang-items','lang-item','lang')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'lang-items','lang-item','lang')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this)"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="lang col-md-6"> <span>نام زبان</span> <input type="text"> </div> <div class="lang-rate col-md-5"> <span>سطح</span> <select name="" id=""> <option value=""></option> <option value="1">⭐(در حال یادگیری)</option> <option value="2">⭐⭐(کم تجربه)</option> <option value="3">⭐⭐⭐(تسلط نسبی)</option> <option value="4">⭐⭐⭐⭐(تسلط کامل)</option> <option value="5">⭐⭐⭐⭐⭐(حرفه ای)</option> </select> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `lang_${index}`;
    elem.setAttribute('name', `lang_${index}`);
    elem.className = `col-md-12 lang-item border rounded-2 mb-3 col-md-10`;
    elem.innerHTML = lang;
    var element = document.getElementsByClassName('lang-items')[0];
    element.appendChild(elem);
}

function addskill() {
    var index = document.getElementsByClassName('skill-item');
    index = index.length;
    var skill = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'skill-items', 'skill-item', 'skill')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this,'skill-items', 'skill-item', 'skill')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'skill')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="skill-name text-center col-md-7"> <span>نام مهارت</span> <input type="text"> </div> <div class="skill-rate text-center col-md-5"> <span>سطح مهارت</span> <select name="" id=""> <option value=""></option> <option value="1">⭐(در حال یادگیری)</option> <option value="2">⭐⭐(کم تجربه)</option> <option value="3">⭐⭐⭐(تسلط نسبی)</option> <option value="4">⭐⭐⭐⭐(تسلط کامل) </option> <option value="5">⭐⭐⭐⭐⭐(حرفه ای) </option> </select> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `skill_${index}`;
    elem.setAttribute('name', `skill_${index}`);
    elem.className = `skill-item col-md-12 border rounded-3 p-3 d-flex justify-content-around flex-md-row-reverse`;
    elem.innerHTML = skill;
    var element = document.getElementsByClassName('skill-items')[0];
    element.appendChild(elem);
}

function addcertification() {
    var index = document.getElementsByClassName('certification-item');
    index = index.length;
    var certification = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'certification-items','certification-item','certificate')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'certification-items','certification-item','certificate')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'certificate')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs col-md-12 d-flex flex-column align-items-center justify-content-around mt-5 mb-5 "> <div class="col-md-10"> <span>عنوان گواهی نامه</span> <input type="text"> </div> <div class="col-md-10 item-data-inputs"> <div class="col-md-6 d-flex flex-column justify-content-between"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 certification-date"> <div class="col-md-5 skill-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 skill-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-5"> <span>عنوان موسسه</span> <input type="text"> </div> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `certificate_${index}`;
    elem.setAttribute('name', `certificate_${index}`);
    elem.className = `certification-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = certification;
    var element = document.getElementsByClassName('certification-items')[0];
    element.appendChild(elem);
}

function addeducation() {
    var index = document.getElementsByClassName('education-item');
    index = index.length;
    var education = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'education-items','education-item','education')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'education-items','education-item','education')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'education')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="col-md-3 flex-item"> <span>مقطع تحصیلی</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>رشته تحصیلی</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>نام دانشگاه/موسسه</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 education-date"> <div class="col-md-5 education-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 education-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-11 education-desc-textarea"> <span>توضیحات</span> <textarea name="" id="" cols="30" rows="10">`;
    var elem = document.createElement('div');
    elem.id = `education_${index}`;
    elem.setAttribute('name', `education_${index}`);
    elem.className = `education-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = education;
    var element = document.getElementsByClassName('education-items')[0];
    element.appendChild(elem);
}

function addjob() {
    var index = document.getElementsByClassName('job-item');
    index = index.length;
    var job = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'job-items','job-item','job')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'job-items','job-item','job')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'job')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="col-md-3 flex-item"> <span>نام شرکت / سازمان</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>سمت شغلی</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>شهر</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 job-date"> <div class="col-md-5 job-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 job-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-11 job-desc-textarea"> <span>توضیحات</span> <textarea name="" id="" cols="30" rows="10">`;
    var elem = document.createElement('div');
    elem.id = `job_${index}`;
    elem.setAttribute('name', `job_${index}`);
    elem.className = `job-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = job;
    var element = document.getElementsByClassName('job-items')[0];
    element.appendChild(elem);
}

function addproject() {
    var index = document.getElementsByClassName('project-item');
    index = index.length;
    var project = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'project-items','project-item','project')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'project-items','project-item','project')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'project')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="col-md-3 flex-item"> <span>کارفرما / درخواست دهنده</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>عنوان</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>لینک</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 project-date"> <div class="col-md-5 project-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 project-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-11 project-desc-textarea"> <span>توضیحات</span> <textarea name="" id="" cols="30" rows="10">`;
    var elem = document.createElement('div');
    elem.id = `project_${index}`;
    elem.setAttribute('name', `project_${index}`);
    elem.className = `project-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = project;
    var element = document.getElementsByClassName('project-items')[0];
    element.appendChild(elem);
}

function addinternship() {
    var index = document.getElementsByClassName('internship-item');
    index = index.length;
    var internship = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'internship-items','internship-item','internship')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'internship-items','internship-item','internship')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'internship')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="col-md-3 flex-item"> <span>نام شرکت / مرکز اشتغال</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>عنوان شغلی</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>شهر</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 other-date"> <div class="col-md-5 other-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 other-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-11"> <span>توضیحات</span> <textarea name="" id="" cols="30" rows="10">`;
    var elem = document.createElement('div');
    elem.id = `internship_${index}`;
    elem.setAttribute('name', `internship_${index}`);
    elem.className = `internship-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = internship;
    var element = document.getElementsByClassName('internship-items')[0];
    element.appendChild(elem);
}

function addintroduced() {
    var index = document.getElementsByClassName('introduced-item');
    index = index.length;
    var introduced = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'introduced-items','introduced-item','introduced')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'introduced-items','introduced-item','introduced')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'introduced')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs mb-5"> <div class="col-md-3 flex-item"> <span>نام مرکز</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>نام معرف</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>ایمیل</span> <input type="text"> </div> <div class="col-md-3 flex-item"> <span>شماره تلفن</span> <input type="text"> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `introduced_${index}`;
    elem.setAttribute('name', `introduced_${index}`);
    elem.className = `introduced-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = introduced;
    var element = document.getElementsByClassName('introduced-items')[0];
    element.appendChild(elem);
}

function addentertainment(){
    var index = document.getElementsByClassName('entertainment-item');
    index = index.length;
    var entertainment = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'entertainment-items','entertainment-item','entertainment')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'entertainment-items','entertainment-item','entertainment')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'entertainment')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="col-md-11 item-inputs"> <div class="col-md-12"> <span>نام علاقه مندی</span> <input type="text"> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `entertainment_${index}`;
    elem.setAttribute('name', `entertainment_${index}`);
    elem.className = `entertainment-item col-md-11 m-auto border rounded-2 mb-3`;
    elem.innerHTML = entertainment;
    var element = document.getElementsByClassName('entertainment-items')[0];
    element.appendChild(elem);
}

function removeitem(id, itemname) {
    var index = document.getElementsByClassName(`${itemname}-item`);
    id = id.parentElement.parentElement.parentElement.id;
    index = index.length;
    var elem = document.getElementById(id);
    elem.remove();

    if (index <= 1){
        if (itemname == 'user-social-media'){
            addsocial();
        }

        if (itemname == 'lang'){
            addlang();
        }

        if (itemname == 'skill'){
            addskill();
        }

        if (itemname == 'certificate'){
            addcertification();
        }

        if (itemname == 'education'){
            addeducation();
        }

        if (itemname == 'job'){
            addjob();
        }

        if (itemname == 'project'){
            addproject();
        }

        if (itemname == 'internship'){
            addinternship();
        }

        if (itemname == 'introduced'){
            addintroduced();
        }

        if (itemname == 'entertainment'){
            addentertainment();
        }
    }

    var item_id = id .match(/(\d+)/)[0];

    $.ajax({
    method:'POST',
    url:'/create-resume/savedata/resume_remove_item/',
    data:{
        'item_name': itemname,
        'id': item_id,
        'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
    }
});

}

function movedownelement(id, parr, list, sec) {
    var arr = document.getElementsByClassName(list);
    var parrent = document.getElementsByClassName(parr)[0];
    id = id.parentElement.parentElement.parentElement.id;
    var arrlen = arr.length;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].id == id) {
            var old_index = i;
        }
    }
    var new_index = old_index + 1;
    var array2 = new Set(arr);
    var array3 = Array.from(array2);
    var element = array3[old_index];
    array3.splice(old_index, 1);
    array3.splice(new_index, 0, element);

    for (var i = 0; i < arrlen; i++) {
        array3[i].id = `${sec}_${i}`;
        array3[i].setAttribute('name', `${sec}_${i}`);
    }

    for (var i = 0; i < array3.length; i++) {
        parrent.appendChild(array3[i])
    }

}

function moveupelement(id, parr, list, sec) {
    var arr = document.getElementsByClassName(list);
    var parrent = document.getElementsByClassName(parr)[0];
    id = id.parentElement.parentElement.parentElement.id;
    var arrlen = arr.length;
    for (var i = 0; i < arr.length; i++) {
        if (arr[i].id == id) {
            var old_index = i;
        }
    }
    if (old_index > 0) {
        var new_elem = arr[old_index];
        var new_index = old_index - 1;
        var new_arr_list = [];
        for (var i = 0; i < arr.length; i++) {
            if (i == new_index) {
                new_arr_list.push(new_elem);
                arr[old_index].remove();
            }
            new_arr_list.push(arr[i]);
        }
        for (var i = 0; i < arrlen; i++) {
            new_arr_list[i].id = `${sec}_${i}`;
            new_arr_list[i].setAttribute('name', `${sec}_${i}`);
        }

        for (var i in new_arr_list) {
            parrent.appendChild(new_arr_list[i])
        }
    }

}


var tb1 = 'personal-info-page';
var id1 = 'personal-info';
var id2 = 'PERSONAL-INFO';
function pages(id) {
    if (tb1 != (id + '-' + 'page')) {
        document.getElementsByClassName(tb1)[0].className = tb1 + ' invisible';

        lower_id = id.toLowerCase();
        upper_id  = id.toUpperCase();

        document.getElementById(id2).className = 'btn tab-item';
        document.getElementById(id1).className = 'tab-btn';
        
        var newtab = document.getElementsByClassName(lower_id + '-' + 'page')[0];
        newtab.className = (lower_id + '-' + 'page');
        
        document.getElementById(lower_id).className = 'tab-btn active-tab';
        document.getElementById(upper_id).className = 'btn tab-item active-tab';

        if (lower_id == "other")
        {
            $('.nex-btn')[0].style.display = 'none';
            $('.down-btn')[0].style.bottom = '120px';
            $('.pre-btn')[0].style.display = 'block';
        }

        else if (lower_id == "personal-info"){
            $('.pre-btn')[0].style.display = 'none';
            $('.down-btn')[0].style.bottom = '160px';
            $('.nex-btn')[0].style.display = 'block';
        }

        else{
            $('.pre-btn')[0].style.display = 'block';
            $('.down-btn')[0].style.bottom = '160px';
            $('.nex-btn')[0].style.display = 'block';
        }



        $("#myModal").modal("hide");

        tb1 = lower_id + '-' + 'page';
        id1 = lower_id;
        id2 = upper_id;
        savedata(tb1);

    }
}

var recentpage = 'personal-info-page';
function savedata(obj){
    if (recentpage == 'personal-info-page'){
        personal_info_page_ajax();
    }
    if (recentpage == 'skills-page'){
        skills_page_ajax();
    }
    if (recentpage == 'education-page'){
        education_page_ajax();
    }
    if (recentpage == 'job-page'){
        job_page_ajax();
    }
    if (recentpage == 'project-page'){
        project_page_ajax();
    }
    if (recentpage == 'other-page'){
        other_page_ajax();

    }
    recentpage = obj;
}

function personal_info_page_ajax(){
    var first_name = document.getElementsByName('firstname')[0].value;
    var last_name = document.getElementsByName('lastname')[0].value;
    var job_title = document.getElementsByName('jobtitle')[0].value;
    var country = document.getElementsByName('country')[0].value;
    var state = document.getElementsByName('state')[0].value;
    var city = document.getElementsByName('city')[0].value;
    var military = document.getElementsByName('military')[0].value;
    var relationship = document.getElementsByName('relationship')[0].value;
    var sex = document.getElementsByName('sex')[0].value;                       //base info
    var day = document.getElementsByName('day')[0].value;
    var month = document.getElementsByName('month')[0].value;
    var year = document.getElementsByName('year')[0].value;
    // var avatar = document.getElementsByClassName('upload-avatar')[0];
    var phone = document.getElementsByName('phone')[0].value;
    var email = document.getElementsByName('email')[0].value;
    var website = document.getElementsByName('website')[0].value;
    var summary = document.getElementsByName('summary')[0].value;
    var resume_id = document.getElementById('resume_id').value;

    var social_media_count = document.getElementsByClassName('user-social-media-item').length;
    


    for (var i=0; i<social_media_count; i++){
        var social_media_item = document.getElementById('social_'+i);
        var social_media_id = social_media_item.getElementsByTagName('input')[0].value;
        var social_media_name = social_media_item.getElementsByTagName('select')[0].value;
        var social_media_number = i;


        if(social_media_id != '' || social_media_id != null){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_social/',
            data:{
                'social_media_name': social_media_name,
                'social_media_number': social_media_number,
                'social_media_id': social_media_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }
    }

    $.ajax({
        method:'POST',
        url:'/create-resume/savedata/user_base_info/',
        data:{
            first_name,
            last_name,
            job_title,
            country,
            state,
            city,
            military,
            relationship,
            sex,
            day,
            month,
            year,
            resume_id,
            phone,
            email,
            website,
            summary,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        }
    }).then(res=> {
        if (res != 'datasaved') {
            alert('لطفا فیلد ها را پر کنید');
        }
    });
}

function skills_page_ajax(){
    var lang_items = document.getElementsByClassName('lang-item').length;
    var skills_items = document.getElementsByClassName('skill-item').length;
    var certificate_items = document.getElementsByClassName('certification-item').length;

    for(var i=0; i<lang_items; i++){

        var lang_item = document.getElementById('lang_'+i);

        var lang_name = lang_item.getElementsByTagName('input')[0].value;
        var lang_grade = lang_item.getElementsByTagName('select')[0].value;
        var lang_id = i;


        if(lang_name != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_lang/',
            data:{
                'lang_name': lang_name,
                'lang_grade': lang_grade,
                'lang_id': lang_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }
    }

    for(var i=0; i<skills_items; i++){

        var skill_item = document.getElementById('skill_'+i);
        var skill_name = skill_item.getElementsByTagName('input')[0].value;
        var skill_grade = skill_item.getElementsByTagName('select')[0].value;
        var skill_id = i;

        if(skill_name != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_skill/',
            data:{
                'skill_name': skill_name,
                'skill_grade': skill_grade,
                'skill_id': skill_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }

    for(var i=0; i<certificate_items; i++){

        var certificate_item = document.getElementById('certificate_'+i);
        var certificate_title = certificate_item.getElementsByTagName('input')[0].value;
        var organization_title = certificate_item.getElementsByTagName('input')[3].value;
        var start_date = certificate_item.getElementsByTagName('input')[1].value;
        var end_date = certificate_item.getElementsByTagName('input')[2].value;
        var certificate_id = i;


        if(certificate_title != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_certificate/',
            data:{
                'certificate_title': certificate_title,
                'organization_title': organization_title,
                'start_date': start_date,
                'end_date': end_date,
                'certificate_id': certificate_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }

}

function education_page_ajax(){
    var education_items = document.getElementsByClassName('education-item').length;

    for(var i=0; i<education_items; i++){
        var education_item = document.getElementById('education_'+i);

        var education_title = education_item.getElementsByTagName('input')[1].value;
        var education_grade = education_item.getElementsByTagName('input')[0].value;
        var university_name = education_item.getElementsByTagName('input')[2].value;
        var start_date = education_item.getElementsByTagName('input')[3].value;
        var end_date = education_item.getElementsByTagName('input')[4].value;
        var text = education_item.getElementsByTagName('textarea')[0].value;
        var education_id = i;


        if(education_title != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_education/',
            data:{
                'education_title': education_title,
                'education_grade': education_grade,
                'university_name': university_name,
                'start_date': start_date,
                'end_date': end_date,
                'text': text,
                'education_id': education_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }
    }
}

function job_page_ajax(){
    var job_items = document.getElementsByClassName('job-item').length;
    for(var i=0; i<job_items; i++){
        var job_item = document.getElementById('job_'+i);
        var job_title = job_item.getElementsByTagName('input')[1].value;
        var company_name = job_item.getElementsByTagName('input')[0].value;
        var city = job_item.getElementsByTagName('input')[2].value;
        var start_date = job_item.getElementsByTagName('input')[3].value;
        var end_date = job_item.getElementsByTagName('input')[4].value;
        var text = job_item.getElementsByTagName('textarea')[0].value;
        var job_id = i;

        if(job_title != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_job/',
            data:{
                'job_title': job_title,
                'company_name': company_name,
                'city': city,
                'start_date': start_date,
                'end_date': end_date,
                'text': text,
                'job_id': job_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }
}

function project_page_ajax(){
    var project_items = document.getElementsByClassName('project-item').length;

    for(var i=0; i<project_items; i++){
        var project_item = document.getElementById('project_'+i);

        var project_title = project_item.getElementsByTagName('input')[1].value;
        var employer = project_item.getElementsByTagName('input')[0].value;
        var link = project_item.getElementsByTagName('input')[2].value;
        var start_date = project_item.getElementsByTagName('input')[3].value;
        var end_date = project_item.getElementsByTagName('input')[4].value;
        var text = project_item.getElementsByTagName('textarea')[0].value;
        var project_id = i;

        if(project_title != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_project/',
            data:{
                'project_title': project_title,
                'employer': employer,
                'link': link,
                'start_date': start_date,
                'end_date': end_date,
                'text': text,
                'project_id': project_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }
}

function other_page_ajax(){
    var internship_items = document.getElementsByClassName('internship-item').length;
    var introduced_items = document.getElementsByClassName('introduced-item').length;
    var entertainment_items = document.getElementsByClassName('entertainment-item').length;

    for(var i=0; i<internship_items; i++){
        internship_item = document.getElementById('internship_'+i);

        internship_title = internship_item.getElementsByTagName('input')[1].value;
        employer = internship_item.getElementsByTagName('input')[0].value;
        city = internship_item.getElementsByTagName('input')[2].value;
        start_date = internship_item.getElementsByTagName('input')[3].value;
        end_date = internship_item.getElementsByTagName('input')[4].value;
        text = internship_item.getElementsByTagName('textarea')[0].value;
        internship_id = i;

        if(internship_title != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_internship/',
            data:{
                'title': internship_title,
                'employer': employer,
                'city': city,
                'start_date': start_date,
                'end_date': end_date,
                'text': text,
                'internship_id': internship_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }

    for(var i=0; i<introduced_items; i++){
        var introduced_item = document.getElementById('introduced_'+i);

        var name = introduced_item.getElementsByTagName('input')[1].value;
        var company_name = introduced_item.getElementsByTagName('input')[0].value;
        var email = introduced_item.getElementsByTagName('input')[2].value;
        var phone = introduced_item.getElementsByTagName('input')[3].value;
        var introduced_id = i;

        if(name != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_introduced/',
            data:{
                'name': name,
                'company_name': company_name,
                'email': email,
                'phone': phone,
                'introduced_id': introduced_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }

    for(var i=0; i<entertainment_items; i++){
        var entertainment_item = document.getElementById('entertainment_'+i);

        var name = entertainment_item.getElementsByTagName('input')[0].value;
        var entertainment_id = i;

        if(name != ""){
            $.ajax({
            method:'POST',
            url:'/create-resume/savedata/user_entertainment/',
            data:{
                'name': name,
                'entertainment_id': entertainment_id,
                'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
            }
        });
        }

    }
}

function submit_forms(){
    document.getElementById('form1').submit();
}

function switch_page(direction){
    var Pages = ["personal-info","skills","education","job","project","other"];
    var current_page = $('.active-tab')[1].id;
    if (direction == 'nex'){

        if (Pages.indexOf(current_page) < Pages.length - 1){
            var next_page = Pages[Pages.indexOf(current_page) + 1];
            $('.pre-btn')[0].style.display = 'block';
            pages(next_page);
            if (next_page == "other")
            {
            $('.nex-btn')[0].style.display = 'none';
            $('.down-btn')[0].style.bottom = '120px';
            $('.pre-btn')[0].style.display = 'block';
            }

        else if (next_page == "personal-info"){
            $('.pre-btn')[0].style.display = 'none';
            $('.down-btn')[0].style.bottom = '160px';
            $('.nex-btn')[0].style.display = 'block';
            }

        else{
            $('.pre-btn')[0].style.display = 'block';
            $('.down-btn')[0].style.bottom = '160px';
            $('.nex-btn')[0].style.display = 'block';
            }
        }
    }

    if (direction == 'pre'){
        if (Pages.indexOf(current_page) > 0){
            var pre_page = Pages[Pages.indexOf(current_page) - 1];
            pages(pre_page);
            if(pre_page == 'project'){
                $('.nex-btn')[0].style.display = 'block';
                $('.down-btn')[0].style.bottom = '160px';
            }
            if (pre_page == 'personal-info'){
                $('.pre-btn')[0].style.display = 'none';
            }
        }
    }
}

var resume_template_id = 0;
function resume_id(rid) {
    rid = rid.replace('resume_','');
    resume_template_id = rid;
    // $('.resume-template')[0].className = "resume-template invisible";
    var test = document.getElementsByClassName('resume-template')[0];
    test.className = "resume-template invisible";
    // var nextab = $('.resume-info')[0];
    var nextab = document.getElementsByClassName('resume-info')[0];
    nextab.className = "resume-info";
    window.scrollTo(0,0);
}

// Generate the PDF.
function topdf() {
    var element = document.getElementById('Resume');
    var watermark = document.getElementsByClassName('watermark')[0];
    if (watermark) {
        watermark.style.display = 'block';
    }
    html2pdf().from(element).set({
        margin: [0, -0.218, 0, 0],
        filename: 'samplepdf.pdf',
        image: { type: 'jpeg', quality: 4 },
        html2canvas: {
            quality: 4,
            scale: 5,
        },
        jsPDF: { orientation: 'p', unit: 'cm', format: [30, 21] }
    }).save();
}