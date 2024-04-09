// Получаем все ссылки меню
const menuLinks = document.querySelectorAll('nav ul li a');

// Функция для подсветки текущего пункта меню
function highlightMenuItem() {
    // Получаем текущее положение на странице
    const currentPosition = window.scrollY;

    // Перебираем все ссылки меню
    menuLinks.forEach(link => {
        const sectionId = link.getAttribute('href').substring(1);
        const section = document.getElementById(sectionId);
        if (section.offsetTop <= currentPosition && section.offsetTop + section.offsetHeight > currentPosition) {
            // Если текущая секция на экране, добавляем класс "active" к соответствующей ссылке
            link.classList.add('active');
        } else {
            // В противном случае, удаляем класс "active"
            link.classList.remove('active');
        }
    });
}

// Вызываем функцию для подсветки текущего пункта меню при загрузке страницы и прокрутке
document.addEventListener('DOMContentLoaded', highlightMenuItem);
window.addEventListener('scroll', highlightMenuItem);

// Добавляем обработчики событий для смены цвета при наведении мыши
menuLinks.forEach(link => {
    link.addEventListener('mouseenter', () => {
        link.style.color = '#DC8CF7'; // Изменяем цвет при наведении мыши
    });

    link.addEventListener('mouseleave', () => {
        link.style.color = '#ffffff'; // Возвращаем изначальный цвет после ухода мыши
    });
});
