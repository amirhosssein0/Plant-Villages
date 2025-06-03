// Placeholder for base JavaScript 

// Fade-in animation for hero section
window.addEventListener('DOMContentLoaded', function() {
    const hero = document.querySelector('.hero');
    if (hero) {
        hero.style.opacity = 0;
        hero.style.transition = 'opacity 1.2s';
        setTimeout(() => {
            hero.style.opacity = 1;
        }, 200);
    }

    // Navbar mobile toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navList = document.querySelector('.nav-list');
    if (navToggle && navList) {
        navToggle.addEventListener('click', function() {
            navList.classList.toggle('active');
        });
    }
}); 