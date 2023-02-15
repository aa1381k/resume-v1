var df_scale = 1;
$(window).resize(function() {
    
});


var resume = document.getElementsByClassName("resume-preview")[0];

function RGBToHex(rgb) {
    // Choose correct separator
    let sep = rgb.indexOf(",") > -1 ? "," : " ";
    // Turn "rgb(r,g,b)" into [r,g,b]
    rgb = rgb.substr(4).split(")")[0].split(sep);
  
    let r = (+rgb[0]).toString(16),
        g = (+rgb[1]).toString(16),
        b = (+rgb[2]).toString(16);
  
    if (r.length == 1)
      r = "0" + r;
    if (g.length == 1)
      g = "0" + g;
    if (b.length == 1)
      b = "0" + b;
  
    return "#" + r + g + b;
  }

function changecolor(color, element) {
    var elements = resume.getElementsByTagName('h2');
    var bg_elements = resume.getElementsByClassName('bg');
    var font_elements = resume.getElementsByClassName('font');
    var head_bg = resume.getElementsByClassName('head')[0];
    var footer_bg = resume.getElementsByClassName('footer')[0];

    for (var i = 0; i < elements.length; i++) {
        elements[i].style.color = color;
    }
    for (var i = 0; i < bg_elements.length; i++) {
        bg_elements[i].style.backgroundColor = color;
    }
    for (var i = 0; i < font_elements.length; i++) {
        font_elements[i].style.color = color;
    }

    head_bg.style.backgroundColor = color;
    footer_bg.style.backgroundColor = color;
}

function changefont(font) {
    var elements = resume.querySelectorAll('*');
    for (var i = 0; i < elements.length; i++) {
        console.log(elements[i].tagName);

        if(elements[i].tagName != "I"){

            elements[i].style.fontFamily = font;
            
        }
    }
}

function topdf() {
    var element = document.getElementById('Resume');
    // element.style.marginTop = "0px";
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


function showcolor(){
    $(".resume-color-m")[0].click();
}

 document.getElementById("testimage").addEventListener("click", function() {
	html2canvas(document.getElementById("Resume")).then(function (canvas) {
            var anchorTag = document.createElement("a");
			document.body.appendChild(anchorTag);
			// document.getElementById("previewImg").appendChild(canvas);
			anchorTag.download = "filename.jpg";
			anchorTag.href = canvas.toDataURL();
			anchorTag.target = '_blank';
			anchorTag.click();
		});
 });