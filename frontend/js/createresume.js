function changeicon(test, index) {
    var selected_value = test.options[test.selectedIndex].value;
    var icon = document.getElementsByClassName('user-social-media-item')[index].getElementsByClassName('item-inputs')[0].getElementsByTagName('i')[0];
    icon.className = 'fa-brands fa-' + selected_value;
}

function addsocial() {
    var index = document.getElementsByClassName('user-social-media-item')
    index = index.length;
    var social = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'user-social-media','user-social-media-item','social')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'user-social-media','user-social-media-item','social')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'user-social-media')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs col-md-12"> <span><i class="fa-brands fa-telegram"></i></span> <div class="social-media-body col-md-12"> <select name="" id="" onchange="changeicon(this,${index})"> <option value="">نام شبکه اجتماعی</option> <option value="linkedin">لینکداین</option> <option value="twitter">توییتر</option> <option value="facebook">فیسبوک</option> <option value="instagram">اینستاگرام</option> <option value="telegram">تلگرام</option> <option value="github">گیت‌هاب</option> <option value="dribbble">دریبل</option> <option value="whatsapp">واتساپ</option> <option value="skype">اسکایپ</option> <option value="youtube">یوتیوب</option> <option value="stack-overflow">StackOverflow</option> </select> <div class="social-media-id">  <input type="text" name="" id="" placeholder="ID"> </div> </div> </div>`;
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
    var lang = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'lang-items','lang-item','lang')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'lang-items','lang-item','lang')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'lang')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs"> <div class="lang col-md-6"> <span>نام زبان</span> <select name="" id=""> <option value="" selected=""></option> <option value="English">انگلیسی</option> <option value="Arabic">عربی</option> <option value="German">آلمانی</option> <option value="France">فرانسوی</option> <option value="Spanish">اسپانیایی</option> <option value="Russian">روسی</option> <option value="Italy">ایتالیایی</option> <option value="Turkish">ترکی استانبولی</option> <option value="Persian">فارسی</option> <option value="China">چینی</option> <option value="Hebrew">عبری</option> <option value="Azerbaijani">ترکی آذربایجانی</option> <option value="Armenian">ارمنی</option> <option value="Japanese">ژاپنی</option> <option value="Georgian">گرجی</option> <option value="Kurdish">کُردی</option> <option value="Portuguese">پرتغالی</option> <option value="Bengali">بنگالی</option> <option value="Lahnda">لندا</option> <option value="Javanese">جاوه‌ای</option> <option value="Korean">کره ای</option> <option value="Vietnamese">ویتنامی</option> <option value="Urdu">اردو</option> <option value="Hindi">هندی</option> <option value="Egyptian">مصری</option> <option value="Telugu">تلوگو</option> <option value="Gujarati">گجراتی</option> <option value="Tamil">تامیلی</option> <option value="Marathi">مراتی</option> <option value="Hungarian">مجاری</option> <option value="Swedish">سوئدی</option> <option value="Pashto">پشتو</option> <option value="Greek">یونانی</option> <option value="Dutch">هلندی</option> <option value="Danish">دانمارکی</option> <option value="Latin">لاتین</option> </select> </div> <div class="lang-rate col-md-5"> <span>سطح</span> <select name="" id=""> <option value="0"></option> <option value="1">نیتیو</option> <option value="2">کاملا مسلط</option> <option value="3">دارای تسلط خوب</option> <option value="4">تسلط کامل به استفاده روزمره</option> <option value="5">تسلط نسبی به استفاده‌ روزمره</option> <option value="6">C2</option> <option value="7">C1</option> <option value="8">B2</option> <option value="9">B1</option> <option value="10">A2</option> <option value="11">A1</option> <option value="12">زبان مادری</option> </select> </div> </div>`;
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
    var certification = `<div class="move-btns"> <span><button class="btn" onclick="moveupelement(this, 'certification-items','certification-item','certification')"><i class="fa-solid fa-angle-up"></i></button></span> <span><button class="btn" onclick="movedownelement(this, 'certification-items','certification-item','certification')"><i class="fa-solid fa-angle-down"></i></button></span> <span><button class="btn" onclick="removeitem(this,'certification')"><i class="fa-solid fa-xmark"></i></button></span> </div> <div class="item-inputs col-md-12 d-flex flex-column align-items-center justify-content-around mt-5 mb-5 "> <div class="col-md-10"> <span>عنوان گواهی نامه</span> <input type="text"> </div> <div class="col-md-10 item-data-inputs"> <div class="col-md-6 d-flex flex-column justify-content-between"> <span>تاریخ شروع و پایان</span> <div class="col-md-12 certification-date"> <div class="col-md-5 skill-date-start"> <input type="text" placeholder="شروع"> </div> <div class="col-md-5 skill-date-end"> <input type="text" placeholder="پایان"> </div> </div> </div> <div class="col-md-5"> <span>عنوان موسسه</span> <input type="text"> </div> </div> </div>`;
    var elem = document.createElement('div');
    elem.id = `certification_${index}`;
    elem.setAttribute('name', `certification_${index}`);
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
    if (index > 1) {
        var elem = document.getElementById(id);
        elem.remove()
    }
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
    console.log(parr);
    console.log(list);
    console.log(sec);
    var arr = document.getElementsByClassName(list);
    var parrent = document.getElementsByClassName(parr)[0];
    id = id.parentElement.parentElement.parentElement.id;
    var arrlen = arr.length;
    console.log(arrlen);
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
var id2 = 'PERSONAL-INFO'
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

        $("#myModal").modal("hide");

        tb1 = lower_id + '-' + 'page';
        id1 = lower_id;
        id2 = upper_id;
    }
}



function test() {
    alert('salaaaaaaam');
}
