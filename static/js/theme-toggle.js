function setTheme(mode) {
  const html = document.documentElement;
  if (mode === 'dark') {
    html.classList.add('dark');
    localStorage.setItem('theme', 'dark');
  } else {
    html.classList.remove('dark');
    localStorage.setItem('theme', 'light');
  }
}

function toggleTheme() {
  const current = localStorage.getItem('theme') || 'system';
  if (current === 'dark' || (current === 'system' && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
    setTheme('light');
  } else {
    setTheme('dark');
  }
}

function applyInitialTheme() {
  const saved = localStorage.getItem('theme');
  if (saved === 'dark') {
    document.documentElement.classList.add('dark');
  } else if (saved === 'light') {
    document.documentElement.classList.remove('dark');
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    document.documentElement.classList.add('dark');
  }
}

applyInitialTheme();

window.addEventListener('DOMContentLoaded', () => {
  const toggleBtn = document.querySelector('[data-theme-toggle]');
  if (toggleBtn) {
    toggleBtn.addEventListener('click', toggleTheme);
  }
});
