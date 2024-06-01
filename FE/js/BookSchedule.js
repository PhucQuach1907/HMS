document.addEventListener('DOMContentLoaded', async function () {
    const doctorSelect = document.getElementById('doctor_id');
    const dateInput = document.getElementById('date');
    const timeRangeSelect = document.getElementById('time_range');
    const scheduleForm = document.getElementById('schedule-form');
    let patient_id;

    data = await authorizationUser();
    findPatientByUserId(data.id).then(id => patient_id = id);

    fetch('http://127.0.0.1:8083/api/doctor/')
        .then(response => response.json())
        .then(data => {
            data.forEach(doctor => {
                const option = document.createElement('option');
                option.value = doctor.id;
                fetch(`http://127.0.0.1:8081/api/user/user-info/${doctor.user_id}`)
                    .then(response => response.json())
                    .then(data => {
                        option.textContent = `${data.fullname.first_name} ${data.fullname.mid_name} ${data.fullname.last_name}`;
                        doctorSelect.appendChild(option);
                    });
            });
        });

    doctorSelect.addEventListener('change', updateDisabledTimeSlots);
    dateInput.addEventListener('change', updateDisabledTimeSlots);

    function updateDisabledTimeSlots() {
        const doctorId = doctorSelect.value;
        const date = dateInput.value;

        if (doctorId && date) {
            fetch(`http://127.0.0.1:8084/api/appointment?doctor_id=${doctorId}&date=${date}`)
                .then(response => {
                    if (response.ok) {
                        return response.json();
                    }
                    throw new Error('Network response was not ok.');
                })
                .then(data => {
                    const occupiedTimeRanges = data
                        .filter(appointment => appointment.date === date)
                        .map(appointment => {
                            const startTime = appointment.start_time.slice(0, 5);
                            const endTime = appointment.end_time.slice(0, 5);
                            return `${startTime}-${endTime}`;
                        });
                    console.log(occupiedTimeRanges)
                    for (const option of timeRangeSelect.options) {
                        if (occupiedTimeRanges.includes(option.value)) {
                            option.disabled = true;
                        } else {
                            option.disabled = false;
                        }
                    }
                })
                .catch(error => console.error('Error fetching appointments:', error));
        } else {
            for (const option of timeRangeSelect.options) {
                option.disabled = false;
            }
        }
    }

    scheduleForm.addEventListener('submit', async function (e) {
        e.preventDefault();

        const doctorId = doctorSelect.value;
        const date = dateInput.value;
        const timeRange = timeRangeSelect.value;
        const [startTime, endTime] = timeRange.split('-');

        const appointmentData = {
            patient_id: patient_id,
            doctor_id: parseInt(doctorId, 10),
            date: date,
            start_time: startTime,
            end_time: endTime,
            status: "scheduled"
        };

        await fetch('http://127.0.0.1:8084/api/appointment/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(appointmentData)
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    alert(data.error);
                } else {
                    alert('Đặt lịch thành công!');
                    window.location.href = "detailSchedule.html";
                }
            })
            .catch(error => console.error('Error creating appointment:', error));
    });
});
