const background = document.querySelector('.background-3d');

window.addEventListener('mousemove', (event) => {   
    const { clientX, clientY } = event;
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    const offsetX = (clientX - centerX) / 50;
    const offsetY = (clientY - centerY) / 50;

  background.style.transform = `translate(${offsetX}px, ${offsetY}px) scale(1.1)`;
});

document.getElementById('recommendationForm').addEventListener('submit', function (event) {
  event.preventDefault();
  document.getElementById('result').scrollIntoView({ behavior: 'smooth' });
});