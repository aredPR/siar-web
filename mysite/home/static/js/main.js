function scrollToSection() {
    document.getElementById('que-es').scrollIntoView({ behavior: 'smooth' });
}

// Sección Producto 
document.addEventListener('DOMContentLoaded', function() {
    const downloadBtn = document.querySelector('.download-btn');
    const downloadIcon = document.querySelector('.download-icon');
    
    if (downloadBtn && downloadIcon) {
      downloadBtn.addEventListener('mouseenter', function() {
        downloadIcon.classList.add('animate-bounce');
      });
      
      downloadBtn.addEventListener('mouseleave', function() {
        downloadIcon.classList.remove('animate-bounce');
      });
    }
    
    // Animación para las imágenes al hacer scroll
    const animateOnScroll = function() {
      const images = document.querySelectorAll('.relative img');
      
      images.forEach(image => {
        const imagePosition = image.getBoundingClientRect().top;
        const screenPosition = window.innerHeight / 1.3;
        
        if (imagePosition < screenPosition) {
          image.classList.add('scale-105');
          setTimeout(() => {
            image.classList.remove('scale-105');
          }, 500);
        }
      });
    };
    
    window.addEventListener('scroll', animateOnScroll);
  });