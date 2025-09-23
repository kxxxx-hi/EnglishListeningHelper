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
            /*
                // Innovative (创新的) - Traditional (传统的)
                { s: ['Innovative', 'Original', 'Creative'], a: 'Traditional' },
                // Unconventional (非传统的) - Conventional (传统的)
                { s: ['Unconventional', 'Unorthodox', 'Offbeat'], a: 'Conventional' },
                // Idiosyncratic (特质的) - Common (常见的)
                { s: ['Idiosyncratic', 'Peculiar', 'Distinctive'], a: 'Common' },
                // Eclectic (折衷的) - Uniform (统一的)
                { s: ['Eclectic', 'Diverse', 'Varied'], a: 'Uniform' },
                // Whimsical (异想天开的) - Serious (严肃的)
                { s: ['Whimsical', 'Playful', 'Fanciful'], a: 'Serious' },
                // Visionary (有远见的) - Short-sighted (目光短浅的)
                { s: ['Visionary', 'Forward-looking', 'Prophetic'], a: 'Short-sighted' },
                // Pioneering (开创性的) - Following (追随者)
                { s: ['Pioneering', 'Groundbreaking', 'Leading'], a: 'Following' },
                // Quirky (古怪的) - Normal (正常的)
                { s: ['Quirky', 'Peculiar', 'Odd'], a: 'Normal' },
                // Aesthetic (审美的) - Unappealing (不吸引人的)
                { s: ['Aesthetic', 'Artistic', 'Beautiful'], a: 'Unappealing' },
                // Profound (深奥的) - Superficial (肤浅的)
                { s: ['Profound', 'Deep', 'Meaningful'], a: 'Superficial' },
                // Introspective (内省的) - Extroverted (外向的)
                { s: ['Introspective', 'Meditative', 'Reflective'], a: 'Extroverted' },
                // Maverick (特立独行的) - Conformist (墨守成规的)
                { s: ['Maverick', 'Rebel', 'Individualist'], a: 'Conformist' },
                // Versatile (多才多艺的) - Inflexible (不灵活的)
                { s: ['Versatile', 'Adaptable', 'Flexible'], a: 'Inflexible' },
                // Charismatic (有魅力的) - Uninspiring (乏味的)
                { s: ['Charismatic', 'Magnetic', 'Charming'], a: 'Uninspiring' },
                // Uninhibited (无拘无束的) - Reserved (内敛的)
                { s: ['Uninhibited', 'Free-spirited', 'Spontaneous'], a: 'Reserved' },
                // Compassionate (有同情心的) - Cruel (残忍的)
                { s: ['Compassionate', 'Caring', 'Sympathetic'], a: 'Cruel' },
                // Empathetic (有同理心的) - Indifferent (漠不关心的)
                { s: ['Empathetic', 'Understanding', 'Sensitive'], a: 'Indifferent' },
                // Loyal (忠诚的) - Treacherous (背信弃义的)
                { s: ['Loyal', 'Faithful', 'Devoted'], a: 'Treacherous' },
                // Reliable (可靠的) - Untrustworthy (不可靠的)
                { s: ['Reliable', 'Trustworthy', 'Dependable'], a: 'Untrustworthy' },
                // Sincere (真诚的) - Insincere (不真诚的)
                { s: ['Sincere', 'Genuine', 'Heartfelt'], a: 'Insincere' },
                // Affectionate (深情的) - Cold (冷淡的)
                { s: ['Affectionate', 'Loving', 'Warm'], a: 'Cold' },
                // Supportive (支持的) - Unhelpful (无助的)
                { s: ['Supportive', 'Encouraging', 'Helpful'], a: 'Unhelpful' },
                // Genuine (真诚的) - Fake (假的)
                { s: ['Genuine', 'Authentic', 'Real'], a: 'Fake' },
                // Kind-hearted (好心的) - Mean (刻薄的)
                { s: ['Kind-hearted', 'Benevolent', 'Generous'], a: 'Mean' },
                // Selfless (无私的) - Selfish (自私的)
                { s: ['Selfless', 'Altruistic', 'Giving'], a: 'Selfish' },
                // Candid (坦率的) - Deceptive (欺骗的)
                { s: ['Candid', 'Frank', 'Open'], a: 'Deceptive' },
                // Understanding (善解人意的) - Intolerant (不宽容的)
                { s: ['Understanding', 'Tolerant', 'Patient'], a: 'Intolerant' },
                // Dependable (值得信赖的) - Unreliable (不可靠的)
                { s: ['Dependable', 'Reliable', 'Trustworthy'], a: 'Unreliable' },
                // Patient (有耐心的) - Impatient (不耐烦的)
                { s: ['Patient', 'Tolerant', 'Calm'], a: 'Impatient' },
                // Humble (谦逊的) - Arrogant (傲慢的)
                { s: ['Humble', 'Modest', 'Meek'], a: 'Arrogant' },
                // Benevolent (仁慈的) - Malicious (恶毒的)
                { s: ['Benevolent', 'Kind', 'Generous'], a: 'Malicious' },
                // Encouraging (鼓舞人心的) - Discouraging (令人沮丧的)
                { s: ['Encouraging', 'Inspiring', 'Uplifting'], a: 'Discouraging' },
                // Thoughtful (体贴的) - Thoughtless (不体贴的)
                { s: ['Thoughtful', 'Considerate', 'Mindful'], a: 'Thoughtless' },
                // Gracious (亲切的) - Rude (粗鲁的)
                { s: ['Gracious', 'Courteous', 'Polite'], a: 'Rude' },
                // Principled (有原则的) - Unprincipled (无原则的)
                { s: ['Principled', 'Ethical', 'Moral'], a: 'Unprincipled' },
                // Witty (机智的) - Dull (乏味的)
                { s: ['Witty', 'Clever', 'Humorous'], a: 'Dull' },
                // Perceptive (有洞察力的) - Oblivious (未察觉的)
                { s: ['Perceptive', 'Insightful', 'Discerning'], a: 'Oblivious' },
                // Prudent (审慎的) - Reckless (鲁莽的)
                { s: ['Prudent', 'Cautious', 'Wise'], a: 'Reckless' },
                // Insightful (富有见地的) - Shallow (肤浅的)
                { s: ['Insightful', 'Perceptive', 'Discerning'], a: 'Shallow' },
                // Cultivated (有教养的) - Uncouth (粗俗的)
                { s: ['Cultivated', 'Refined', 'Educated'], a: 'Uncouth' },
                // Philosophical (哲学的) - Practical (实际的)
                { s: ['Philosophical', 'Pensive', 'Intellectual'], a: 'Practical' },
                // Resilient (有弹性的、坚韧的) - Fragile (脆弱的)
                { s: ['Resilient', 'Tough', 'Durable'], a: 'Fragile' },
                // Enlightened (开明的) - Ignorant (无知的)
                { s: ['Enlightened', 'Educated', 'Informed'], a: 'Ignorant' },
                // Rational (理性的) - Irrational (不理性的)
                { s: ['Rational', 'Logical', 'Reasonable'], a: 'Irrational' },
                // Discreet (谨慎的) - Obvious (明显的)
                { s: ['Discreet', 'Cautious', 'Circumspect'], a: 'Obvious' },
                // Judicious (明断的) - Imprudent (不慎重的)
                { s: ['Judicious', 'Wise', 'Sensible'], a: 'Imprudent' },
                // Reflective (沉思的) - Spontaneous (冲动的)
                { s: ['Reflective', 'Thoughtful', 'Contemplative'], a: 'Spontaneous' },
                // Astute (敏锐的) - Naive (天真的)
                { s: ['Astute', 'Shrewd', 'Clever'], a: 'Naive' },
                // Driven (有上进心的) - Apathetic (冷漠的)
                { s: ['Driven', 'Ambitious', 'Motivated'], a: 'Apathetic' },
                // Ambitious (有抱负的) - Content (知足的)
                { s: ['Ambitious', 'Determined', 'Aspiring'], a: 'Content' },
                // Persistent (坚持不懈的) - Quitting (放弃的)
                { s: ['Persistent', 'Tenacious', 'Relentless'], a: 'Quitting' },
                // Resolute (坚决的) - Hesitant (犹豫的)
                { s: ['Resolute', 'Firm', 'Steadfast'], a: 'Hesitant' },
                // Energetic (精力充沛的) - Lethargic (无精打采的)
                { s: ['Energetic', 'Vigorous', 'Dynamic'], a: 'Lethargic' },
                // Disciplined (有纪律的) - Undisciplined (无纪律的)
                { s: ['Disciplined', 'Controlled', 'Methodical'], a: 'Undisciplined' },
                // Relentless (不懈的) - Half-hearted (三心二意的)
                { s: ['Relentless', 'Persistent', 'Unrelenting'], a: 'Half-hearted' },
                // Proactive (积极主动的) - Reactive (被动的)
                { s: ['Proactive', 'Initiating', 'Forward-thinking'], a: 'Reactive' },
                // Meticulous (一丝不苟的) - Careless (粗心的)
                { s: ['Meticulous', 'Thorough', 'Precise'], a: 'Careless' },
                // Dedicated (敬业的) - Indifferent (漠不关心的)
                { s: ['Dedicated', 'Committed', 'Devoted'], a: 'Indifferent' },
                // Goal-oriented (以目标为导向的) - Aimless (无目标的)
                { s: ['Goal-oriented', 'Focused', 'Purposeful'], a: 'Aimless' },
                // Assertive (自信的) - Passive (被动的)
                { s: ['Assertive', 'Confident', 'Decisive'], a: 'Passive' },
                // Resourceful (足智多谋的) - Helpless (无助的)
                { s: ['Resourceful', 'Ingenious', 'Clever'], a: 'Helpless' },
                // Perseverant (有毅力的) - Faltering (动摇的)
                { s: ['Perseverant', 'Persistent', 'Steadfast'], a: 'Faltering' },
                // Determined (有决心的) - Undecided (未决的)
                { s: ['Determined', 'Resolute', 'Firm'], a: 'Undecided' },
                // Competitive (有竞争力的) - Cooperative (合作的)
                { s: ['Competitive', 'Rivalrous', 'Ambitious'], a: 'Cooperative' },
                // Tenacious (坚韧的) - Weak (弱小的)
                { s: ['Tenacious', 'Resolute', 'Stubborn'], a: 'Weak' },
                // Audacious (大胆的) - Cautious (谨慎的)
                { s: ['Audacious', 'Bold', 'Daring'], a: 'Cautious' },
                // Strategic (有战略性的) - Haphazard (杂乱无章的)
                { s: ['Strategic', 'Tactical', 'Planned'], a: 'Haphazard' },
                // Inspiring (鼓舞人心的) - Demoralizing (令人沮丧的)
                { s: ['Inspiring', 'Uplifting', 'Motivating'], a: 'Demoralizing' },
                
                // --- 新增词汇 ---

                // 1. 可持续发展
                { s: ['Sustainability', 'Viability', 'Durability'], a: 'Unsustainability' },
                { s: ['Conservation', 'Preservation', 'Safeguarding'], a: 'Destruction' },
                { s: ['Deforestation', 'Logging', 'Forest clearance'], a: 'Reforestation' },
                { s: ['Biodiversity', 'Variety of life', 'Biological diversity'], a: 'Uniformity' },
                { s: ['Emission', 'Discharge', 'Output'], a: 'Absorption' },
                { s: ['Renewable energy', 'Solar', 'Wind'], a: 'Non-renewable energy' },
                { s: ['Climate change', 'Global warming', 'Climate crisis'], a: 'Climate stability' },
                { s: ['Pollution', 'Contamination', 'Degradation'], a: 'Purity' },
                { s: ['Ecosystem', 'Habitat', 'Biome'], a: 'Disruption' },
                { s: ['Extinction', 'Disappearance', 'Annihilation'], a: 'Survival' },
            
                // 2. 旅游
                { s: ['Itinerary', 'Schedule', 'Travel plan'], a: 'Spontaneity' },
                { s: ['Accommodation', 'Lodging', 'Residence'], a: 'Nomadism' },
                { s: ['Hospitality', 'Welcome', 'Friendliness'], a: 'Hostility' },
                { s: ['Excursion', 'Trip', 'Outing'], a: 'Residency' },
                { s: ['Voyage', 'Journey', 'Expedition'], a: 'Immobility' },
                { s: ['Expedition', 'Exploration', 'Adventure'], a: 'Retreat' },
                { s: ['Backpacking', 'Budget travel', 'Independent travel'], a: 'Luxury travel' },
                { s: ['Trek', 'Hike', 'Long journey'], a: 'Stroll' },
                { s: ['Passport', 'Travel document', 'ID'], a: 'Restriction' },
            
                // 3. 健康与医学
                { s: ['Epidemic', 'Outbreak', 'Contagion'], a: 'Wellness' },
                { s: ['Pandemic', 'Global epidemic', 'Worldwide outbreak'], a: 'Localized outbreak' },
                { s: ['Immunity', 'Resistance', 'Protection'], a: 'Vulnerability' },
                { s: ['Vaccination', 'Immunization', 'Inoculation'], a: 'Infection' },
                { s: ['Nutrition', 'Nourishment', 'Sustenance'], a: 'Deprivation' },
                { s: ['Malnutrition', 'Undernourishment', 'Deficiency'], a: 'Overnutrition' },
                { s: ['Obesity', 'Overweight', 'Corpulence'], a: 'Underweight' },
                { s: ['Rehabilitation', 'Recovery', 'Therapy'], a: 'Deterioration' },
                { s: ['Prevention', 'Precaution', 'Protection'], a: 'Causation' },
                { s: ['Therapy', 'Treatment', 'Healing'], a: 'Illness' },
                { s: ['Surgery', 'Operation', 'Procedure'], a: 'Natural healing' },
                { s: ['Transplant', 'Graft', 'Implantation'], a: 'Rejection' },
                { s: ['Genetics', 'Heredity', 'DNA science'], a: 'Nurture' },
                { s: ['Mental health', 'Psychological well-being', 'Emotional stability'], a: 'Mental illness' },
                { s: ['Anxiety', 'Nervousness', 'Worry'], a: 'Calmness' },
                { s: ['Therapy session', 'Counseling', 'Consultation'], a: 'Avoidance' },
                { s: ['Clinical trial', 'Medical study', 'Drug testing'], a: 'Anecdotal evidence' },
                { s: ['Placebo', 'Dummy pill', 'Inactive drug'], a: 'Active drug' },
                { s: ['Pathogen', 'Germ', 'Microbe'], a: 'Antiseptic' },
                { s: ['Virus', 'Microorganism', 'Contagion'], a: 'Antibody' },
                { s: ['Bacteria', 'Microbes', 'Germs'], a: 'Antibiotic' },
                { s: ['Antibiotic', 'Antimicrobial drug', 'Medicine'], a: 'Bacteria' },
                { s: ['Antiviral', 'Virus-fighting drug', 'Treatment'], a: 'Pro-viral' },
                { s: ['Herbal remedy', 'Plant medicine', 'Alternative cure'], a: 'Synthetic drug' },
                { s: ['Alternative medicine', 'Complementary therapy', 'Holistic healing'], a: 'Conventional medicine' },
                { s: ['Side effect', 'Adverse reaction', 'Secondary effect'], a: 'Intended effect' },
                { s: ['Life expectancy', 'Lifespan', 'Longevity'], a: 'Mortality rate' },
                { s: ['Mortality rate', 'Death rate', 'Fatality rate'], a: 'Birth rate' },
            
                // 4. 职业与工作
                { s: ['Employment', 'Job', 'Occupation'], a: 'Unemployment' },
                { s: ['Unemployment', 'Joblessness', 'Redundancy'], a: 'Employment' },
                { s: ['Occupation', 'Profession', 'Trade'], a: 'Hobby' },
                { s: ['Profession', 'Vocation', 'Discipline'], a: 'Amateurism' },
                { s: ['Apprenticeship', 'Training', 'Internship'], a: 'Mastery' },
                { s: ['Promotion', 'Advancement', 'Elevation'], a: 'Demotion' },
                { s: ['Demotion', 'Downgrade', 'Reduction'], a: 'Promotion' },
                { s: ['Salary', 'Wage', 'Income'], a: 'Debt' },
                { s: ['Wage', 'Earnings', 'Remuneration'], a: 'Expense' },
                { s: ['Income', 'Revenue', 'Earning'], a: 'Outgoings' },
                { s: ['Overtime', 'Extra work', 'Additional hours'], a: 'Leisure time' },
                { s: ['Benefits', 'Perks', 'Advantages'], a: 'Liabilities' },
                { s: ['Pension', 'Retirement fund', 'Allowance'], a: 'Current income' },
                { s: ['Retirement', 'End of career', 'Pensioning off'], a: 'Employment' },
                { s: ['Job satisfaction', 'Fulfillment', 'Contentment'], a: 'Job dissatisfaction' },
                */


                // 5. Society
                { s: ['Community', 'Neighborhood', 'Collective'], a: 'Isolation' },
                { s: ['Population', 'Inhabitants', 'Residents'], a: 'Depopulation' },
                { s: ['Demographics', 'Population data', 'Statistics'], a: 'Anecdotes' },
                { s: ['Urbanization', 'City development', 'Metropolitan growth'], a: 'Ruralization' },
                { s: ['Suburbanization', 'Suburban growth', 'Urban sprawl'], a: 'Centralization' },
                { s: ['Migration', 'Relocation', 'Resettlement'], a: 'Immobility' },
                { s: ['Immigration', 'In-migration', 'Entry'], a: 'Emigration' },
                { s: ['Emigration', 'Out-migration', 'Departure'], a: 'Immigration' },
                { s: ['Multiculturalism', 'Cultural diversity', 'Pluralism'], a: 'Homogeneity' },
                { s: ['Assimilation', 'Integration', 'Incorporation'], a: 'Segregation' },
                { s: ['Integration', 'Inclusion', 'Unification'], a: 'Exclusion' },
                { s: ['Segregation', 'Separation', 'Division'], a: 'Integration' },
                { s: ['Inequality', 'Disparity', 'Imbalance'], a: 'Equality' },
                { s: ['Poverty', 'Destitution', 'Deprivation'], a: 'Affluence' },
                { s: ['Affluence', 'Wealth', 'Prosperity'], a: 'Poverty' },
                { s: ['Social mobility', 'Class movement', 'Upward mobility'], a: 'Social stagnation' },
                { s: ['Class system', 'Social hierarchy', 'Stratification'], a: 'Classless society' },
                { s: ['Hierarchy', 'Ranking', 'Structure'], a: 'Anarchy' },
                { s: ['Discrimination', 'Prejudice', 'Bias'], a: 'Fairness' },
                { s: ['Prejudice', 'Intolerance', 'Unfair judgment'], a: 'Tolerance' },
                { s: ['Racism', 'Racial discrimination', 'Bigotry'], a: 'Racial equality' },
                { s: ['Sexism', 'Gender bias', 'Inequality'], a: 'Gender equality' },
                { s: ['Ageism', 'Age bias', 'Generational prejudice'], a: 'Age equality' },
                { s: ['Feminism', 'Women’s rights', 'Gender equality'], a: 'Misogyny' },
                { s: ['Activism', 'Advocacy', 'Campaigning'], a: 'Passivity' },
                { s: ['Civil rights', 'Freedoms', 'Equal rights'], a: 'Oppression' },
                { s: ['Human rights', 'Fundamental rights', 'Entitlements'], a: 'Abuse of rights' },
                { s: ['Legislation', 'Lawmaking', 'Statute'], a: 'Deregulation' },
                { s: ['Policy', 'Strategy', 'Guideline'], a: 'Randomness' },
                { s: ['Governance', 'Administration', 'Control'], a: 'Mismanagement' },
                { s: ['Government', 'Administration', 'Regime'], a: 'Anarchy' },
                { s: ['Authority', 'Power', 'Control'], a: 'Subordination' },
                { s: ['Bureaucracy', 'Officialdom', 'Red tape'], a: 'Efficiency' },
                { s: ['Welfare', 'Well-being', 'Benefits'], a: 'Hardship' },
                { s: ['Healthcare system', 'Medical services', 'Hospital system'], a: 'Health decline' },
                { s: ['Education system', 'Schooling system', 'Academic structure'], a: 'Ignorance' },
                { s: ['Public services', 'Utilities', 'Community support'], a: 'Private services' },
                { s: ['Infrastructure', 'Facilities', 'Framework'], a: 'Dilapidation' },
                { s: ['Transport system', 'Transit network', 'Public transport'], a: 'Private transport' },
                { s: ['Justice system', 'Courts', 'Legal framework'], a: 'Injustice' },
                { s: ['Law enforcement', 'Policing', 'Authorities'], a: 'Lawlessness' },
                { s: ['Crime rate', 'Level of crime', 'Criminal statistics'], a: 'Peacefulness' },
                { s: ['Social norm', 'Custom', 'Expectation'], a: 'Deviance' },
                { s: ['Cultural heritage', 'Tradition', 'Legacy'], a: 'Cultural loss' },
                { s: ['Tradition', 'Custom', 'Heritage'], a: 'Modernity' },
                { s: ['Ritual', 'Ceremony', 'Custom'], a: 'Spontaneity' },
                { s: ['Festival', 'Celebration', 'Holiday'], a: 'Routine' },
                { s: ['Civic duty', 'Responsibility', 'Public service'], a: 'Negligence' },
                { s: ['Volunteering', 'Unpaid work', 'Community service'], a: 'Mandatory work' },
                { s: ['Philanthropy', 'Charity', 'Generosity'], a: 'Stinginess' }
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
