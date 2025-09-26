import json
import pathlib
import streamlit as st
import streamlit.components.v1 as components

# Load external data
DATA_PATH = pathlib.Path(__file__).parent / "data.json"
GAME_DATA = json.loads(DATA_PATH.read_text(encoding="utf-8"))

st.set_page_config(page_title="English Listening Helper", layout="wide")

# Inject JSON once, then reference in JS as window.GAME_DATA
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>English Listening Helper</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <style>
    body {{ font-family: 'Inter', sans-serif; }}
    .tab-active {{ border-color:#4f46e5; color:#4f46e5; background-color:#eef2ff; }}
    .card {{ min-height:20rem; display:flex; flex-direction:column; justify-content:center; align-items:center; }}
    .btn-choice {{ transition:all .2s; }}
    .btn-choice:hover {{ transform:translateY(-2px); box-shadow:0 4px 6px -1px rgb(0 0 0 / .1), 0 2px 4px -2px rgb(0 0 0 / .1); }}
    .correct {{ background-color:#10b981 !important; color:white !important; border-color:#059669 !important; }}
    .incorrect {{ background-color:#ef4444 !important; color:white !important; border-color:#dc2626 !important; }}
  </style>
</head>
<body class="bg-gray-100 text-gray-800 flex items-center justify-center min-h-screen p-4">
  <!-- Inline JSON payload -->
  <script>
    window.GAME_DATA = {json.dumps(GAME_DATA, ensure_ascii=False)};
  </script>

  <div class="w-full max-w-2xl mx-auto bg-white rounded-2xl shadow-lg p-6 md:p-8">
    <header class="text-center mb-6">
      <h1 class="text-3xl font-bold text-gray-900">English Listening Helper</h1>
      <p class="text-gray-500 mt-1">Practice your vocabulary and listening skills.</p>
    </header>

    <!-- Tabs -->
    <div class="border-b border-gray-200 mb-6">
      <nav class="-mb-px flex space-x-4" aria-label="Tabs">
        <button id="tab-flashcards" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">Flashcards</button>
        <button id="tab-antonym" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">Antonym Game</button>
        <button id="tab-pronunciation" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">Pronunciation Game</button>
        <button id="tab-minimalpairs" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">Which one are you hearing?</button>
      </nav>
    </div>

    <main>
      <!-- Flashcards -->
      <div id="view-flashcards" class="space-y-6">
        <div>
          <label for="correct-list" class="block text-sm font-medium text-gray-700">Customize correct List (comma-separated)</label>
          <textarea id="correct-list" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="e.g., apple, beautiful, challenge, ..."></textarea>
          <button id="save-list-btn" class="mt-2 w-full inline-flex justify-center items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Save and Use This List</button>
        </div>
        <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner">
          <div id="flashcard-container" class="card">
            <p id="flashcard-instruction" class="text-gray-500 mb-4">Click the speaker to hear the correct.</p>
            <button id="play-audio-btn" class="w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
            </button>
            <div id="correct-reveal" class="mt-4 h-10">
              <h2 id="correct-text" class="text-4xl font-bold text-gray-800 invisible"></h2>
            </div>
          </div>
          <button id="reveal-correct-btn" class="mt-4 inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">Reveal correct</button>
        </div>
        <div class="flex justify-between items-center">
          <button id="prev-correct-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg></button>
          <span id="correct-counter" class="text-sm font-medium text-gray-600">1 / 10</span>
          <button id="next-correct-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300"><svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></button>
        </div>
      </div>

      <!-- Antonym -->
      <div id="view-antonym" class="hidden space-y-6">
        <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Exclude the Antonym</h3>
          <p class="text-gray-500 mb-6">Three corrects are synonyms. Click the one that is the antonym.</p>
          <div id="antonym-choices" class="grid grid-cols-2 gap-4 w-full max-w-md"></div>
        </div>
        <div id="antonym-feedback" class="h-6 text-center font-medium"></div>
      </div>

      <!-- Pronunciation -->
      <div id="view-pronunciation" class="hidden space-y-6">
        <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Choose the Correct correct</h3>
          <p class="text-gray-500 mb-6">Listen to the audio and click the matching correct.</p>
          <button id="play-pronunciation-audio-btn" class="mb-6 w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
          </button>
          <div id="pronunciation-choices" class="grid grid-cols-2 gap-4 w-full max-w-md"></div>
        </div>
        <div id="pronunciation-feedback" class="h-6 text-center font-medium"></div>
      </div>

      <!-- Minimal Pairs -->
      <div id="view-minimalpairs" class="hidden space-y-6">
        <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
          <h3 class="text-xl font-semibold text-gray-800 mb-2">Which one are you hearing?</h3>
          <p class="text-gray-500 mb-6">Click the speaker, then choose the word you heard.</p>
          <button id="play-minimalpairs-audio-btn" class="mb-6 w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
          </button>
          <div id="minimalpairs-choices" class="grid grid-cols-2 gap-4 w-full max-w-md"></div>
        </div>
        <div id="minimalpairs-feedback" class="h-6 text-center font-medium"></div>
      </div>
    </main>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', () => {
      // --- STATE ---
      let currentMode = 'flashcards';
      let currentcorrectIndex = 0;
      const synth = window.speechSynthesis;

      // Read data from external JSON (already injected)
      const DATA = window.GAME_DATA || {{}};
      let correctList = (DATA.flashcards && DATA.flashcards.length) ? DATA.flashcards : ['eloquent','gregarious','resilience'];
      const antonymData = DATA.antonym || [];
      const pronunciationData = DATA.pronunciation || [];
      const minimalPairsData = DATA.minimalPairs || [];

      // --- DOM MAPS ---
      const views = {{
        flashcards: document.getElementById('view-flashcards'),
        antonym: document.getElementById('view-antonym'),
        pronunciation: document.getElementById('view-pronunciation'),
        minimalpairs: document.getElementById('view-minimalpairs'),
      }};
      const tabs = {{
        flashcards: document.getElementById('tab-flashcards'),
        antonym: document.getElementById('tab-antonym'),
        pronunciation: document.getElementById('tab-pronunciation'),
        minimalpairs: document.getElementById('tab-minimalpairs'),
      }};

      // Flashcards
      const correctListInput = document.getElementById('correct-list');
      const saveListBtn = document.getElementById('save-list-btn');
      const playAudioBtn = document.getElementById('play-audio-btn');
      const revealcorrectBtn = document.getElementById('reveal-correct-btn');
      const correctText = document.getElementById('correct-text');
      const prevcorrectBtn = document.getElementById('prev-correct-btn');
      const nextcorrectBtn = document.getElementById('next-correct-btn');
      const correctCounter = document.getElementById('correct-counter');
      const flashcardInstruction = document.getElementById('flashcard-instruction');

      // Antonym
      const antonymChoicesContainer = document.getElementById('antonym-choices');
      const antonymFeedback = document.getElementById('antonym-feedback');
      let currentAntonymQuestion = {{}};

      // Pronunciation
      const playPronunciationAudioBtn = document.getElementById('play-pronunciation-audio-btn');
      const pronunciationChoicesContainer = document.getElementById('pronunciation-choices');
      const pronunciationFeedback = document.getElementById('pronunciation-feedback');
      let currentPronunciationQuestion = {{}};

      // Minimal pairs
      const playMinimalPairsAudioBtn = document.getElementById('play-minimalpairs-audio-btn');
      const minimalPairsChoicesContainer = document.getElementById('minimalpairs-choices');
      const minimalPairsFeedback = document.getElementById('minimalpairs-feedback');
      let currentMinimalPairsQuestion = {{}};

      // --- UTILS ---
      const speak = (text) => {{
        if (synth.speaking) synth.cancel();
        const u = new SpeechSynthesisUtterance(text);
        u.lang = 'en-US';
        u.rate = 0.9;
        synth.speak(u);
      }};
      const shuffleArray = (arr) => {{
        for (let i = arr.length - 1; i > 0; i--) {{
          const j = Math.floor(Math.random() * (i + 1));
          [arr[i], arr[j]] = [arr[j], arr[i]];
        }}
        return arr;
      }};
      const switchMode = (mode) => {{
        currentMode = mode;
        Object.values(views).forEach(v => v.classList.add('hidden'));
        Object.values(tabs).forEach(t => t.classList.remove('tab-active'));
        views[mode].classList.remove('hidden');
        tabs[mode].classList.add('tab-active');
        if (mode === 'antonym') setupAntonymGame();
        if (mode === 'pronunciation') setupPronunciationGame();
        if (mode === 'minimalpairs') setupMinimalPairsGame();
      }};

      // --- FLASHCARDS ---
      const updateFlashcardView = () => {{
        flashcardInstruction.classList.remove('hidden');
        correctText.textContent = correctList[currentcorrectIndex] || '';
        correctText.classList.add('invisible');
        correctCounter.textContent = `${{currentcorrectIndex + 1}} / ${{correctList.length}}`;
      }};
      const savecorrectList = () => {{
        const corrects = correctListInput.value.split(',').map(s => s.trim()).filter(Boolean);
        if (corrects.length) {{
          correctList = corrects;
          currentcorrectIndex = 0;
          updateFlashcardView();
        }}
      }};

      // --- ANTONYM ---
      const setupAntonymGame = () => {{
        if (!antonymData.length) {{
          antonymChoicesContainer.innerHTML = '<p class="text-gray-500">No antonym data.</p>';
          return;
        }}
        antonymFeedback.textContent = '';
        currentAntonymQuestion = antonymData[Math.floor(Math.random()*antonymData.length)];
        const choices = shuffleArray([...(currentAntonymQuestion.s||[]), currentAntonymQuestion.a]);
        antonymChoicesContainer.innerHTML = '';
        choices.forEach(choice => {{
          const b = document.createElement('button');
          b.textContent = choice;
          b.className = 'btn-choice w-full px-4 py-3 border border-gray-300 rounded-lg text-lg font-medium bg-white text-gray-700 hover:bg-gray-50';
          b.onclick = () => checkAntonymAnswer(choice);
          antonymChoicesContainer.appendChild(b);
        }});
      }};
      const checkAntonymAnswer = (sel) => {{
        const btns = antonymChoicesContainer.querySelectorAll('button');
        btns.forEach(b => {{
          b.disabled = true;
          if (b.textContent === currentAntonymQuestion.a) b.classList.add('correct');
          else if (b.textContent === sel) b.classList.add('incorrect');
        }});
        if (sel === currentAntonymQuestion.a) {{
          antonymFeedback.textContent = 'Correct!';
          antonymFeedback.className = 'h-6 text-center font-medium text-green-600';
        }} else {{
          antonymFeedback.textContent = 'Not quite. Try the next one!';
          antonymFeedback.className = 'h-6 text-center font-medium text-red-600';
        }}
        setTimeout(setupAntonymGame, 2000);
      }};

      // --- PRONUNCIATION ---
      const setupPronunciationGame = () => {{
        if (!pronunciationData.length) {{
          pronunciationChoicesContainer.innerHTML = '<p class="text-gray-500">No pronunciation data.</p>';
          return;
        }}
        pronunciationFeedback.textContent = '';
        currentPronunciationQuestion = pronunciationData[Math.floor(Math.random()*pronunciationData.length)];
        const choices = shuffleArray([currentPronunciationQuestion.correct, ...(currentPronunciationQuestion.distractors||[])]);
        pronunciationChoicesContainer.innerHTML = '';
        choices.forEach(choice => {{
          const b = document.createElement('button');
          b.textContent = choice;
          b.className = 'btn-choice w-full px-4 py-3 border border-gray-300 rounded-lg text-lg font-medium bg-white text-gray-700 hover:bg-gray-50';
          b.onclick = () => checkPronunciationAnswer(choice);
          pronunciationChoicesContainer.appendChild(b);
        }});
      }};
      const checkPronunciationAnswer = (sel) => {{
        const btns = pronunciationChoicesContainer.querySelectorAll('button');
        btns.forEach(b => {{
          b.disabled = true;
          if (b.textContent === currentPronunciationQuestion.correct) b.classList.add('correct');
          else if (b.textContent === sel) b.classList.add('incorrect');
        }});
        if (sel === currentPronunciationQuestion.correct) {{
          pronunciationFeedback.textContent = 'Correct!';
          pronunciationFeedback.className = 'h-6 text-center font-medium text-green-600';
        }} else {{
          pronunciationFeedback.textContent = 'Not quite. Try the next one!';
          pronunciationFeedback.className = 'h-6 text-center font-medium text-red-600';
        }}
        setTimeout(setupPronunciationGame, 2000);
      }};

      // --- MINIMAL PAIRS ---
      const setupMinimalPairsGame = () => {{
        if (!minimalPairsData.length) {{
          minimalPairsChoicesContainer.innerHTML = '<p class="text-gray-500">No minimal-pairs data.</p>';
          return;
        }}
        minimalPairsFeedback.textContent = '';
        const q = minimalPairsData[Math.floor(Math.random()*minimalPairsData.length)];
        const target = Math.random() < 0.5 ? q.correct : q.distractor;
        currentMinimalPairsQuestion = {{ ...q, target }};
        const choices = shuffleArray([q.correct, q.distractor]);
        minimalPairsChoicesContainer.innerHTML = '';
        choices.forEach(choice => {{
          const b = document.createElement('button');
          b.textContent = choice;
          b.className = 'btn-choice w-full px-4 py-3 border border-gray-300 rounded-lg text-lg font-medium bg-white text-gray-700 hover:bg-gray-50';
          b.onclick = () => checkMinimalPairsAnswer(choice);
          minimalPairsChoicesContainer.appendChild(b);
        }});
      }};
      const checkMinimalPairsAnswer = (sel) => {{
        const btns = minimalPairsChoicesContainer.querySelectorAll('button');
        btns.forEach(b => {{
          b.disabled = true;
          if (b.textContent === currentMinimalPairsQuestion.target) b.classList.add('correct');
          else if (b.textContent === sel) b.classList.add('incorrect');
        }});
        if (sel === currentMinimalPairsQuestion.target) {{
          minimalPairsFeedback.textContent = 'Correct!';
          minimalPairsFeedback.className = 'h-6 text-center font-medium text-green-600';
        }} else {{
          minimalPairsFeedback.textContent = 'Not quite. Try the next one!';
          minimalPairsFeedback.className = 'h-6 text-center font-medium text-red-600';
        }}
        setTimeout(setupMinimalPairsGame, 2000);
      }};

      // --- EVENTS ---
      Object.keys(tabs).forEach(k => tabs[k].addEventListener('click', () => switchMode(k)));
      playAudioBtn.addEventListener('click', () => speak(correctList[currentcorrectIndex]));
      document.getElementById('next-correct-btn').addEventListener('click', () => {{ currentcorrectIndex = (currentcorrectIndex + 1) % correctList.length; updateFlashcardView(); }});
      document.getElementById('prev-correct-btn').addEventListener('click', () => {{ currentcorrectIndex = (currentcorrectIndex - 1 + correctList.length) % correctList.length; updateFlashcardView(); }});
      revealcorrectBtn.addEventListener('click', () => {{ flashcardInstruction.classList.add('hidden'); correctText.classList.remove('invisible'); }});
      saveListBtn.addEventListener('click', () => {{
        correctList = correctListInput.value.split(',').map(s=>s.trim()).filter(Boolean);
        currentcorrectIndex = 0; updateFlashcardView();
      }});
      playPronunciationAudioBtn.addEventListener('click', () => speak((currentPronunciationQuestion||{{}}).correct || ''));
      playMinimalPairsAudioBtn.addEventListener('click', () => speak((currentMinimalPairsQuestion||{{}}).target || ''));

      // Init
      document.getElementById('correct-list').value = correctList.join(', ');
      (() => switchMode('flashcards'))();
      updateFlashcardView();
    });
  </script>
</body>
</html>
"""

components.html(html_content, height=800, scrolling=True)
