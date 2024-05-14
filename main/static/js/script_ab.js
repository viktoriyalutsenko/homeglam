        const reviewsSlider = document.querySelector('.reviews-slider');
        const prevBtn = document.querySelector('.prev-btn');
        const nextBtn = document.querySelector('.next-btn');

        let currentSlide = 0;
        const slideWidth = reviewsSlider.offsetWidth;

        prevBtn.addEventListener('click', () => {
            currentSlide = Math.max(currentSlide - 1, 0);
            reviewsSlider.scrollTo({
                left: currentSlide * slideWidth,
                behavior: 'smooth'
            });
        });

        nextBtn.addEventListener('click', () => {
            currentSlide = Math.min(currentSlide + 1, reviewsSlider.children.length - 1);
            reviewsSlider.scrollTo({
                left: currentSlide * slideWidth,
                behavior: 'smooth'
            });
        });