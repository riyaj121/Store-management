const checkValidInput = (input, type_of_input) => {

    let valid = false;

    // if the user input is a name, chcek if it has the string '<script> in it
    if (type_of_input === 'name') {

        if (input.value.includes('<script>')) {
            //input.value = NULL;
            input.setCustomValidity(" Invalid name format ");
        } else {
            input.setCustomValidity("");
            valid = true;
        }
    }

    // if the user input is an email, check if it is of format xyz@xx.com
    if (type_of_input === 'email') {

        if (input.validity.typeMismatch) {
            input.setCustomValidity(" Invalid mail format");
        } else {
            input.setCustomValidity("");
            valid = true;
        }
    }

    if (!valid) { input.reportValidity(); } else { return true; }

}

function checkName() {

    // take the value of user  when filling out a form and check if its valid
    var fname = document.getElementById('fname');
    var lname = document.getElementById('lname');
    var email = document.getElementById('mail');
    var pass = document.getElementById('passsword');

    let validFname = checkValidInput(fname, 'name')
    let validLname = checkValidInput(lname, 'name');
    let validEmail = checkValidInput(email, 'email');

    if (validFname && validLname && validEmail) {


        const data = {
            'u_fname': fname.value,
            'u_lname': lname.value,
            'u_email': mail.value,
            'u_pass': password.value
        };

        fetch('addUser.py', {
                method: 'POST', // or 'PUT'
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            })
            .then(response => response.json())
            .then(data => {
                console.log('Success:', data);
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }


}

document.getElementById('signupConfirm_bttn').addEventListener("click", checkName());