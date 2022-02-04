$(document).ready(function () {
    animatetoID(localStorage.getItem("sectionId"))
})
function animatetoID(id) {
    $('html, body').animate({
        scrollTop: $("#" + id).offset().top
    }, 1000);
}

function setScroll(sectionId) {
    localStorage.setItem("sectionId", sectionId);
    window.location = 'http://127.0.0.1:8000/about/'

}
