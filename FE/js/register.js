document.addEventListener('DOMContentLoaded', function () {
    const registerForm = document.getElementById('register-form');

    registerForm.addEventListener('submit', async function (e) {
        e.preventDefault();

        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;
        const firstName = document.getElementById('first_name').value;
        const midName = document.getElementById('mid_name').value;
        const lastName = document.getElementById('last_name').value;
        const noHouse = document.getElementById('noHouse').value;
        const street = document.getElementById('street').value;
        const district = document.getElementById('district').value;
        const city = document.getElementById('city').value;
        const country = document.getElementById('country').value;
        const gender = document.getElementById('gender').value;
        const dob = document.getElementById('dob').value;
        const phoneNumber = document.getElementById('phone_number').value;

        const userData = {
            username: username,
            password: password,
            gender: gender,
            dob: dob,
            phone_number: phoneNumber,
            fullname: {
                first_name: firstName,
                mid_name: midName,
                last_name: lastName
            },
            address: {
                noHouse: noHouse,
                street: street,
                district: district,
                city: city,
                country: country
            },
            user_type: "patient"
        };

        await fetch('http://127.0.0.1:8081/api/user/register/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(userData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.errors) {
                    alert(data.errors);
                } else {
                    fetch('http://127.0.0.1:8082/api/patient/', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({
                            user_id: data.id
                        })
                    })
                    alert("ID đăng nhập của bạn là: " + data.login_id)
                    window.location.href = "login.html";
                }
            });
    });
});
