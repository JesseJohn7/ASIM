document.getElementById('signupForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const firstName = document.getElementById('firstName').value;
    const lastName = document.getElementById('lastName').value;
    const employmentStatus = document.getElementById('employmentStatus').value;
    const phoneNumber = document.getElementById('phoneNumber').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

     if (firstName && lastName && employmentStatus && phoneNumber && email && password) {
        window.location.href = '../Sign Up 2/index.html';
    } else {
        alert('Please fill all fields');
    } 
});