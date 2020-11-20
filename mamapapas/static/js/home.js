new WOW().init();
// Боковое меню
/*let menu=$('#mobileMenu'),logo=$('.logo');
menu.hide();
logo.on('click',function(){
    let inxtwo=$('.logo').index(this);
$(menu[inxtwo]).slideToggle(200)
})*/
function openForm() {
    try {
        document.getElementById("popup-form").style.display = "grid";
    }
    catch {
        return false;
    }
}

function closeForm() {
    document.getElementById("popup-form").style.display = "none";
}

//function openTeacher(teacher) {
//    try {
//        document.getElementById(teacher).style.display = "grid";
//    }
//    catch {
//        return false;
//    }
//}
//
//function closeTeacher(teacher) {
//    try {
//        document.getElementById(teacher).style.display = "none";
//    } 
//    catch {
//        return false;
//    }
//}


function openAmshinskayaMonika() {
    document.getElementById("popup-amshinskaya-monika").style.display = "grid";
}
function closeAmshinskayaMonika() {
    document.getElementById("popup-amshinskaya-monika").style.display = "none";
} 

function openPopovaAnna() {
    document.getElementById("popup-popova-anna").style.display = "grid";
}
function closePopovaAnna() {
    document.getElementById("popup-popova-anna").style.display = "none";
} 

function openPashkovskayaKsenia() {
    document.getElementById("popup-pashkovskaya-ksenia").style.display = "grid";
}
function closePashkovskayaKsenia() {
    document.getElementById("popup-pashkovskaya-ksenia").style.display = "none";
} 

function openPopovaAnastasia() {
    document.getElementById("popup-popova-anastasia").style.display = "grid";
}
function closePopovaAnastasia() {
    document.getElementById("popup-popova-anastasia").style.display = "none";
} 

function openAlonVanda() {
    document.getElementById("popup-alon-vanda").style.display = "grid";
}
function closeAlonVanda() {
    document.getElementById("popup-alon-vanda").style.display = "none";
} 

function openBogushOlga() {
    document.getElementById("popup-bogush-olga").style.display = "grid";
}
function closeBogushOlga() {
    document.getElementById("popup-bogush-olga").style.display = "none";
} 

function openAmshinskayaJessika() {
    document.getElementById("popup-amshinskaya-jessika").style.display = "grid";
}
function closeAmshinskayaJessika() {
    document.getElementById("popup-amshinskaya-jessika").style.display = "none";
} 



function openPrivacy(){
    try {
        document.getElementById("popup-privacy").style.display = "grid";
    }
    catch {
        return false;
    }
}
function closePrivacy(){
    try {
        document.getElementById("popup-privacy").style.display = "none";
    }
    catch {
        return false;
    }
}

  
function closeForm() {
    try {
        document.getElementById("callform").style.display = "none";
    }
    catch {
        return false;
    }
}




document.getElementById('call-amshinskaya-monika-popup').onclick = openAmshinskayaMonika;
document.getElementById('popup-amshinskaya-monika-close').onclick = closeAmshinskayaMonika;

document.getElementById('call-popova-anna-popup').onclick = openPopovaAnna;
document.getElementById('popup-popova-anna-close').onclick = closePopovaAnna;

document.getElementById('call-pashkovskaya-ksenia-popup').onclick = openPashkovskayaKsenia;
document.getElementById('popup-pashkovskaya-ksenia-close').onclick = closePashkovskayaKsenia;

document.getElementById('call-popova-anastasia-popup').onclick = openPopovaAnastasia;
document.getElementById('popup-popova-anastasia-close').onclick = closePopovaAnastasia;

document.getElementById('call-alon-vanda-popup').onclick = openAlonVanda;
document.getElementById('popup-alon-vanda-close').onclick = closeAlonVanda;

document.getElementById('call-bogush-olga-popup').onclick = openBogushOlga;
document.getElementById('popup-bogush-olga-close').onclick = closeBogushOlga;

document.getElementById('call-amshinskaya-jessika-popup').onclick = openAmshinskayaJessika;
document.getElementById('popup-amshinskaya-jessika-close').onclick = closeAmshinskayaJessika;

//$('#call-amshinskaya-monika-popup').onclick = openTeacher();

var x = document.getElementsByClassName('call-privacy-popup');
var i;
for (i = 0; i < x.length; i++) {
    x[i].onclick = openPrivacy;
};
document.getElementById('popup-privacy-close').onclick = closePrivacy;

$('.call-privacy-popup').onclick = openPrivacy;
 
  

// Приветствие
$('#play-intro').click(function () {
    $("#play-intro").hide();
    if ($("#hello").get(0).stoped) {
        $("#hello").get(0).play();
    }
    else if ($("#hello").get(0).paused) {
        $("#hello").get(0).play();
    } else {
        $("#hello").get(0).pause();
    }
});

new Glide('#reviews', {
    type: 'carousel',
    startAt: 0,
    perView: 3,
    focusAt: 'center',
    keyboard: true,
    before: 0, 
    after: 0,
    breakpoints: {
        1024: {
            perView: 1,
        },
    }
}).mount();

// FAQ
let faqAnswer=$('.faqAnswer'),faqShow=$('.faqShow');
faqAnswer.hide();
faqShow.on('click',function(){
    let inx=$('.faqShow').index(this);
$(faqAnswer[inx]).slideToggle(200);
})