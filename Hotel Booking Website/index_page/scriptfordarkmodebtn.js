document.addEventListener('DOMContentLoaded', function() {
    const modeToggle = document.getElementById('mode-toggle');
    const icon = document.getElementById('icon');
  
    modeToggle.addEventListener('click', function() {
      document.body.classList.toggle('dark-mode');
    // const arr = document.querySelectorAll('div');
    // for(const i of arr) i.classList.toggle('dark-mode');
      const isDarkMode = document.body.classList.contains('dark-mode');
      icon.className = isDarkMode ? 'ri-moon-line' : 'ri-sun-line';
    });
  });
  