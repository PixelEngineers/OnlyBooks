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
    const csrf = loginForm.children[0];
    loginForm.innerHTML = ``
    loginForm.appendChild(csrf)
    loginForm.innerHTML += `
        <h2>Sign Up</h2>
        <input type="text" name="username" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <input type="password" name="confirm_password" placeholder="Confirm Password" required>
        <button type="submit">Sign Up</button>
    `;
    const label = document.getElementById('switch_login_form');
    label.innerHTML = `
    Already have an account? <a href="#" onclick="switchToLogin()">Login</a>
    `;
}

function switchToLogin() {
    const loginForm = document.getElementById('loginForm');
    const csrf = loginForm.children[0];
    loginForm.innerHTML = ``
    loginForm.appendChild(csrf)
    loginForm.innerHTML += `
        <h2>Login</h2>
        <input type="text" name="username" placeholder="Email" required>
        <input type="password" name="password" placeholder="Password" required>
        <button type="submit">Login</button>
    `;
    const label = document.getElementById('switch_login_form');
    label.innerHTML = `
    Don't have an account? <a href="#" onclick="switchToSignup()">Sign Up</a>
    `;
}

// Example function to get CSRF token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function searchBooks() {
    const searchInput = document.querySelector('.hero input').value;
    alert(`Searching for "${searchInput}"...`);
}
