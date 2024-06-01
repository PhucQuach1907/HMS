let data, user_id;
document.addEventListener('DOMContentLoaded', async function () {
    data = await authorizationUser();
    if (data.user_type === "patient") {
        findPatientByUserId(data.id).then(id => user_id = id);
    } else if (data.user_type === "doctor") {
        findDoctorByUserId(data.id).then(id => user_id = id);
    }

    fetch(`http://127.0.0.1:8084/api/appointment/?patient_id=${user_id}`)
        .then(response => response.json())
        .then(data => {
            const appointmentsDiv = document.getElementById('appointments');
            data.forEach(appointment => {
                const appointmentDiv = document.createElement('div');
                appointmentDiv.classList.add('appointment');

                fetch(`http://127.0.0.1:8083/api/doctor/${appointment.doctor_id}/`)
                    .then(response => {
                        return response.json()
                    })
                    .then(data => {
                        fetch(`http://127.0.0.1:8081/api/user/user-info/${data.user_id}/`)
                            .then(response => {
                                return response.json()
                            })
                            .then(data => {
                                let doctor = data.fullname.last_name + " " + data.fullname.mid_name + " " + data.fullname.first_name;
                                appointmentDiv.innerHTML = `
                    <div class="date">Ngày: ${appointment.date}</div>
                    <div class="time">Giờ: ${appointment.start_time} - ${appointment.end_time}</div>
                    <div class="doctor">Bác sĩ: ${doctor}</div>
                    <div class="status">Trạng thái: ${appointment.status}</div>
                `;
                                appointmentsDiv.appendChild(appointmentDiv);
                            })
                    })
            });
        })
        .catch(error => console.error('Error fetching appointments:', error));
})
