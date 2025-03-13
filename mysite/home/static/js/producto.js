document.addEventListener('DOMContentLoaded', function() {
    // Función para animar elementos cuando son visibles
    function animateOnScroll() {
        const elements = document.querySelectorAll('.animate-fade-in');
        const timelineItems = document.querySelectorAll('.timeline-item');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementBottom = element.getBoundingClientRect().bottom;
            
            // Si el elemento está visible en la ventana
            if (elementTop < window.innerHeight - 100 && elementBottom > 0) {
                element.classList.add('active');
            }
        });
        
        timelineItems.forEach(item => {
            const itemTop = item.getBoundingClientRect().top;
            const itemBottom = item.getBoundingClientRect().bottom;
            
            // Si el elemento está visible en la ventana
            if (itemTop < window.innerHeight - 100 && itemBottom > 0) {
                item.classList.add('active');
            }
        });
    }
    
    // Ejecutar al cargar la página
    animateOnScroll();
    
    // Ejecutar al hacer scroll
    window.addEventListener('scroll', animateOnScroll);
    
    // Mejorar la interactividad del producto arrastrable
    const product = document.getElementById('product');
    const exit = document.getElementById('exit');
    const deactivateBtn = document.getElementById('deactivate-btn');
    const resetBtn = document.getElementById('reset-btn');
    const alarmStatus = document.getElementById('alarm-status');
    const notificationArea = document.getElementById('notification-area');
    
    let isDragging = false;
    let isDeactivated = false;
    let productRect, exitRect;
    
    // Posición inicial del producto
    let initialLeft, initialTop;
    
    // Guardar posición inicial
    function saveInitialPosition() {
        const rect = product.getBoundingClientRect();
        initialLeft = rect.left;
        initialTop = rect.top;
    }
    
    // Inicializar
    saveInitialPosition();
    
    // Eventos para arrastrar el producto
    product.addEventListener('mousedown', startDrag);
    product.addEventListener('touchstart', startDrag, { passive: false });
    
    function startDrag(e) {
        e.preventDefault();
        isDragging = true;
        
        // Añadir efecto visual al arrastrar
        product.style.boxShadow = '0 0 15px rgba(255, 0, 0, 0.7)';
        product.style.zIndex = '100';
        
        document.addEventListener('mousemove', drag);
        document.addEventListener('touchmove', drag, { passive: false });
        document.addEventListener('mouseup', stopDrag);
        document.addEventListener('touchend', stopDrag);
    }
    
    function drag(e) {
        if (!isDragging) return;
        
        const storeImage = document.getElementById('store-image');
        const storeRect = storeImage.getBoundingClientRect();
        
        let clientX, clientY;
        
        if (e.type === 'touchmove') {
            clientX = e.touches[0].clientX;
            clientY = e.touches[0].clientY;
        } else {
            clientX = e.clientX;
            clientY = e.clientY;
        }
        
        // Limitar el movimiento dentro de la imagen de la tienda
        const x = Math.max(storeRect.left, Math.min(clientX, storeRect.right));
        const y = Math.max(storeRect.top, Math.min(clientY, storeRect.bottom));
        
        // Posicionar el producto
        product.style.left = (x - storeRect.left) + 'px';
        product.style.top = (y - storeRect.top) + 'px';
        product.style.transform = 'none';
        
        // Comprobar colisión con la salida
        checkCollision();
    }
    
    function stopDrag() {
        if (!isDragging) return;
        
        isDragging = false;
        product.style.boxShadow = '';
        
        document.removeEventListener('mousemove', drag);
        document.removeEventListener('touchmove', drag);
        document.removeEventListener('mouseup', stopDrag);
        document.removeEventListener('touchend', stopDrag);
        
        // Comprobar colisión final
        checkCollision();
    }
    
    function checkCollision() {
        productRect = product.getBoundingClientRect();
        exitRect = exit.getBoundingClientRect();
        
        // Si hay colisión y el llavero no está desactivado
        if (isColliding(productRect, exitRect) && !isDeactivated) {
            triggerAlarm();
        }
    }
    
    function isColliding(rect1, rect2) {
        return !(
            rect1.right < rect2.left || 
            rect1.left > rect2.right || 
            rect1.bottom < rect2.top || 
            rect1.top > rect2.bottom
        );
    }
    
    function triggerAlarm() {
        // Mostrar alerta en la página
        alarmStatus.className = 'p-3 sm:p-4 bg-danger text-white rounded-lg mb-3 sm:mb-4 text-sm sm:text-base';
        alarmStatus.innerHTML = 'Estado: ¡ALARMA ACTIVADA!';
        
        // Mostrar notificación
        notificationArea.classList.remove('hidden');
        
        // Añadir efecto de vibración al producto
        product.classList.add('animate-pulse');
        
        // Añadir efecto de parpadeo a la salida
        exit.style.animation = 'pulse 0.5s infinite';
        exit.style.borderColor = 'red';
    }
    
    // Desactivar llavero
    deactivateBtn.addEventListener('click', function() {
        isDeactivated = true;
        product.style.backgroundColor = 'green';
        alarmStatus.className = 'p-3 sm:p-4 bg-green-100 text-green-800 rounded-lg mb-3 sm:mb-4 text-sm sm:text-base';
        alarmStatus.innerHTML = 'Estado: Llavero desactivado';
        notificationArea.classList.add('hidden');
        
        // Añadir efecto visual
        deactivateBtn.classList.add('animate-pulse');
        setTimeout(() => {
            deactivateBtn.classList.remove('animate-pulse');
        }, 1000);
    });
    
    // Reiniciar demo
    resetBtn.addEventListener('click', function() {
        isDeactivated = false;
        product.style.backgroundColor = '';
        product.style.left = '';
        product.style.top = '';
        product.style.transform = '-translate-x-1/2 -translate-y-1/2';
        product.classList.remove('animate-pulse');
        
        alarmStatus.className = 'p-3 sm:p-4 bg-green-100 text-green-800 rounded-lg mb-3 sm:mb-4 text-sm sm:text-base';
        alarmStatus.innerHTML = 'Estado: Sistema listo';
        notificationArea.classList.add('hidden');
        
        exit.style.animation = '';
        exit.style.borderColor = '';
        
        // Añadir efecto visual
        resetBtn.classList.add('animate-pulse');
        setTimeout(() => {
            resetBtn.classList.remove('animate-pulse');
        }, 1000);
    });
});