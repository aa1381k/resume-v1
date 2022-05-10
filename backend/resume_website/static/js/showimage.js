var uploadfile = function(event) {
    var output = document.getElementsByClassName('profileimage')[0];
    output.src = URL.createObjectURL(event.target.files[0]);
    output.onload = function() {
      URL.revokeObjectURL(output.src) // free memory
    }
  };

function removeprofileimage() {
    var default_image = 'http://127.0.0.1:8000/static/images/user.png';
    var image = document.getElementsByClassName('profileimage')[0].src;

    if (image != default_image) {
        document.getElementsByClassName('profileimage')[0].src = default_image;
        document.getElementById('removeimage').style.display = 'none';
    }
}

// (function () {
//     var profile_default_image = 'http://127.0.0.1:5500/frontend/images/user.png';
//     var recent_profile_image = document.getElementsByClassName('profileimage')[0].src;
//
//     if (recent_profile_image === profile_default_image) {
//         document.getElementById('removeimage').style.display = 'none';
//     }
//
//     else{
//         document.getElementById('removeimage').style.display = 'inline';
//     }
//
// })();


