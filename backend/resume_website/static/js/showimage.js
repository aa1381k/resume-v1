function readURL(input,loc) {
    console.log(input.files);
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('.'+loc)
                .attr('src', e.target.result)
                // .width(150)
                // .height(200);
                if(loc == "post-image-show"){
                    document.getElementsByClassName('custom-file-remove')[0].style.display = 'block';
                }
                else{
                    document.getElementById('removeimage').style.display = 'inline';
                }
        };

        reader.readAsDataURL(input.files[i]);
    }
}

function removeprofileimage(loc) {
    var default_image = 'http://127.0.0.1:8000/static/images/user.png';
    var image = document.getElementsByClassName(loc)[0].src;

    if (image != default_image) {
        document.getElementsByClassName(loc)[0].src = default_image;
        document.getElementById(loc).style.display = 'none';
    }
}


