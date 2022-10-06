const btnMenuOpen = document.getElementById('menu-open')
const menu = document.querySelector(".nav-menu");

const toggleMenu = function () {
    menu.classList.toggle("open");
}

btnMenuOpen.addEventListener("click", function (e) {
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