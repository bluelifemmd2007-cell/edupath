async function loadDashboard() {
  if (!requireAuth()) return;

  const user = getUser();
  if (user) {
    document.getElementById('welcome-name').textContent = user.username;
    document.getElementById('stat-grade').textContent = user.grade || '—';
  }

  try {
    const latest = await api('/assessments/latest');
    const container = document.getElementById('latest-results');

    if (!latest) {
      document.getElementById('stat-count').textContent = '۰';
      document.getElementById('stat-top').textContent = '—';
      container.innerHTML =
        '<div class="empty-state"><p>هنوز تستی انجام نداده‌اید. اولین تست خود را شروع کنید!</p><a href="/assessment" class="btn btn-primary">شروع تست</a></div>';
      return;
    }

    document.getElementById('stat-count').textContent = '۱+';
    document.getElementById('stat-top').textContent = latest.results[0]?.title || '—';

    container.innerHTML = latest.results.slice(0, 5).map((item, i) => `
      <div class="result-item" style="margin-bottom:0.75rem;">
        <div class="result-rank">${i + 1}</div>
        <div class="result-info">
          <h3 style="font-size:1rem;">${item.title}</h3>
          <p style="font-size:0.85rem;">${item.description}</p>
        </div>
        <div class="match-percent">${item.match_percent}٪</div>
      </div>
    `).join('');

    container.innerHTML += `<div style="text-align:center;margin-top:1rem;"><a href="/results?id=${latest.id}" class="btn btn-outline btn-sm">مشاهده کامل نتایج</a></div>`;
  } catch (err) {
    document.getElementById('latest-results').innerHTML =
      `<div class="empty-state"><p>${err.message}</p></div>`;
  }
}

document.addEventListener('DOMContentLoaded', loadDashboard);
