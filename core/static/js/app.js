// static/js/app.js

document.addEventListener('DOMContentLoaded', () => {
    loadNewImages();
});

function loadNewImages() {
    fetch('/get-images/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Images loaded:', data);
            document.getElementById('left-image').src = data.left_image_path;
            document.getElementById('right-image').src = data.right_image_path;
            document.getElementById('left-image').dataset.name = data.left_image_name;
            document.getElementById('right-image').dataset.name = data.right_image_name;
        })
        .catch(error => console.error('Error loading images:', error));
}

function vote(choice) {
    let leftImage = document.getElementById('left-image');
    let rightImage = document.getElementById('right-image');
    let chosenImage, otherImage;

    if (choice === 'left') {
        chosenImage = leftImage.dataset.name;
        otherImage = rightImage.dataset.name;
    } else {
        chosenImage = rightImage.dataset.name;
        otherImage = leftImage.dataset.name;
    }

    fetch(`/vote?chosen=${chosenImage}&other=${otherImage}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Vote registered:', data);
            loadNewImages(); // Load new images after voting
        })
        .catch(error => console.error('Error voting:', error));
}
