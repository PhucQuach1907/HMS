async function authorizationUser() {
    const token = sessionStorage.getItem('token');
    if (!token) {
        alert("Vui lòng đăng nhập!");
        window.location.href = "login.html";
        return null;
    }

    const decodeTokenUrl = 'http://127.0.0.1:8081/api/user/decode-token/';

    try {
        const response = await fetch(decodeTokenUrl, {
            method: 'GET',
            headers: {
                'Authorization': `Bearer ${token}`,
                'Content-Type': 'application/json'
            }
        });

        if (!response.ok) {
            alert("Vui lòng đăng nhập lại!");
            window.location.href = "login.html";
            return null;
        }

        const data = await response.json();
        return data;

    } catch (error) {
        console.error('Error during authorization:', error);
        alert("Đã xảy ra lỗi, vui lòng thử lại sau!");
        return null;
    }
}

async function findPatientByUserId(userId) {
    try {
        const response = await fetch('http://127.0.0.1:8082/api/patient/');
        const patients = await response.json();
        const patient = patients.find(patient => patient.user_id === userId);

        if (patient) {
            console.log('Patient found:', patient);
            return patient.id;
        } else {
            console.log('Patient not found');
            return null;
        }
    } catch (error) {
        console.error('Error fetching patients:', error);
        return null;
    }
}

async function findDoctorByUserId(userId) {
    try {
        const response = await fetch('http://127.0.0.1:8083/api/doctor/');
        const doctors = await response.json();
        const doctor = doctors.find(doctor => doctor.user_id === userId);

        if (doctor) {
            console.log('Doctor found:', doctor);
            return doctor.id;
        } else {
            console.log('Doctor not found');
            return null;
        }
    } catch (error) {
        console.error('Error fetching doctors:', error);
        return null;
    }
}
