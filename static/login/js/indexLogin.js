document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Obtener los valores del formulario
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    
    // Validación simple (puedes cambiarla según tus necesidades)
    if (username === "usuario" && password === "contraseña") {
        alert("Bienvenido, " + username + "!");
        // Redirigir a otra página o realizar alguna acción
        // window.location.href = "dashboard.html";
    } else {
        document.getElementById("error-message").innerText = "Usuario o contraseña incorrectos.";
    }
});
