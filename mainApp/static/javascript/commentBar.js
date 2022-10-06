const btncommentOpen = document.getElementById('btn-open')
const btncommentOpen2 = document.getElementById('btn-open-2')
const btncommentClose = document.getElementById('btn-close')
const comment = document.querySelector(".comment-nav");

const togglecomment = function () {
    comment.classList.toggle("open");
}

btncommentOpen.addEventListener("click", function (e) {
    e.stopPropagation();
    togglecomment();
});

btncommentOpen2.addEventListener("click", function (e) {
    e.stopPropagation();
    togglecomment();
});

btncommentClose.addEventListener("click", function (e) {
    e.stopPropagation();
    togglecomment();
});

document.addEventListener("click", function (e) {
    const target = e.target;
    const its_comment = target == comment || comment.contains(target);
    const its_btncomment = target == btncommentOpen;
    const comment_is_active = comment.classList.contains("open");

    if (!its_comment && !its_btncomment && comment_is_active) {
        togglecomment();
    }
});