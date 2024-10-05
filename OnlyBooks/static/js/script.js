function searchBooks() {
    const searchInput = document.querySelector('.hero input').value;
    alert(`Searching for "${searchInput}"...`);
}

function toggleModal() {
    const modal = document.getElementById('loginModal');
    modal.style.display = modal.style.display === 'block' ? 'none' : 'block';
}

window.onclick = function(event) {
    const modal = document.getElementById('loginModal');
    if (event.target === modal) {
        modal.style.display = "none";
    }
};

function switchToSignup() {
    const loginForm = document.getElementById('loginForm');
    loginForm.innerHTML = `
        <h2>Sign Up</h2>
        <input type="text" placeholder="Email" required>
        <input type="password" placeholder="Password" required>
        <input type="password" placeholder="Confirm Password" required>
        <button type="submit">Sign Up</button>
    `;
    const label = document.getElementById('switch_login_form');
    label.innerHTML = `
    Do have an account? <a href="#" onclick="switchToLogin()">Login</a>
    `;
}
function switchToLogin() {
    const loginForm = document.getElementById('loginForm');
    loginForm.innerHTML = `
        <h2>Login</h2>
        <input type="text" placeholder="Email" required>
        <input type="password" placeholder="Password" required>
        <button type="submit">Login</button>
    `;
    const label = document.getElementById('switch_login_form');
    label.innerHTML = `
    Don't have an account? <a href="#" onclick="switchToSignup()">Sign Up</a>
    `;
}