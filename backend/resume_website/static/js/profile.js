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

    if (tab.id == "profile-settings") {
        tab.className = "btn active";
        document.getElementsByClassName("setting-body")[0].style.display = "block";
        recent_tab = tab.id;
        recent_page = "setting-body";
    }


}


function showpost(post,post_id) {
    work_samples_images(post_id);
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


function addpost(){
    $("#add-post").modal("show");
}

function removeimage(loc) {
    var default_image = 'http://127.0.0.1:8000/static/images/new-post.gif';
    var image = document.getElementsByClassName(loc)[0].src;

    if (image != default_image) {
        document.getElementsByClassName(loc)[0].src = default_image;
        document.getElementsByClassName("custom-file-remove")[0].style.display = 'none';
    }
}


function readURL(input,loc) {
    console.log(input.files);
   for (var i=0; i<input.files.length; i++) {
        var reader = new FileReader();
    // var image_tag_count = document.getElementsByClassName('images')[0];
    // image_tag_count = image_tag_count.getElementsByTagName('img').length;

        reader.onload = function (e) {

            var new_image = document.createElement('img');
            new_image.src = e.target.result;
            new_image.className = 'd-block w-100';
            var image = document.createElement('div');
            image.className = 'carousel-item';
            image.appendChild(new_image);
            var image_section = document.getElementsByClassName("carousel-inner")[0];
            image_section.appendChild(image);


            document.getElementsByClassName('custom-file-remove')[0].style.display = 'block';

        };


        reader.readAsDataURL(input.files[i]);
   }


}


function work_samples_images(post_id){
    $.ajax({
        url: '/account/user_work_samples/work_samples_images/',
        method: 'POST',
        data: {
            "post_id": post_id,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
        success: function (data) {
            data = data.replace("{","");
            data = data.replace("}","");
            data = data.split(",");
            var node =document.getElementById("show_post_modal");
            while(node.lastChild){
                node.lastChild.remove();
            }
            for (var i = 0; i < data.length; i++) {
                var parent = document.createElement("div");
                if (i == 0) {
                    parent.className = "carousel-item active";
                }
                else {
                    parent.className = "carousel-item";
                }
                var new_image = document.createElement('img');
                new_image.src = "/medias/" + data[i];
                new_image.className = 'col-md-12';
                parent.appendChild(new_image);
                document.getElementById("show_post_modal").appendChild(parent);
            }

            if (data.length < 2) {
                document.getElementsByClassName('carousel-control-prev')[0].style.display = 'none';
                document.getElementsByClassName('carousel-control-next')[0].style.display = 'none';
            }
            else {
                document.getElementsByClassName('carousel-control-prev')[0].style.display = 'flex';
                document.getElementsByClassName('carousel-control-next')[0].style.display = 'flex';
            }
        }
    });

}


$('.carousel').attr('data-interval', '1');