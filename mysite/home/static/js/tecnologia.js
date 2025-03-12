// Get all buttons and sections
const allBtn = document.getElementById('all-btn');
const iotBtn = document.getElementById('iot-btn');
const webBtn = document.getElementById('web-btn');
const mobileBtn = document.getElementById('mobile-btn');

const iotSection = document.getElementById('iot-section');
const webSection = document.getElementById('web-section');
const mobileSection = document.getElementById('mobile-section');

// Function to set active button style
function setActiveButton(activeBtn) {
    // Reset all buttons
    [allBtn, iotBtn, webBtn, mobileBtn].forEach(btn => {
        btn.classList.remove('bg-primary', 'text-white');
        btn.classList.add('hover:bg-gray-100');
    });
    
    // Set active button
    activeBtn.classList.add('bg-primary', 'text-white');
    activeBtn.classList.remove('hover:bg-gray-100');
}

// Show all sections
allBtn.addEventListener('click', () => {
    iotSection.style.display = 'block';
    webSection.style.display = 'block';
    mobileSection.style.display = 'block';
    setActiveButton(allBtn);
});

// Show only IoT section
iotBtn.addEventListener('click', () => {
    iotSection.style.display = 'block';
    webSection.style.display = 'none';
    mobileSection.style.display = 'none';
    setActiveButton(iotBtn);
});

// Show only Web section
webBtn.addEventListener('click', () => {
    iotSection.style.display = 'none';
    webSection.style.display = 'block';
    mobileSection.style.display = 'none';
    setActiveButton(webBtn);
});

// Show only Mobile section
mobileBtn.addEventListener('click', () => {
    iotSection.style.display = 'none';
    webSection.style.display = 'none';
    mobileSection.style.display = 'block';
    setActiveButton(mobileBtn);
});