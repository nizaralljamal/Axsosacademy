document.addEventListener('DOMContentLoaded', () => {
    const header = document.querySelector('.header');
    const nextBtn = document.getElementById('nextBtn');
    const prevBtn = document.getElementById('prevBtn');

    const backgrounds = [
        'url(\'calculator-bg.jpg\')',
        'url(\'cta-bg.jpg\')',
        'url(\'heading-bg.jpg\')'
    ];

    let currentBackground = 0;

    function updateBackground() {
        header.style.backgroundImage = backgrounds[currentBackground];
    }

    nextBtn.addEventListener('click', () => {
        currentBackground = (currentBackground + 1) % backgrounds.length;
        updateBackground();
    });

    prevBtn.addEventListener('click', () => {
        currentBackground = (currentBackground - 1 + backgrounds.length) % backgrounds.length;
        updateBackground();
    });

    // Set initial background
    updateBackground();
});