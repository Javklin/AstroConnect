const apiUrl = 'http://127.0.0.1:5000/stars';

async function loadStars(category) {
    const constellationOption = document.querySelector('input[name="constellation"]:checked').value;
    const categoryWithConstellation = constellationOption === 'avec' ? `const_${category}` : category;
    const response = await fetch(`${apiUrl}?category=${categoryWithConstellation}`);
    const stars = await response.json();

    renderSkyMap(stars);
}

function renderSkyMap(stars) {
    const skyMap = document.getElementById('sky-map');
    skyMap.innerHTML = '';

    const bounds = {
        raMin: Math.min(...stars.map(star => star.ra)),
        raMax: Math.max(...stars.map(star => star.ra)),
        decMin: Math.min(...stars.map(star => star.dec)),
        decMax: Math.max(...stars.map(star => star.dec)),
    };

    stars.forEach(star => {
        const normalizedX = ((star.ra - bounds.raMin) / (bounds.raMax - bounds.raMin)) * 100;
        const normalizedY = ((star.dec - bounds.decMin) / (bounds.decMax - bounds.decMin)) * 100;


        if (normalizedX >= 0 && normalizedX <= 100 && normalizedY >= 0 && normalizedY <= 100) {
            const starElement = document.createElement('div');
            starElement.className = 'star';
            starElement.style.left = `${normalizedX}%`;
            starElement.style.top = `${normalizedY}%`;
            starElement.style.width = `${Math.max(5, Math.min(15, star.lum * 2))}px`; 
            starElement.style.height = `${Math.max(5, Math.min(15, star.lum * 2))}px`;
            starElement.title = `Désignation: ${star.proper || 'Inconnu'} (Constellation: ${star.con || 'Inconnu'})`;


            skyMap.appendChild(starElement);
        }
    });
}
