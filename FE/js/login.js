document.addEventListener('DOMContentLoaded', function () {
    const loginForm = document.getElementById('login-form')
    loginForm.addEventListener("submit", async function (e) {
        e.preventDefault();
        const loginId = document.getElementById('username').value
        const password = document.getElementById('password').value
        await fetch('http://127.0.0.1:8081/api/user/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'login_id': loginId,
                'password': password
            })
        })
            .then(response => {
                return response.json()
            })
            .then(data => {
                if (data.error) {
                    alert(data.error)
                } else {
                    sessionStorage.setItem('token', data.token)
                    window.location.href = "bookSchedule.html"
                }
            })
    })
})