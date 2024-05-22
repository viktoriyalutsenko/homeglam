// Получаем все кнопки "Добавить в корзину"
const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

// Добавляем обработчик события для каждой кнопки
addToCartButtons.forEach(button => {
    button.addEventListener('click', addToCart);
});

// Функция, которая добавляет товар в корзину
function addToCart(event) {
    const button = event.target;
    const product = button.closest('.product-card');
    const productId = product.dataset.productId;

    fetch(`/add-to-cart/${productId}/`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        alert(`Вы добавили "${data.product_name}" в корзину за ${data.product_price} руб.`);
    })
    .catch(error => {
        console.error('Ошибка при добавлении товара в корзину:', error);
    });
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}