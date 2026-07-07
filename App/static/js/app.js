const API = '/api';

function getToken() {
  return localStorage.getItem('edupath_token');
}

function setToken(token) {
  localStorage.setItem('edupath_token', token);
}

function clearToken() {
  localStorage.removeItem('edupath_token');
}

function getUser() {
  const raw = localStorage.getItem('edupath_user');
  return raw ? JSON.parse(raw) : null;
}

function setUser(user) {
  localStorage.setItem('edupath_user', JSON.stringify(user));
}

function clearUser() {
  localStorage.removeItem('edupath_user');
}

async function api(path, options = {}) {
  const headers = { 'Content-Type': 'application/json', ...options.headers };
  const token = getToken();
  if (token) headers['Authorization'] = `Bearer ${token}`;

  const res = await fetch(`${API}${path}`, { ...options, headers });
  const data = await res.json().catch(() => null);

  if (!res.ok) {
    throw new Error(data?.detail || 'خطایی رخ داد');
  }
  return data;
}

function requireAuth() {
  if (!getToken()) {
    window.location.href = '/?login=1';
    return false;
  }
  return true;
}

function updateNavbar() {
  const user = getUser();
  const authBtns = document.getElementById('auth-btns');
  const userMenu = document.getElementById('user-menu');
  if (!authBtns || !userMenu) return;

  if (user) {
    authBtns.style.display = 'none';
    userMenu.style.display = 'flex';
    const nameEl = document.getElementById('nav-username');
    if (nameEl) nameEl.textContent = user.username;
  } else {
    authBtns.style.display = 'flex';
    userMenu.style.display = 'none';
  }
}

function initAuthModal() {
  const overlay = document.getElementById('auth-modal');
  if (!overlay) return;

  const loginTab = overlay.querySelector('[data-tab="login"]');
  const registerTab = overlay.querySelector('[data-tab="register"]');
  const loginForm = document.getElementById('login-form');
  const registerForm = document.getElementById('register-form');
  const errorEl = document.getElementById('auth-error');

  document.getElementById('open-login')?.addEventListener('click', () => {
    overlay.classList.add('active');
    switchTab('login');
  });

  document.getElementById('open-register')?.addEventListener('click', () => {
    overlay.classList.add('active');
    switchTab('register');
  });

  overlay.addEventListener('click', (e) => {
    if (e.target === overlay) overlay.classList.remove('active');
  });

  function switchTab(tab) {
    loginTab.classList.toggle('active', tab === 'login');
    registerTab.classList.toggle('active', tab === 'register');
    loginForm.classList.toggle('active', tab === 'login');
    registerForm.classList.toggle('active', tab === 'register');
    errorEl.textContent = '';
  }

  loginTab?.addEventListener('click', () => switchTab('login'));
  registerTab?.addEventListener('click', () => switchTab('register'));

  loginForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorEl.textContent = '';
    try {
      const data = await api('/auth/login', {
        method: 'POST',
        body: JSON.stringify({
          username: document.getElementById('login-user').value,
          password: document.getElementById('login-pass').value,
        }),
      });
      setToken(data.token);
      setUser(data.user);
      overlay.classList.remove('active');
      updateNavbar();
      const redirect = new URLSearchParams(location.search).get('redirect');
      if (redirect) window.location.href = redirect;
    } catch (err) {
      errorEl.textContent = err.message;
    }
  });

  registerForm?.addEventListener('submit', async (e) => {
    e.preventDefault();
    errorEl.textContent = '';
    try {
      const data = await api('/auth/register', {
        method: 'POST',
        body: JSON.stringify({
          username: document.getElementById('reg-user').value,
          email: document.getElementById('reg-email').value,
          password: document.getElementById('reg-pass').value,
          grade: document.getElementById('reg-grade').value,
        }),
      });
      setToken(data.token);
      setUser(data.user);
      overlay.classList.remove('active');
      updateNavbar();
      const redirect = new URLSearchParams(location.search).get('redirect');
      if (redirect) window.location.href = redirect;
    } catch (err) {
      errorEl.textContent = err.message;
    }
  });

  if (new URLSearchParams(location.search).get('login') === '1') {
    overlay.classList.add('active');
  }
}

document.getElementById('logout-btn')?.addEventListener('click', () => {
  clearToken();
  clearUser();
  window.location.href = '/';
});

document.addEventListener('DOMContentLoaded', () => {
  updateNavbar();
  initAuthModal();
});
