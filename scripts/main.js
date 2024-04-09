// Обработчик события клика на кнопки переключения языка
document.querySelectorAll('.lang').forEach(item => {
    item.addEventListener('click', event => {
        event.preventDefault();
        const lang = item.getAttribute('data-lang');
        changeLanguage(lang);
    });
});

// Функция изменения языка контента
function changeLanguage(lang) {
    // Здесь можно добавить логику для изменения текста на странице в соответствии с выбранным языком
    // Например, использовать объект с переводами для каждого языка
    // Или загружать контент с сервера в соответствии с выбранным языком
    console.log(`Выбран язык: ${lang}`);
}

