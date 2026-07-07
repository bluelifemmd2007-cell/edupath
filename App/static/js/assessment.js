let questions = [];
let currentIndex = 0;
let answers = {};

async function initAssessment() {
  if (!getToken()) {
    document.getElementById('auth-modal').classList.add('active');
    const params = new URLSearchParams(location.search);
    if (!params.has('redirect')) {
      history.replaceState(null, '', '?redirect=/assessment');
    }
    return;
  }

  try {
    questions = await api('/assessments/questions');
    renderQuestion();
  } catch (err) {
    alert(err.message);
  }
}

function renderQuestion() {
  const q = questions[currentIndex];
  const total = questions.length;

  document.getElementById('question-number').textContent = `سوال ${currentIndex + 1} از ${total}`;
  document.getElementById('question-text').textContent = q.text;
  document.getElementById('progress-fill').style.width = `${((currentIndex + 1) / total) * 100}%`;

  const container = document.getElementById('scale-buttons');
  container.innerHTML = '';

  for (let i = 1; i <= 10; i++) {
    const btn = document.createElement('button');
    btn.className = 'scale-btn';
    btn.textContent = i;
    if (answers[q.id] === i) btn.classList.add('selected');
    btn.addEventListener('click', () => {
      answers[q.id] = i;
      container.querySelectorAll('.scale-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
    });
    container.appendChild(btn);
  }

  document.getElementById('prev-btn').disabled = currentIndex === 0;
  document.getElementById('next-btn').textContent = currentIndex === total - 1 ? 'مشاهده نتایج' : 'بعدی';
}

document.getElementById('prev-btn').addEventListener('click', () => {
  if (currentIndex > 0) {
    currentIndex--;
    renderQuestion();
  }
});

document.getElementById('next-btn').addEventListener('click', async () => {
  const q = questions[currentIndex];
  if (!answers[q.id]) {
    alert('لطفاً یک گزینه انتخاب کنید');
    return;
  }

  if (currentIndex < questions.length - 1) {
    currentIndex++;
    renderQuestion();
    return;
  }

  try {
    const payload = {
      answers: Object.entries(answers).map(([question_id, value]) => ({ question_id, value })),
    };
    const result = await api('/assessments/submit', {
      method: 'POST',
      body: JSON.stringify(payload),
    });
    localStorage.setItem('edupath_last_result', JSON.stringify(result));
    window.location.href = `/results?id=${result.id}`;
  } catch (err) {
    alert(err.message);
  }
});

document.addEventListener('DOMContentLoaded', initAssessment);
