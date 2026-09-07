login.jss: function login() {

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username === "admin" && password === "1234") {

        window.location.href = "index.html";

    } else {

        document.getElementById("message").textContent =
            "Invalid username or password";

    }
}
