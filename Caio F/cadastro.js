const init = () => {
    const inputUsername = document.getElementById('input_cadastro_nome');
    const inputEmail = document.querySelector('input[type="email"]');
    const inputPassword = document.getElementById('input_cadastro_password');
    const inputConfirmaPassword = document.getElementById('input_cadastro_confirmapassword');
    const submitButton = document.getElementById('button__signup');

    if(submitButton) {
        submitButton.addEventListener('click', (event) => {
            event.preventDefault();

            fetch('https://reqres.in/api/login', {
                method: 'POST',
                header: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    email: inputEmail.value,
                    password: inputPassword.value,
                })
            }).then((response) => {
                return response.json();
            }).then((data) => {
                console.log(data);
            })
        })
    }
}

window.onload = init;