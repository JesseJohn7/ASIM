document.getElementById('personal-info-form').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Form submitted!');
    // Handle form submission logic here
});


function redirectToIndex(){
    window.location.href = "../Congratulations/index.html";
}
