document.addEventListener('DOMContentLoaded', function() {
    // Получаем все кнопки "Добавить в корзину"
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');

    // Добавляем обработчик события для каждой кнопки
    addToCartButtons.forEach(button => {
        button.addEventListener('click', addToCart);
    });

    // Функция, которая добавляет товар в корзину
    function addToCart(event) {
        event.preventDefault();
        const button = event.target;
        const product = button.closest('.product-card');
        const productId = product.dataset.productId;

        fetch(`/add-to-cart/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            },
            body: JSON.stringify({ quantity: 1 }) // Пример добавления товара с количеством 1
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert(`Вы добавили "${data.product_name}" в корзину за ${data.product_price} руб.`);
            } else {
                alert('Ошибка при добавлении товара в корзину.');
            }
        })
        .catch(error => {
            console.error('Ошибка при добавлении товара в корзину:', error);
        });
    }

    // Получаем все кнопки "Удалить из корзины"
    const removeFromCartButtons = document.querySelectorAll('.remove-from-cart-btn');

    // Добавляем обработчик события для каждой кнопки
    removeFromCartButtons.forEach(button => {
        button.addEventListener('click', removeFromCart);
    });

    // Функция, которая удаляет товар из корзины
    function removeFromCart(event) {
        event.preventDefault();
        const button = event.target;
        const form = button.closest('form');
        const action = form.action;

        console.log(`Удаление товара по URL: ${action}`); // Логирование URL

        fetch(action, {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => {
            if (response.status === 204) {
                alert('Товар удален из корзины');
                location.reload();
            } else {
                return response.text().then(text => { throw new Error(text); });
            }
        })
        .catch(error => {
            console.error('Ошибка при удалении товара из корзины:', error);
            alert('Ошибка при удалении товара из корзины');
        });
    }

    // Функция для получения CSRF токена
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
});
