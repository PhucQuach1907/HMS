let data, user_id;
document.addEventListener('DOMContentLoaded', async function () {
    data = await authorizationUser();
    if (data.user_type === "patient") {
        findPatientByUserId(data.id).then(id => user_id = id);
        displayUserInfo(data.id);
    } else if (data.user_type === "doctor") {
        findDoctorByUserId(data.id).then(id => user_id = id);
        displayDoctorInfo(data.id);
    }

    document.getElementById('edit-button').addEventListener('click', function () {
        document.getElementById('edit-login_id').value = data.login_id;
        document.getElementById('edit-last_name').value = data.fullname.last_name;
        document.getElementById('edit-mid_name').value = data.fullname.mid_name;
        document.getElementById('edit-first_name').value = data.fullname.first_name;
        document.getElementById('edit-phone_number').value = data.phone_number;
        document.getElementById('edit-noHouse').value = data.address.noHouse;
        document.getElementById('edit-street').value = data.address.street;
        document.getElementById('edit-district').value = data.address.district;
        document.getElementById('edit-city').value = data.address.city;
        document.getElementById('edit-country').value = data.address.country;
        document.getElementById('edit-gender').value = data.gender;
        document.getElementById('edit-dob').value = data.dob;

        if (data.user_type === 'doctor') {
            document.getElementById('edit-specialty-group').classList.remove('hidden');
            document.getElementById('edit-degree-group').classList.remove('hidden');
            document.getElementById('edit-specialty').value = data.specialty;
            document.getElementById('edit-degree').value = data.degree;
        }

        document.getElementById('edit-popup').style.display = 'block';
    })
})

document.querySelector('.close-button').addEventListener('click', function () {
    document.getElementById('edit-popup').style.display = 'none';
});

document.getElementById('logout-button').addEventListener('click', function () {
    sessionStorage.removeItem('token');
    window.location.href = 'login.html';
});

document.getElementById('edit-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const updatedData = {
        password: data.password,
        login_id: data.login_id,
        username: data.username,
        phone_number: document.getElementById('edit-phone_number').value,
        fullname: {
            first_name: document.getElementById('edit-first_name').value,
            mid_name: document.getElementById('edit-mid_name').value,
            last_name: document.getElementById('edit-last_name').value
        },
        address: {
            noHouse: document.getElementById('edit-noHouse').value,
            street: document.getElementById('edit-street').value,
            district: document.getElementById('edit-district').value,
            city: document.getElementById('edit-city').value,
            country: document.getElementById('edit-country').value
        },
        gender: document.getElementById('edit-gender').value,
        dob: document.getElementById('edit-dob').value,
        user_type: data.user_type,
    };

    try {
        const response = await fetch(`http://127.0.0.1:8081/api/user/user-info/${data.id}/`, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(updatedData)
        });

        if (response.ok) {
            alert('Thông tin đã được cập nhật thành công');
            window.location.reload();
        } else {
            console.log(response.message);
            alert('Cập nhật thông tin thất bại');
        }
    } catch (error) {
        console.error('Error updating user info:', error);
        alert('Đã xảy ra lỗi, vui lòng thử lại sau!');
    }
});


function displayUserInfo(userID) {
    fetch(`http://127.0.0.1:8081/api/user/user-info/${userID}/`)
        .then(response => {
            return response.json()
        })
        .then(data => {
            document.getElementById('login_id').textContent = data.login_id;
            document.getElementById('username').textContent = data.fullname.last_name + " " + data.fullname.mid_name + " " + data.fullname.first_name;
            document.getElementById('phone_number').textContent = data.phone_number;
            document.getElementById('address').textContent = data.address.noHouse + ", " + data.address.street + ", " + data.address.district + ", " + data.address.city + ", " + data.address.country;
            document.getElementById('gender').textContent = data.gender;
            document.getElementById('dob').textContent = new Date(data.dob).toLocaleDateString();
            document.getElementById('user_type').textContent = data.user_type;
        })
}

function displayDoctorInfo(userID) {
    displayUserInfo(userID);
    fetch(`http://127.0.0.1:8083/api/doctor/${user_id}/`)
        .then(response => {
            return response.json()
        })
        .then(data => {
            document.getElementById("specialty-field").classList.remove("hidden");
            document.getElementById("degree-field").classList.remove("hidden");
            document.getElementById("specialty").textContent = data.specialty;
            document.getElementById("degree").textContent = data.degree;
        })
}