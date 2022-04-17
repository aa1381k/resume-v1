function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#profileimage')
                .attr('src', e.target.result)
                .width(150)
                .height(200);
                document.getElementById('removeimage').style.display = 'inline';
        };

        reader.readAsDataURL(input.files[0]);
    }
}

function removeprofileimage() {
    var default_image = 'http://127.0.0.1:8000/static/images/user.png';
    var image = document.getElementById('profileimage').src;

    if (image != default_image) {
        document.getElementById('profileimage').src = default_image;
        document.getElementById('removeimage').style.display = 'none';
    }
}

(function () {
    var profile_default_image = 'http://127.0.0.1:5500/frontend/images/user.png';
    var recent_profile_image = document.getElementById('profileimage').src;

    if (recent_profile_image === profile_default_image) {
        document.getElementById('removeimage').style.display = 'none';
    }

    else{
        document.getElementById('removeimage').style.display = 'inline';
    }

})();


