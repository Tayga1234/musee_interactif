// ========================
// Smooth Scroll pour le menu
// ========================
document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');

  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      if (link.hash !== "") {
        e.preventDefault();
        const target = document.querySelector(link.hash);
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });
});

// ========================
// Simple fade-in animation pour sections
// ========================
function revealOnScroll() {
  const reveals = document.querySelectorAll('section');

  for (let i = 0; i < reveals.length; i++) {
    const windowHeight = window.innerHeight;
    const elementTop = reveals[i].getBoundingClientRect().top;
    const elementVisible = 150;

    if (elementTop < windowHeight - elementVisible) {
      reveals[i].classList.add('active');
    } else {
      reveals[i].classList.remove('active');
    }
  }
}

window.addEventListener('scroll', revealOnScroll);
window.addEventListener('load', revealOnScroll);

// ========================
// Navbar sticky après scroll
// ========================
window.addEventListener('scroll', () => {
  const navbar = document.querySelector('.navbar');
  if (window.scrollY > 50) {
    navbar.classList.add('sticky');
  } else {
    navbar.classList.remove('sticky');
  }
});

// ========================
// Carrousel simple pour les œuvres (optionnel)
// ========================
const carousels = document.querySelectorAll('.carousel');
carousels.forEach(carousel => {
  let index = 0;
  const items = carousel.querySelectorAll('.carousel-item');
  const total = items.length;

  function showSlide(i) {
    items.forEach((item, idx) => {
      item.style.display = idx === i ? 'block' : 'none';
    });
  }

  showSlide(index);

  setInterval(() => {
    index = (index + 1) % total;
    showSlide(index);
  }, 4000);
});
