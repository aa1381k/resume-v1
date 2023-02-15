var recent_tab = "about-me";
var recent_page = "main-profile-body";

function changetab(tab) {
    document.getElementById(recent_tab).className = "btn";
    document.getElementsByClassName(recent_page)[0].style.display = "none";

    if (tab.id == "about-me") {
        tab.className = "btn Active";
        document.getElementsByClassName("main-profile-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "main-profile-body";
    }

    if (tab.id == "work-samples") {
        tab.className = "btn Active";
        document.getElementsByClassName("work-samples-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "work-samples-body";
    }

    if (tab.id == "contact-me") {
        tab.className = "btn Active";
        document.getElementsByClassName("contact-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "contact-body";
    }

}


function showpost(post) {
    var image = $(post).find("img")[0];
    var image_src = image.src;
    var modal = document.getElementById("myModal");
    var modal_image = document.getElementById("modal-image");
    modal_image.src = image_src;
    var post_title = $(post).find(".work-samples-item-desc-title").find("h6")[0];
    var modal_title = document.getElementById("modal-title");
    modal_title.innerHTML = post_title.innerHTML;
    var post_desc = $(post).find(".desc").find("p")[0];
    var modal_desc = $(".modal-desc")[0];
    modal_desc.innerHTML = post_desc.innerHTML;
    var post_project_link = $(post).find(".links").find("a")[0];
    var modal_project_link = document.getElementById("modal-project-link");
    modal_project_link.href = post_project_link.href;
    $("#myModal").modal("show");
}


function preview(object) {
    var frame = document.getElementById(object);
    frame.src = URL.createObjectURL(event.target.files[0]);
}
function clearImage(object) {
    var frame = document.getElementById(object);
    if (object == "profile-frame") {
        frame.src = "../images/user.png";
    }
    if (object == "bg-frame") {
        frame.src = "../images/curved2.jpg";
    }
}

function edit_section(section_id) {
    var section = document.getElementById(section_id);
    var edit_button = section.getElementsByClassName("edit")[0];
    var remove_button = section.getElementsByClassName("remove")[0];
    var submit_button = section.getElementsByClassName("submit")[0];
    var edit_input = section.getElementsByClassName("form-control")[0];
    var text = section.getElementsByTagName("span")[0];
    text.style.display = "none";
    edit_input.className = "form-control w-50";
    edit_button.style.display = "none";
    remove_button.style.display = "none";
    submit_button.style.display = "block";
}

function submit_edit(section_id) {
    var section = document.getElementById(section_id);
    var edit_button = section.getElementsByClassName("edit")[0];
    var remove_button = section.getElementsByClassName("remove")[0];
    var submit_button = section.getElementsByClassName("submit")[0];
    var edit_input = section.getElementsByClassName("form-control")[0];
    var text = section.getElementsByTagName("span")[0];
    text.innerHTML = edit_input.value;
    text.style.display = "block";
    edit_input.className = "form-control w-50 hidden";
    edit_button.style.display = "block";
    remove_button.style.display = "block";
    submit_button.style.display = "none";
}

function remove_section(section_id) {
    var section = document.getElementById(section_id);
    section.remove();
}

function add_section() {
    var element_lenght = document.getElementById("demo1").getElementsByTagName("li").length;
    var new_element_id = "section_" + (element_lenght + 1);
    var new_element_node = `<li class="list-group-item col-md-7 d-flex justify-content-evenly align-items-center" id="${new_element_id}"> <input type="text" class="form-control w-50 hidden"> <span>New Section</span> <div class="btns d-flex gap"> <button type="button" class="edit btn btn-outline-primary" onclick="edit_section('${new_element_id}')"><i class="bi bi-pencil"></i></button> <button type="button" class="remove btn btn-outline-danger" onclick="remove_section('${new_element_id}')"><i class="bi bi-x-lg"></i></button> <button type="button" class="submit btn btn-outline-success hidden" onclick="submit_edit('${new_element_id}')"><i class="bi bi-check"></i></button> </div>                                 <i class="bi bi-arrow-down-up"></i>
    </li>`;
    document.getElementById("demo1").innerHTML += new_element_node;
}


Sortable.create(demo1, {
    animation: 100,
    group: 'list-1',
    draggable: '.list-group-item',
    handle: '.list-group-item',
    sort: true,
    filter: '.sortable-disabled',
    // chosenClass: 'active'
});