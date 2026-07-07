function renderResults(data) {
  const list = document.getElementById('results-list');
  list.innerHTML = '';

  const date = new Date(data.created_at);
  document.getElementById('results-date').textContent =
    `تاریخ: ${date.toLocaleDateString('fa-IR')}`;

  data.results.forEach((item, i) => {
    const el = document.createElement('div');
    el.className = 'card result-item';
    el.innerHTML = `
      <div class="result-rank">${i + 1}</div>
      <div class="result-info">
        <h3>${item.title}</h3>
        <p>${item.description}</p>
      </div>
      <div class="match-bar"><div class="match-fill" style="width:${item.match_percent}%"></div></div>
      <div class="match-percent">${item.match_percent}٪</div>
    `;
    list.appendChild(el);
  });
}

async function loadResults() {
  if (!requireAuth()) return;

  const params = new URLSearchParams(location.search);
  const id = params.get('id');

  try {
    let data;
    if (id) {
      data = await api(`/assessments/${id}`);
    } else {
      const cached = localStorage.getItem('edupath_last_result');
      if (cached) {
        data = JSON.parse(cached);
      } else {
        data = await api('/assessments/latest');
      }
    }

    if (!data) {
      document.getElementById('results-list').innerHTML =
        '<div class="empty-state"><p>هنوز تستی انجام نداده‌اید.</p><a href="/assessment" class="btn btn-primary">شروع تست</a></div>';
      return;
    }

    renderResults(data);
  } catch (err) {
    document.getElementById('results-list').innerHTML =
      `<div class="empty-state"><p>${err.message}</p></div>`;
  }
}

document.addEventListener('DOMContentLoaded', loadResults);
