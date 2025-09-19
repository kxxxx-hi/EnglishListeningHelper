import streamlit as st
import streamlit.components.v1 as components

# English Listening Helper HTML content.
# This content is loaded and displayed directly by Streamlit.
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>English Listening Helper</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .tab-active {
            border-color: #4f46e5;
            color: #4f46e5;
            background-color: #eef2ff;
        }
        .card {
            min-height: 20rem; /* 320px */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        .btn-choice {
            transition: all 0.2s ease-in-out;
        }
        .btn-choice:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1);
        }
        .correct {
            background-color: #10b981 !important;
            color: white !important;
            border-color: #059669 !important;
        }
        .incorrect {
            background-color: #ef4444 !important;
            color: white !important;
            border-color: #dc2626 !important;
        }
    </style>
</head>
<body class="bg-gray-100 text-gray-800 flex items-center justify-center min-h-screen p-4">

    <div class="w-full max-w-2xl mx-auto bg-white rounded-2xl shadow-lg p-6 md:p-8">
        <header class="text-center mb-6">
            <h1 class="text-3xl font-bold text-gray-900">English Listening Helper</h1>
            <p class="text-gray-500 mt-1">Practice your vocabulary and listening skills.</p>
        </header>

        <!-- Navigation Tabs -->
        <div class="border-b border-gray-200 mb-6">
            <nav class="-mb-px flex space-x-4" aria-label="Tabs">
                <button id="tab-flashcards" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">
                    Flashcards
                </button>
                <button id="tab-antonym" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">
                    Antonym Game
                </button>
                <button id="tab-pronunciation" class="whitespace-nowrap py-3 px-1 border-b-2 font-medium text-sm text-gray-500 hover:text-gray-700 hover:border-gray-300">
                    Pronunciation Game
                </button>
            </nav>
        </div>

        <main>
            <!-- Flashcards Mode -->
            <div id="view-flashcards" class="space-y-6">
                <div>
                    <label for="word-list" class="block text-sm font-medium text-gray-700">Customize Word List (comma-separated)</label>
                    <textarea id="word-list" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="e.g., apple, beautiful, challenge, ..."></textarea>
                    <button id="save-list-btn" class="mt-2 w-full inline-flex justify-center items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Save and Use This List
                    </button>
                </div>
                
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner">
                    <div id="flashcard-container" class="card">
                        <p id="flashcard-instruction" class="text-gray-500 mb-4">Click the speaker to hear the word.</p>
                        <button id="play-audio-btn" class="w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" /></svg>
                        </button>
                        <div id="word-reveal" class="mt-4 h-10">
                            <h2 id="word-text" class="text-4xl font-bold text-gray-800 invisible"></h2>
                        </div>
                    </div>
                     <button id="reveal-word-btn" class="mt-4 inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Reveal Word
                    </button>
                </div>

                <div class="flex justify-between items-center">
                    <button id="prev-word-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
                    </button>
                    <span id="word-counter" class="text-sm font-medium text-gray-600">1 / 10</span>
                    <button id="next-word-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                    </button>
                </div>
            </div>

            <!-- Antonym Game -->
            <div id="view-antonym" class="hidden space-y-6">
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Exclude the Antonym</h3>
                    <p class="text-gray-500 mb-6">Three words are synonyms. Click the one that is the antonym.</p>
                    <div id="antonym-choices" class="grid grid-cols-2 gap-4 w-full max-w-md">
                        <!-- Buttons will be generated here -->
                    </div>
                </div>
                 <div id="antonym-feedback" class="h-6 text-center font-medium"></div>
            </div>

            <!-- Pronunciation Game -->
            <div id="view-pronunciation" class="hidden space-y-6">
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Choose the Correct Word</h3>
                    <p class="text-gray-500 mb-6">Listen to the audio and click the matching word.</p>
                     <button id="play-pronunciation-audio-btn" class="mb-6 w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" /></svg>
                    </button>
                    <div id="pronunciation-choices" class="grid grid-cols-2 gap-4 w-full max-w-md">
                         <!-- Buttons will be generated here -->
                    </div>
                </div>
                <div id="pronunciation-feedback" class="h-6 text-center font-medium"></div>
            </div>
        </main>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            // --- STATE MANAGEMENT ---
            let currentMode = 'flashcards';
            let wordList = ['eloquent', 'gregarious', 'resilience', 'ubiquitous', 'ephemeral', 'serendipity', 'magnanimous', 'perspicacious', 'conundrum', 'juxtaposition'];
            let currentWordIndex = 0;
            const synth = window.speechSynthesis;

            // --- GAME DATA ---
            const antonymData = [
                // Vast (广阔的) - Cramped (狭窄的)
                { s: ['Vast', 'Huge', 'Spacious'], a: 'Cramped' },
                // Lush (茂盛的) - Barren (荒芜的)
                { s: ['Lush', 'Abundant', 'Verdant'], a: 'Barren' },
                // Serene (宁静的) - Turbulent (喧嚣的)
                { s: ['Serene', 'Peaceful', 'Calm'], a: 'Turbulent' },
                // Tranquil (安静的) - Noisy (吵闹的)
                { s: ['Tranquil', 'Quiet', 'Still'], a: 'Noisy' },
                // Pristine (原始的) - Polluted (受污染的)
                { s: ['Pristine', 'Spotless', 'Unspoiled'], a: 'Polluted' },
                // Refreshing (令人精神焕发的) - Stifling (沉闷的)
                { s: ['Refreshing', 'Invigorating', 'Crisp'], a: 'Stifling' },
                // Remote (偏远的) - Accessible (易到达的)
                { s: ['Remote', 'Distant', 'Isolated'], a: 'Accessible' },
                // Majestic (雄伟的) - Ordinary (普通的)
                { s: ['Majestic', 'Grand', 'Stately'], a: 'Ordinary' },
                // Vibrant (充满生机的) - Lifeless (毫无生气的)
                { s: ['Vibrant', 'Lively', 'Energetic'], a: 'Lifeless' },
                // Untouched (未被触及的) - Developed (被开发的)
                { s: ['Untouched', 'Virgin', 'Unspoiled'], a: 'Developed' },
                // Iconic (标志性的) - Unknown (不知名的)
                { s: ['Iconic', 'Legendary', 'Famous'], a: 'Unknown' },
                // Innovative (创新的) - Traditional (传统的)
                { s: ['Innovative', 'Pioneering', 'Creative'], a: 'Traditional' },
                // Permanent (永久的) - Temporary (临时的)
                { s: ['Permanent', 'Lasting', 'Enduring'], a: 'Temporary' },
                // Massive (巨大的) - Tiny (微小的)
                { s: ['Massive', 'Enormous', 'Colossal'], a: 'Tiny' },
                // Smooth (光滑的) - Rough (粗糙的)
                { s: ['Smooth', 'Polished', 'Sleek'], a: 'Rough' },
                // Magnificent (壮丽的) - Dull (沉闷的)
                { s: ['Magnificent', 'Splendid', 'Impressive'], a: 'Dull' },
                // Empty (空的) - Full (满的)
                { s: ['Empty', 'Vacant', 'Hollow'], a: 'Full' },
                // Vertical (垂直的) - Horizontal (水平的)
                { s: ['Vertical', 'Upright', 'Perpendicular'], a: 'Horizontal' },
                // Restored (修复的) - Ruined (毁坏的)
                { s: ['Restored', 'Repaired', 'Renovated'], a: 'Ruined' },
                // Grand (宏伟的) - Small (小的)
                { s: ['Grand', 'Majestic', 'Imposing'], a: 'Small' },
                // Modern (现代的) - Ancient (古老的)
                { s: ['Modern', 'Contemporary', 'Current'], a: 'Ancient' },
                // Intricate (错综复杂的) - Simple (简单的)
                { s: ['Intricate', 'Complex', 'Detailed'], a: 'Simple' },
                // Unique (独特的) - Common (常见的)
                { s: ['Unique', 'Distinctive', 'Special'], a: 'Common' },
                // Symmetrical (对称的) - Asymmetrical (不对称的)
                { s: ['Symmetrical', 'Balanced', 'Proportional'], a: 'Asymmetrical' },
                // Solid (坚固的) - Fragile (易碎的)
                { s: ['Solid', 'Sturdy', 'Durable'], a: 'Fragile' },
                // Historic (历史悠久的) - New (新的)
                { s: ['Historic', 'Ancient', 'Old'], a: 'New' },
                // Functional (实用的) - Decorative (装饰性的)
                { s: ['Functional', 'Practical', 'Utilitarian'], a: 'Decorative' },
                // Breathtaking (惊人的) - Unimpressive (不引人注目的)
                { s: ['Breathtaking', 'Stunning', 'Spectacular'], a: 'Unimpressive' },
                // Spacious (宽敞的) - Confined (受限的)
                { s: ['Spacious', 'Roomy', 'Expansive'], a: 'Confined' },
                // Secluded (隐蔽的) - Crowded (拥挤的)
                { s: ['Secluded', 'Isolated', 'Private'], a: 'Crowded' },
                // Harmonious (和谐的) - Disruptive (破坏性的)
                { s: ['Harmonious', 'Agreeable', 'Peaceful'], a: 'Disruptive' },
                // Winding (蜿蜒的) - Straight (笔直的)
                { s: ['Winding', 'Curvy', 'Meandering'], a: 'Straight' },
                // Cool (凉爽的) - Hot/Sweltering (酷热的)
                { s: ['Cool', 'Chilly', 'Crisp'], a: 'Hot' },
                // Dense (茂密的) - Sparse (稀疏的)
                { s: ['Dense', 'Thick', 'Packed'], a: 'Sparse' },
                // Calm (平静的) - Rough (崎岖的)
                { s: ['Calm', 'Serene', 'Tranquil'], a: 'Rough' },
                // Natural (自然的) - Artificial (人工的)
                { s: ['Natural', 'Genuine', 'Authentic'], a: 'Artificial' },
                // Noisy (嘈杂的) - Silent (寂静的)
                { s: ['Noisy', 'Loud', 'Clamorous'], a: 'Silent' },
                // Crowded (拥挤的) - Deserted (空旷的)
                { s: ['Crowded', 'Packed', 'Congested'], a: 'Deserted' },
                // Vibrant (充满活力的) - Quiet (安静的)
                { s: ['Vibrant', 'Lively', 'Bustling'], a: 'Quiet' },
                // Exciting (令人兴奋的) - Boring (无聊的)
                { s: ['Exciting', 'Thrilling', 'Stimulating'], a: 'Boring' },
                // Popular (受欢迎的) - Obscure (鲜为人知的)
                { s: ['Popular', 'Well-known', 'Widespread'], a: 'Obscure' },
                // Chaotic (混乱的) - Orderly (有秩序的)
                { s: ['Chaotic', 'Disorderly', 'Haphazard'], a: 'Orderly' },
                // Loud (大声的) - Hushed / quiet (低声的)
                { s: ['Loud', 'Deafening', 'Boisterous'], a: 'Hushed' },
                // Enormous (巨大的) - Small (小的)
                { s: ['Enormous', 'Immense', 'Gigantic'], a: 'Small' },
                // Visible (可见的) - Hidden (隐藏的)
                { s: ['Visible', 'Apparent', 'Obvious'], a: 'Hidden' },
                // Thrilling (惊心动魄的) - Calm (平静的)
                { s: ['Thrilling', 'Exciting', 'Exhilarating'], a: 'Calm' },
                // Temporary (临时的) - Permanent (永久的)
                { s: ['Temporary', 'Brief', 'Transient'], a: 'Permanent' },
                // Dirty (脏的) - Clean (干净的)
                { s: ['Dirty', 'Filthy', 'Soiled'], a: 'Clean' },
                // Public (公共的) - Private (私人的)
                { s: ['Public', 'Communal', 'Shared'], a: 'Private' },
                // Energetic (充满活力的) - Sluggish (低迷的)
                { s: ['Energetic', 'Active', 'Vigorous'], a: 'Sluggish' },
                // Organized (有组织的) - Disorganized (杂乱无章的)
                { s: ['Organized', 'Tidy', 'Systematic'], a: 'Disorganized' },
                // Central (中心的) - Peripheral (边缘的)
                { s: ['Central', 'Core', 'Main'], a: 'Peripheral' },
                // Accessible (可到达的) - Inaccessible (难以到达的)
                { s: ['Accessible', 'Available', 'Reachable'], a: 'Inaccessible' },
                // Lively (生动的) - Dull (沉闷的)
                { s: ['Lively', 'Spirited', 'Vivacious'], a: 'Dull' },
                // Modern (现代的) - Outdated (过时的)
                { s: ['Modern', 'Contemporary', 'New'], a: 'Outdated' },
                // Tense (紧张的) - Relaxed (放松的)
                { s: ['Tense', 'Stressed', 'Nervous'], a: 'Relaxed' },
            ];
            let currentAntonymQuestion = {};

            const pronunciationData = [
                { correct: 'counter', distractors: ['couter', 'kaunter', 'countor'] },
                { correct: 'video', distractors: ['viedo', 'vidio', 'vido'] },
                { correct: 'written work', distractors: ['writtin work', 'writen work', 'writin work'] },
                { correct: 'australia', distractors: ['austrailia', 'austarlia', 'auustralia'] },
                { correct: 'principal', distractors: ['principle', 'prencipal', 'prinsipal'] },
                { correct: 'retail', distractors: ['retaill', 'retial', 'reteil'] },
                { correct: 'fraud', distractors: ['froud', 'frawde', 'fraude'] },
                { correct: 'embezzlement', distractors: ['embezlement', 'embazzlement', 'embezzelment'] },
                { correct: 'corporate', distractors: ['corperate', 'corporat', 'corparet'] },
                { correct: 'campaign', distractors: ['campain', 'campainn', 'camppain'] },
                { correct: 'staff', distractors: ['staf', 'staaff', 'staffe'] },
                { correct: 'wholesale', distractors: ['wholesael', 'whollesale', 'wholsale'] },
                { correct: 'manufacturer', distractors: ['manufacterer', 'manufecturer', 'manufacturur'] },
                { correct: 'outlay', distractors: ['outley', 'outlie', 'outley'] },
                { correct: 'enterprise', distractors: ['enterprize', 'enterpries', 'enteprise'] },
                { correct: 'human resources', distractors: ['human resourses', 'humen resources', 'human resourcess'] },
                { correct: 'merger', distractors: ['merdger', 'mergur', 'murger'] },
                { correct: 'hierarchy', distractors: ['heirarchy', 'hierchy', 'heirachy'] },
                { correct: 'installment', distractors: ['instalment', 'instaalment', 'instollment'] },
                { correct: 'mortgage', distractors: ['morgage', 'mortage', 'mortagge'] },
                { correct: 'clerk', distractors: ['clark', 'clerke', 'clurk'] },
                { correct: 'interest rate', distractors: ['interrest rate', 'intrest rate', 'interest rait'] },
                { correct: 'withdrawal', distractors: ['withdrawl', 'withdral', 'withdrall'] },
                { correct: 'deposit', distractors: ['depposit', 'deposite', 'depozit'] },
                { correct: 'euro', distractors: ['eouro', 'eurro', 'eurou'] },
                { correct: 'freelancer', distractors: ['freelenser', 'freelancerer', 'freelansor'] },
                { correct: 'receptionist', distractors: ['recieptionist', 'receptionnist', 'recepsionist'] },
                { correct: 'internship', distractors: ['interneship', 'intership', 'interneshippe'] },
                { correct: 'spreadsheet', distractors: ['spredsheet', 'spreadsheat', 'spreadshheet'] },
                { correct: 'clerical', distractors: ['clercal', 'clerrical', 'clericall'] },
                { correct: 'administration', distractors: ['administrasion', 'adminastration', 'adminstration'] },
                { correct: 'pension', distractors: ['pention', 'penstion', 'pensoin'] },
                { correct: 'referee', distractors: ['refere', 'refferee', 'referree'] },
                { correct: 'vouch', distractors: ['vouche', 'vouchhe', 'vouchce'] },
                { correct: 'nonfiction', distractors: ['non-fiction', 'nonfictional', 'nonfiksion'] },
                { correct: 'textbook', distractors: ['texbook', 'textbuk', 'texttbook'] },
                { correct: 'encyclopedia', distractors: ['ensyclopedia', 'encyclopida', 'encyclopediya'] },
                { correct: 'photocopier', distractors: ['fotocopier', 'photocopyer', 'photocopierr'] },
                { correct: 'internet access', distractors: ['internet acces', 'internet acsess', 'internett access'] },
                { correct: 'cassette', distractors: ['casette', 'cassett', 'casset'] },
                { correct: 'audio-visual materials', distractors: ['audiovisual materials', 'audio-visual materiels', 'audio-vissual materials'] },
                { correct: 'editorial', distractors: ['editorrial', 'editoriel', 'editoreil'] },
                { correct: 'label', distractors: ['labell', 'labul', 'lable'] },
                { correct: 'allocate', distractors: ['alocate', 'alllocate', 'allocat'] },
                { correct: 'oral test', distractors: ['orall test', 'orral test', 'aural test'] },
                { correct: 'taped interview', distractors: ['tapede interview', 'tapped interview', 'tapedd interview'] },
                { correct: 'questionnaire', distractors: ['questionaire', 'questionairre', 'quesionnaire'] },
                { correct: 'formatting', distractors: ['formating', 'formattingg', 'formattig'] },
                { correct: 'subheadings', distractors: ['subhedings', 'sub-headings', 'subheadins'] },
                { correct: 'contents page', distractors: ['conttents page', 'content page', 'contentss page'] },
                { correct: 'typos', distractors: ['typoss', 'typoz', 'typoes'] },
                { correct: 'bullet points', distractors: ['bulet points', 'bullit points', 'bullet pointss'] },
                { correct: 'footers', distractors: ['footters', 'footerss', 'footerss'] },
                { correct: 'dissertation', distractors: ['dissertasion', 'disertation', 'dissertattion'] },
                { correct: 'coursework', distractors: ['coursewurk', 'courssework', 'courseworks'] },
                { correct: 'second language acquisition', distractors: ['second language aquisition', 'seccond language acquisition', 'second languaje acquisition'] },
                { correct: 'topography', distractors: ['topograpy', 'topographi', 'topograffy'] },
                { correct: 'cartography', distractors: ['cartograpy', 'cartographi', 'cartograffy'] },
                { correct: 'latin america', distractors: ['laten america', 'latinn america', 'latin ammerica'] },
                { correct: 'portuguese', distractors: ['portugues', 'portugeese', 'portuguise'] },
                { correct: 'orientation week', distractors: ['orientasion week', 'orientation wek', 'orientation weke'] },
                { correct: 'course outline', distractors: ['course outlin', 'cours outline', 'course outlyne'] },
                { correct: 'intensive course', distractors: ['intensiv course', 'intenceive course', 'intensive corse'] },
                { correct: 'refresher course', distractors: ['refrecher course', 'refreshur course', 'refresher corse'] },
                { correct: 'training session', distractors: ['training sesion', 'training ssession', 'trainning session'] },
                { correct: 'modular course', distractors: ['moduler course', 'moddular course', 'modular corse'] },
                { correct: 'diploma course', distractors: ['diplomma course', 'diplomaa course', 'diplomma corse'] },
                { correct: 'convener', distractors: ['conveneor', 'convener', 'convener'] },
                { correct: 'counseling center', distractors: ['counceling center', 'counselling center', 'counsaling center'] },
                { correct: 'refectory', distractors: ['refectury', 'refectorey', 'refectoryy'] },
                { correct: 'living quarters', distractors: ['living quaters', 'living quorters', 'living quaterss'] },
                { correct: 'halls of residence', distractors: ['halls of residence', 'halls of resedence', 'halls of residdence'] },
                { correct: 'resources room', distractors: ['resorces room', 'ressources room', 'resourcess room'] },
            ];
            let currentPronunciationQuestion = {};

            // --- DOM ELEMENTS ---
            const views = {
                flashcards: document.getElementById('view-flashcards'),
                antonym: document.getElementById('view-antonym'),
                pronunciation: document.getElementById('view-pronunciation'),
            };
            const tabs = {
                flashcards: document.getElementById('tab-flashcards'),
                antonym: document.getElementById('tab-antonym'),
                pronunciation: document.getElementById('tab-pronunciation'),
            };

            // Flashcard Elements
            const wordListInput = document.getElementById('word-list');
            const saveListBtn = document.getElementById('save-list-btn');
            const playAudioBtn = document.getElementById('play-audio-btn');
            const revealWordBtn = document.getElementById('reveal-word-btn');
            const wordText = document.getElementById('word-text');
            const prevWordBtn = document.getElementById('prev-word-btn');
            const nextWordBtn = document.getElementById('next-word-btn');
            const wordCounter = document.getElementById('word-counter');
            const flashcardInstruction = document.getElementById('flashcard-instruction');

            // Antonym Game Elements
            const antonymChoicesContainer = document.getElementById('antonym-choices');
            const antonymFeedback = document.getElementById('antonym-feedback');

            // Pronunciation Game Elements
            const playPronunciationAudioBtn = document.getElementById('play-pronunciation-audio-btn');
            const pronunciationChoicesContainer = document.getElementById('pronunciation-choices');
            const pronunciationFeedback = document.getElementById('pronunciation-feedback');

            // --- FUNCTIONS ---

            // General
            const speak = (text) => {
                if (synth.speaking) {
                    synth.cancel();
                }
                const utterance = new SpeechSynthesisUtterance(text);
                utterance.lang = 'en-US';
                utterance.rate = 0.9;
                synth.speak(utterance);
            };

            const switchMode = (mode) => {
                currentMode = mode;
                Object.values(views).forEach(v => v.classList.add('hidden'));
                Object.values(tabs).forEach(t => t.classList.remove('tab-active'));
                
                views[mode].classList.remove('hidden');
                tabs[mode].classList.add('tab-active');

                if (mode === 'antonym') setupAntonymGame();
                if (mode === 'pronunciation') setupPronunciationGame();
            };

            // Fisher-Yates Shuffle
            const shuffleArray = (array) => {
                for (let i = array.length - 1; i > 0; i--) {
                    const j = Math.floor(Math.random() * (i + 1));
                    [array[i], array[j]] = [array[j], array[i]];
                }
                return array;
            };

            // Flashcard Functions
            const updateFlashcardView = () => {
                flashcardInstruction.classList.remove('hidden');
                wordText.textContent = wordList[currentWordIndex];
                wordText.classList.add('invisible');
                wordCounter.textContent = `${currentWordIndex + 1} / ${wordList.length}`;
            };

            const saveWordList = () => {
                const words = wordListInput.value.split(',')
                    .map(word => word.trim())
                    .filter(word => word.length > 0);
                if (words.length > 0) {
                    wordList = words;
                    currentWordIndex = 0;
                    updateFlashcardView();
                }
            };
            
            // Antonym Game Functions
            const setupAntonymGame = () => {
                antonymFeedback.textContent = '';
                const randomIndex = Math.floor(Math.random() * antonymData.length);
                currentAntonymQuestion = antonymData[randomIndex];
                
                const choices = shuffleArray([...currentAntonymQuestion.s, currentAntonymQuestion.a]);
                antonymChoicesContainer.innerHTML = '';
                choices.forEach(choice => {
                    const button = document.createElement('button');
                    button.textContent = choice;
                    button.className = 'btn-choice w-full px-4 py-3 border border-gray-300 rounded-lg text-lg font-medium bg-white text-gray-700 hover:bg-gray-50';
                    button.onclick = () => checkAntonymAnswer(choice);
                    antonymChoicesContainer.appendChild(button);
                });
            };

            const checkAntonymAnswer = (selectedWord) => {
                const buttons = antonymChoicesContainer.querySelectorAll('button');
                buttons.forEach(btn => {
                    btn.disabled = true;
                    if (btn.textContent === currentAntonymQuestion.a) {
                        btn.classList.add('correct');
                    } else if (btn.textContent === selectedWord) {
                        btn.classList.add('incorrect');
                    }
                });
                
                if (selectedWord === currentAntonymQuestion.a) {
                    antonymFeedback.textContent = 'Correct!';
                    antonymFeedback.className = 'h-6 text-center font-medium text-green-600';
                } else {
                    antonymFeedback.textContent = 'Not quite. Try the next one!';
                    antonymFeedback.className = 'h-6 text-center font-medium text-red-600';
                }
                
                setTimeout(setupAntonymGame, 2000);
            };

            // Pronunciation Game Functions
            const setupPronunciationGame = () => {
                pronunciationFeedback.textContent = '';
                const randomIndex = Math.floor(Math.random() * pronunciationData.length);
                currentPronunciationQuestion = pronunciationData[randomIndex];

                const choices = shuffleArray([currentPronunciationQuestion.correct, ...currentPronunciationQuestion.distractors]);
                pronunciationChoicesContainer.innerHTML = '';
                 choices.forEach(choice => {
                    const button = document.createElement('button');
                    button.textContent = choice;
                    button.className = 'btn-choice w-full px-4 py-3 border border-gray-300 rounded-lg text-lg font-medium bg-white text-gray-700 hover:bg-gray-50';
                    button.onclick = () => checkPronunciationAnswer(choice);
                    pronunciationChoicesContainer.appendChild(button);
                });
            };

            const checkPronunciationAnswer = (selectedWord) => {
                 const buttons = pronunciationChoicesContainer.querySelectorAll('button');
                buttons.forEach(btn => {
                    btn.disabled = true;
                    if (btn.textContent === currentPronunciationQuestion.correct) {
                        btn.classList.add('correct');
                    } else if (btn.textContent === selectedWord) {
                        btn.classList.add('incorrect');
                    }
                });
                
                if (selectedWord === currentPronunciationQuestion.correct) {
                    pronunciationFeedback.textContent = 'Correct!';
                    pronunciationFeedback.className = 'h-6 text-center font-medium text-green-600';
                } else {
                    pronunciationFeedback.textContent = 'Not quite. Try the next one!';
                    pronunciationFeedback.className = 'h-6 text-center font-medium text-red-600';
                }
                
                setTimeout(setupPronunciationGame, 2000);
            };

            // --- EVENT LISTENERS ---
            Object.keys(tabs).forEach(key => {
                tabs[key].addEventListener('click', () => switchMode(key));
            });

            // Flashcard listeners
            playAudioBtn.addEventListener('click', () => {
                speak(wordList[currentWordIndex]);
            });

            revealWordBtn.addEventListener('click', () => {
                flashcardInstruction.classList.add('hidden');
                wordText.classList.remove('invisible');
            });

            nextWordBtn.addEventListener('click', () => {
                currentWordIndex = (currentWordIndex + 1) % wordList.length;
                updateFlashcardView();
            });

            prevWordBtn.addEventListener('click', () => {
                currentWordIndex = (currentWordIndex - 1 + wordList.length) % wordList.length;
                updateFlashcardView();
            });

            saveListBtn.addEventListener('click', saveWordList);

            // Pronunciation game listener
            playPronunciationAudioBtn.addEventListener('click', () => {
                speak(currentPronunciationQuestion.correct);
            });


            // --- INITIALIZATION ---
            wordListInput.value = wordList.join(', ');
            updateFlashcardView();
            switchMode('flashcards'); // Start in flashcards mode
        });
    </script>
</body>
</html>
"""

# Use Streamlit's components to display the HTML content
st.set_page_config(page_title="English Listening Helper", layout="wide")
components.html(html_content, height=800, scrolling=True)
