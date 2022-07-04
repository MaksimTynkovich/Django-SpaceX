const btnMenuOpen = document.getElementById('btn-open')
const btnMenuClose = document.getElementById('btn-close')
const btnResponse = document.getElementById('response-btn')
const comment = document.getElementById('comment-reply')
const menu = document.querySelector(".comment-nav");

const toggleMenu = function () {
    menu.classList.toggle("open");
}

btnMenuOpen.addEventListener("click", function (e) {
    e.stopPropagation();
    toggleMenu();
});

btnMenuClose.addEventListener("click", function (e) {
    e.stopPropagation();
    toggleMenu();
});

document.addEventListener("click", function (e) {
    const target = e.target;
    const its_menu = target == menu || menu.contains(target);
    const its_btnMenu = target == btnMenuOpen;
    const menu_is_active = menu.classList.contains("open");

    if (!its_menu && !its_btnMenu && menu_is_active) {
        toggleMenu();
    }
});

btnResponse.addEventListener("click", function () {
    comment.style.display == 'block' ? comment.style.display = 'none' : comment.style.display = 'block'
});