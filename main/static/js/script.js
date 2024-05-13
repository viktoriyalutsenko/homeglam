<script src="https://unpkg.com/swiper/swiper-bundle.min.js"></script>
    <!-- Инициализация Swiper -->
    <script>
        var swiper = new Swiper('.swiper-container', {
            slidesPerView: 1,
            spaceBetween: 30,
            navigation: {
                nextEl: '.swiper-button-next',
                prevEl: '.swiper-button-prev',
            },
            loop: true,
        });
    </script>