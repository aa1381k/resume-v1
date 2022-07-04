var recent_tab = "about-me";
var recent_page = "main-profile-body";

function changetab(tab) {
    document.getElementById(recent_tab).className = "btn";
    document.getElementsByClassName(recent_page)[0].style.display = "none";

    if (tab.id == "about-me") {
        tab.className = "btn active";
        document.getElementsByClassName("main-profile-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "main-profile-body";
    }

    if (tab.id == "work-samples") {
        tab.className = "btn active";
        document.getElementsByClassName("work-samples-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "work-samples-body";
    }

    if (tab.id == "contact-me") {
        tab.className = "btn active";
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
