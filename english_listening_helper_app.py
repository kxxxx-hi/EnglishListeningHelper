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
                    <label for="correct-list" class="block text-sm font-medium text-gray-700">Customize correct List (comma-separated)</label>
                    <textarea id="correct-list" rows="3" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm" placeholder="e.g., apple, beautiful, challenge, ..."></textarea>
                    <button id="save-list-btn" class="mt-2 w-full inline-flex justify-center items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Save and Use This List
                    </button>
                </div>
                
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner">
                    <div id="flashcard-container" class="card">
                        <p id="flashcard-instruction" class="text-gray-500 mb-4">Click the speaker to hear the correct.</p>
                        <button id="play-audio-btn" class="w-24 h-24 bg-indigo-100 rounded-full flex items-center justify-center text-indigo-600 hover:bg-indigo-200 transition-colors">
                            <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z" /></svg>
                        </button>
                        <div id="correct-reveal" class="mt-4 h-10">
                            <h2 id="correct-text" class="text-4xl font-bold text-gray-800 invisible"></h2>
                        </div>
                    </div>
                     <button id="reveal-correct-btn" class="mt-4 inline-flex items-center px-4 py-2 border border-gray-300 text-sm font-medium rounded-md shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                        Reveal correct
                    </button>
                </div>

                <div class="flex justify-between items-center">
                    <button id="prev-correct-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" /></svg>
                    </button>
                    <span id="correct-counter" class="text-sm font-medium text-gray-600">1 / 10</span>
                    <button id="next-correct-btn" class="p-3 rounded-full bg-gray-200 hover:bg-gray-300">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7" /></svg>
                    </button>
                </div>
            </div>

            <!-- Antonym Game -->
            <div id="view-antonym" class="hidden space-y-6">
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Exclude the Antonym</h3>
                    <p class="text-gray-500 mb-6">Three corrects are synonyms. Click the one that is the antonym.</p>
                    <div id="antonym-choices" class="grid grid-cols-2 gap-4 w-full max-w-md">
                        <!-- Buttons will be generated here -->
                    </div>
                </div>
                 <div id="antonym-feedback" class="h-6 text-center font-medium"></div>
            </div>

            <!-- Pronunciation Game -->
            <div id="view-pronunciation" class="hidden space-y-6">
                <div class="bg-gray-50 rounded-lg p-6 text-center shadow-inner card">
                    <h3 class="text-xl font-semibold text-gray-800 mb-2">Choose the Correct correct</h3>
                    <p class="text-gray-500 mb-6">Listen to the audio and click the matching correct.</p>
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
            let correctList = ['eloquent', 'gregarious', 'resilience', 'ubiquitous', 'ephemeral', 'serendipity', 'magnanimous', 'perspicacious', 'conundrum', 'juxtaposition'];
            let currentcorrectIndex = 0;
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
            /*
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
                */



                { correct: "community", distractors: ["comunity", "communiity", "comunitee"], translation: "社区" },
                { correct: "population", distractors: ["populasion", "populattion", "populaton"], translation: "人口" },
                { correct: "demographics", distractors: ["demografics", "demographicks", "demographcs"], translation: "人口统计" },
                { correct: "urbanization", distractors: ["urbanisation", "urbanizasion", "urbanisation"], translation: "城市化" },
                { correct: "suburbanization", distractors: ["suburbanisation", "suburbanizasion", "subarbanization"], translation: "郊区化" },
                { correct: "migration", distractors: ["migrasion", "migraton", "migraition"], translation: "移民/迁徙" },
                { correct: "immigration", distractors: ["imigration", "immigrasion", "immigraton"], translation: "移民进入" },
                { correct: "emigration", distractors: ["emmigration", "emigrasion", "emigraton"], translation: "移民外出" },
                { correct: "multiculturalism", distractors: ["multiculturism", "multiculturealism", "multicultralism"], translation: "多元文化主义" },
                { correct: "assimilation", distractors: ["asimilation", "assimilasion", "assimiliation"], translation: "融合" },
                { correct: "integration", distractors: ["intigration", "integrasion", "intagration"], translation: "融合" },
                { correct: "segregation", distractors: ["segreagation", "segregattion", "segregetion"], translation: "隔离" },
                { correct: "inequality", distractors: ["inequallity", "inequalety", "inequalitty"], translation: "不平等" },
                { correct: "poverty", distractors: ["povverty", "poverety", "povertyy"], translation: "贫困" },
                { correct: "affluence", distractors: ["affluance", "aflluence", "affluencee"], translation: "富裕" },
                { correct: "social mobility", distractors: ["social mobilitty", "social mobilety", "sociial mobility"], translation: "社会流动" },
                { correct: "class system", distractors: ["class sistim", "clas system", "classs system"], translation: "阶级制度" },
                { correct: "hierarchy", distractors: ["heirarchy", "hierachy", "hierarky"], translation: "等级制度" },
                { correct: "discrimination", distractors: ["discrimanation", "discriminattion", "discremination"], translation: "歧视" },
                { correct: "prejudice", distractors: ["prejedice", "prejudise", "prejudisce"], translation: "偏见" },
                { correct: "racism", distractors: ["racisim", "racisum", "racisme"], translation: "种族主义" },
                { correct: "sexism", distractors: ["sexims", "sexissm", "sexizm"], translation: "性别歧视" },
                { correct: "ageism", distractors: ["ageizm", "ageisms", "ageisim"], translation: "年龄歧视" },
                { correct: "feminism", distractors: ["feminisim", "feminissm", "feminizm"], translation: "女权主义" },
                { correct: "activism", distractors: ["activisim", "activisum", "activisme"], translation: "行动主义" },
                { correct: "civil rights", distractors: ["civil rigths", "civel rights", "civil rightss"], translation: "公民权利" },
                { correct: "human rights", distractors: ["human rigths", "human rightss", "human rites"], translation: "人权" },
                { correct: "legislation", distractors: ["legislasion", "legistlation", "legisation"], translation: "立法" },
                { correct: "policy", distractors: ["pollicy", "polocy", "polisy"], translation: "政策" },
                { correct: "governance", distractors: ["governanse", "governancee", "governance"], translation: "治理" },
                { correct: "government", distractors: ["goverment", "governmant", "governmint"], translation: "政府" },
                { correct: "authority", distractors: ["autherity", "authoritty", "autority"], translation: "权威/当局" },
                { correct: "bureaucracy", distractors: ["bureacracy", "burocracy", "bureucracy"], translation: "官僚体制" },
                { correct: "welfare", distractors: ["welfair", "welafre", "welafare"], translation: "福利" },
                { correct: "healthcare system", distractors: ["health care system", "healtcare system", "hethcare system"], translation: "医疗体系" },
                { correct: "education system", distractors: ["educasion system", "edjucation system", "educations system"], translation: "教育体系" },
                { correct: "public services", distractors: ["public servises", "public servicess", "pubblic services"], translation: "公共服务" },
                { correct: "infrastructure", distractors: ["infrastruture", "infrastructture", "infastructure"], translation: "基础设施" },
                { correct: "transport system", distractors: ["tranport system", "transpport system", "transport sistim"], translation: "交通体系" },
                { correct: "justice system", distractors: ["justise system", "justic system", "justise sistim"], translation: "司法体系" },
                { correct: "law enforcement", distractors: ["law enforsement", "law enforcment", "law enforcmant"], translation: "执法" },
                { correct: "crime rate", distractors: ["crrime rate", "cime rate", "krim rate"], translation: "犯罪率" },
                { correct: "social norm", distractors: ["social normm", "sosial norm", "soacial norm"], translation: "社会规范" },
                { correct: "cultural heritage", distractors: ["culturral heritage", "cultural haritage", "cultural herritage"], translation: "文化遗产" },
                { correct: "tradition", distractors: ["tradission", "traditionn", "tradition"], translation: "传统" },
                { correct: "ritual", distractors: ["ritul", "rittual", "rituel"], translation: "仪式" },
                { correct: "festival", distractors: ["festivall", "festivel", "festaval"], translation: "节日" },
                { correct: "civic duty", distractors: ["civic dutty", "civik duty", "cevic duty"], translation: "公民义务" },
                { correct: "volunteering", distractors: ["voluntering", "voluntaring", "volunterring"], translation: "志愿服务" },
                { correct: "philanthropy", distractors: ["filanthropy", "philanthorpy", "philanthrophy"], translation: "慈善事业" }

                
                { "correct": "vulnerable", "distractors": ["volnerable", "vunerable", "vulnarable"], "translation": "脆弱的;易受伤的" },
                { "correct": "infectious", "distractors": ["infectioud", "infectous", "infecious"], "translation": "传染性的;有感染力的" },
                { "correct": "physician", "distractors": ["physicians", "phycisian", "physican"], "translation": "医生;内科医生" },
                { "correct": "practitioner", "distractors": ["prectationer", "practicioner", "practitoner"], "translation": "实践者;从业者;执业者" },
                { "correct": "veterinarian", "distractors": ["viterynarian", "veterinarien", "veterianarian"], "translation": "兽医" },
                { "correct": "have a stuffed nose", "distractors": ["have a stuff nose", "have a stuffed noes", "have a stufed nose"], "translation": "鼻塞的；鼻子不通气的" },
                { "correct": "quarantine service", "distractors": ["quaranting service", "quarentine service", "quarantine servise"], "translation": "检疫服务；隔离检疫部门" },
                { "correct": "composition", "distractors": ["composation", "compositon", "componsition"], "translation": "构成;作品;（学生）作文;创作技巧" },
                { "correct": "claw", "distractors": ["clwa", "clow", "claww"], "translation": "爪;钳;抓" },
                { "correct": "predator", "distractors": ["prediter", "predetor", "preditor"], "translation": "掠夺者;捕食性动物;食肉动物" },
                { "correct": "proliferate", "distractors": ["preliverate", "proliferete", "proliferat"], "translation": "激增" },
                { "correct": "photosynthesis", "distractors": ["photosynthetic", "photosinthesis", "photosynthisis"], "translation": "光合作⽤" },
                { "correct": "ozone", "distractors": ["ozne", "ozon", "oazone"], "translation": "臭氧" },
                { "correct": "salinity", "distractors": ["salinaty", "salinityy", "salinirty"], "translation": "盐分;含盐量" },
                { "correct": "carbohydrate", "distractors": ["caberhtdrate", "carbohydreate", "carbohidrate"], "translation": "碳水化合物;糖类" },
                { "correct": "descend", "distractors": ["descenf", "desend", "desscend"], "translation": "下降;突然造访;突袭;沦落;起源" },
                { "correct": "dinosaur", "distractors": ["dinosaut", "dinasaur", "dinosour"], "translation": "恐龙" },
                { "correct": "ostrich", "distractors": ["ostrach", "ostrichh", "ostrish"], "translation": "鸵鸟" },
                { "correct": "pollinate", "distractors": ["pellenate", "polinate", "pollinatee"], "translation": "授粉;传粉" },
                { "correct": "limbs", "distractors": ["limbd", "limbses", "lombs"], "translation": "肢体;大树枝" },
                { "correct": "wheat", "distractors": ["wheak", "wheet", "wheate"], "translation": "小麦;小麦色" },
                { "correct": "barley", "distractors": ["bulley", "barly", "barleyy"], "translation": "大麦;大麦粒" },
                { "correct": "poultry", "distractors": ["pultry", "poutry", "poulty"], "translation": "家禽" },
                { "correct": "merchant", "distractors": ["murchant", "merchent", "merchand"], "translation": "商人" },
                { "correct": "physiology", "distractors": ["physilogy", "physiollogy", "physiologie"], "translation": "生理学" },
                { "correct": "sanctuary", "distractors": ["sanctary", "sancuary", "sanctuery"], "translation": "避难所;庇护所;庇护;圣所" },
                { "correct": "hibernation", "distractors": ["hybernation", "hibernasion", "hibernantion"], "translation": "冬眠" },
                { "correct": "nutrient", "distractors": ["nutriant", "nutrientt", "nutreint"], "translation": "营养的;营养物" },
                { "correct": "reproduction", "distractors": ["reperduction", "reproducton", "reprodution"], "translation": "生殖;繁殖;复制" },
                { "correct": "hatch out", "distractors": ["huntch out", "hacth out", "hatchout"], "translation": "（尤指小鸡等）孵出；孵化完成" },
                { "correct": "monogamous", "distractors": ["monogomous", "monogamouss", "monogamouse"], "translation": "一夫一妻制的" },
                { "correct": "fatal", "distractors": ["phyt", "fatel", "fatol"], "translation": "致命的;灾难性的" },
                { "correct": "parasite", "distractors": ["parisite", "parasight", "parasitee"], "translation": "寄生虫;寄生生物;依赖他人过活者" },
                { "correct": "deforestation", "distractors": ["diforestation", "deforistation", "deforastation"], "translation": "采伐森林;森林开伐" },
                { "correct": "cholesterol", "distractors": ["colesterol", "cholestrol", "cholesteral"], "translation": "胆固醇" },
                { "correct": "amino acid", "distractors": ["aminal asid", "amino acide", "ameno acid"], "translation": "氨基酸（构成蛋白质的基本单位）" },
                { "correct": "bitterness", "distractors": ["bitternuse", "biterness", "bitteress"], "translation": "苦味，苦" },
                { "correct": "kilocalorie", "distractors": ["kilocallery", "kilocalory", "kilokalorie"], "translation": "千卡;大卡" },
                { "correct": "metabolism", "distractors": ["matabolism", "metablism", "metabolisim"], "translation": "新陈代谢" },
                { "correct": "indigestible", "distractors": ["indigestable", "indigestiable", "indigestiblee"], "translation": "难消化的，无法消化的" },
                { "correct": "eradicate", "distractors": ["irridicate", "eradictate", "eradicatee"], "translation": "消灭;灭绝;根除" },
                { "correct": "reptile", "distractors": ["reptail", "ripeta", "reptille"], "translation": "爬行动物;爬虫类的" },
                { "correct": "dolphin", "distractors": ["dophin", "dolfin", "dolphine"], "translation": "海豚" },
        
                { "correct": "flora", "distractors": ["s", "florra", "florae"], "translation": "植物群落" },
                { "correct": "pouch", "distractors": ["pawch", "pouth", "pouchh"], "translation": "小袋;囊状袋;育儿袋;装入袋中" },
                { "correct": "scale", "distractors": ["skill", "scal", "scales"], "translation": "规模;等级;秤;刻度;比例（尺）;改变…大小;攀登" },
                { "correct": "produce", "distractors": ["produc", "pruduce", "producee"], "translation": "生产;制造;出示;导致;农产品" },
                { "correct": "poultry", "distractors": ["pultry", "poulrty", "poutry"], "translation": "家禽" },
                { "correct": "livestock", "distractors": ["lifestock", "livestok", "livestockk"], "translation": "家畜;牲畜" },
                { "correct": "fishstock", "distractors": ["fish stock", "fishstok", "fishstcok"], "translation": "鱼群；鱼类资源" },
                { "correct": "herd", "distractors": ["hurt", "herdd", "heard"], "translation": "兽群;放牧;（强制）集合" },
                { "correct": "cereal crops", "distractors": ["therialcrops", "cerealcrops", "cereal corp"], "translation": "谷类作物" },
                
                
                { "correct": "craftsman", "distractors": ["crafsment", "craftsmen", "craftman"], "translation": "工匠;手艺人;匠人" },
                
                { "correct": "quarry", "distractors": ["quary", "qurry", "quarryy"], "translation": "采石场;猎物;挖出;苦心找出" },
                { "correct": "cottage", "distractors": ["catage", "cottige", "cottgae"], "translation": "村舍;小屋;小别墅" },
                
                { "correct": "engine room", "distractors": ["engineer", "engineroom", "engine rum"], "translation": "发动机舱；机舱" },
                { "correct": "steam engine", "distractors": ["sti", "steam engin", "steem engine"], "translation": "蒸汽机" },
                { "correct": "infirmary", "distractors": ["infermary", "infirmery", "infimary"], "translation": "医院;医务室" },
                { "correct": "wrist", "distractors": ["rist", "wrists", "wristt"], "translation": "手腕;腕关节" },
                
                
                { "correct": "insomnia", "distractors": ["insomia", "insomnea", "insomniya"], "translation": "失眠（症）" },
                { "correct": "pulse", "distractors": ["pouse", "pluse", "pulss"], "translation": "脉冲;脉搏;搏动" },
                { "correct": "diabetic", "distractors": ["diabetiv", "diabettic", "diabatic"], "translation": "糖尿病的;适合糖尿病患者的" },
                { "correct": "remedy", "distractors": ["ramedy", "remidy", "remedey"], "translation": "疗法;纠正办法;纠正;治疗" },
                { "correct": "therapy", "distractors": ["thearapy", "theraphy", "therpy"], "translation": "治疗;疗法" },
                { "correct": "acupuncture", "distractors": ["accupancture", "acupunture", "acupuntcure"], "translation": "针刺疗法;对…施行针刺疗法" },
                { "correct": "prescribe", "distractors": ["perscribe", "prescrib", "prescripbe"], "translation": "开药方;规定" },
                { "correct": "pharmacy", "distractors": ["farmercy", "pharmasy", "pharamcy"], "translation": "药房;药剂学" },
                { "correct": "vaccinate", "distractors": ["vacacinate", "vacinatte", "vaccinatee"], "translation": "接种疫苗;预防接种" },
                { "correct": "painkiller", "distractors": ["pain killer", "pankiller", "painkiler"], "translation": "止痛药" },
                { "correct": "aspirin", "distractors": ["asiprin", "aspirinr", "asprin"], "translation": "阿司匹林" },
                
                { "correct": "side effect", "distractors": ["sidifect", "side afect", "sideefffect"], "translation": "副作用；意外的附带结果" },
                
                { "correct": "sneeze", "distractors": ["snees", "snezee", "sneese"], "translation": "喷嚏;打喷嚏" },
                
                
                
                { "correct": "dwellings", "distractors": ["duwllings", "dwelings", "dwellinges"], "translation": "住处；住宅" },
                { "correct": "pottery", "distractors": ["potery", "pottry", "poterry"], "translation": "陶器;陶土;制陶手艺" },
                { "correct": "eyesight", "distractors": ["eyesite", "eyesigh", "eyesights"], "translation": "视力;视觉" },
                { "correct": "vision", "distractors": ["vasion", "vission", "vison"], "translation": "视野;视力;想象;幻象" },
                { "correct": "sting", "distractors": ["stin", "stinng", "stingg"], "translation": "刺;刺痛" },
                { "correct": "pest", "distractors": ["past", "pestt", "pext"], "translation": "害虫；有害动物；讨厌的人" },
                { "correct": "vitamin", "distractors": ["vatamin", "vitaman", "vitimin"], "translation": "维生素;维他命" },
                { "correct": "metal", "distractors": ["matal", "metel", "metall"], "translation": "金属" },
                
                { "correct": "endangered", "distractors": ["indangered", "endagered", "endangerd"], "translation": "濒临灭绝的" },
                { "correct": "infect", "distractors": ["infact", "infectt", "inffect"], "translation": "传染;感染" },
                { "correct": "toxin", "distractors": ["toxi", "toxine", "toxinr"], "translation": "毒素;毒质" },
                { "correct": "survival", "distractors": ["servival", "survivel", "survial"], "translation": "生存;存活;幸存" },
                { "correct": "digest", "distractors": ["dygest", "diggest", "digesst"], "translation": "摘要;消化;领会" },
                { "correct": "tongue", "distractors": ["touge", "tounge", "tonguee"], "translation": "舌头;语言" },
                { "correct": "conservation", "distractors": ["concervation", "conser vation", "conservasion"], "translation": "保护;保存;节约" },
                { "correct": "territory", "distractors": ["taritory", "terretory", "territery"], "translation": "领土;领域" },
                { "correct": "inhabit", "distractors": ["in habit", "inhabite", "inhbit"], "translation": "居住于;栖息" },
                { "correct": "habitat", "distractors": ["habitate", "habbitat", "habitatte"], "translation": "栖息地;居留地;产地" },
                { "correct": "amphibian", "distractors": ["anthebian", "amphiban", "amphibien"], "translation": "两栖动物" },
                
                { "correct": "steering wheel", "distractors": ["stearingwheel", "steering wheal", "steerng wheel"], "translation": "方向盘" },
                { "correct": "instrument panel", "distractors": ["instrumentpanal", "instrument pannel", "instrumen panel"], "translation": "仪表板" },
                { "correct": "mileage", "distractors": ["miledge", "milage", "milege"], "translation": "英里里程;英里数" },
                { "correct": "engine size", "distractors": ["engineecize", "engine sizee", "engin size"], "translation": "发动机排量" },
                { "correct": "auditorium", "distractors": ["orditoriam", "auditoriam", "auditorum"], "translation": "礼堂;听众席" },
                { "correct": "cloakroom", "distractors": ["clorkroom", "clockroom", "cloakrom"], "translation": "衣帽间;厕所" },
                { "correct": "escalator", "distractors": ["exalator", "escelator", "escalater"], "translation": "自动扶梯" },
                { "correct": "foyer", "distractors": ["foya", "foyyer", "foier"], "translation": "门厅;休息室" },
                { "correct": "ceiling", "distractors": ["siling", "ceilling", "cealin g"], "translation": "天花板" },
                { "correct": "sculpture", "distractors": ["scopture", "sculputre", "sclupture"], "translation": "雕刻（术）;雕塑品" },
                { "correct": "exterior", "distractors": ["exduera", "exterier", "exteriorr"], "translation": "外观;外部的" },
                { "correct": "refurbish", "distractors": ["referbish", "refurbrish", "refurbsh"], "translation": "翻新;整修" },
                { "correct": "reconstruct", "distractors": ["reconstract", "reconstuct", "recontruct"], "translation": "重建;重现" },
                { "correct": "demolition", "distractors": ["demilation", "demoliton", "demolision"], "translation": "摧毁;拆除" },
                
                { "correct": "concert hall", "distractors": ["concin", "concert halll", "consert hall"], "translation": "音乐厅；演奏厅" },
                { "correct": "venue", "distractors": ["veniue", "veneu", "vennue"], "translation": "举办地点;会场" },
                
                { "correct": "footpath", "distractors": ["footpass", "footpth", "footpathh"], "translation": "人行道;小路" },
                { "correct": "pavement", "distractors": ["payment", "pavemant", "pavment"], "translation": "路面;人行道" },
                
                { "correct": "erect", "distractors": ["irrect", "ereckt", "erec t"], "translation": "直立的;竖立;建立" },
                { "correct": "crossroads", "distractors": ["cross roads", "crossroades", "crossroad"], "translation": "十字路口" },
                { "correct": "traffic congestion", "distractors": ["traffic conjustion", "traffic congession", "trafic congestion"], "translation": "交通拥堵" },
                
                
                


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
            const correctListInput = document.getElementById('correct-list');
            const saveListBtn = document.getElementById('save-list-btn');
            const playAudioBtn = document.getElementById('play-audio-btn');
            const revealcorrectBtn = document.getElementById('reveal-correct-btn');
            const correctText = document.getElementById('correct-text');
            const prevcorrectBtn = document.getElementById('prev-correct-btn');
            const nextcorrectBtn = document.getElementById('next-correct-btn');
            const correctCounter = document.getElementById('correct-counter');
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
                correctText.textContent = correctList[currentcorrectIndex];
                correctText.classList.add('invisible');
                correctCounter.textContent = `${currentcorrectIndex + 1} / ${correctList.length}`;
            };

            const savecorrectList = () => {
                const corrects = correctListInput.value.split(',')
                    .map(correct => correct.trim())
                    .filter(correct => correct.length > 0);
                if (corrects.length > 0) {
                    correctList = corrects;
                    currentcorrectIndex = 0;
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

            const checkAntonymAnswer = (selectedcorrect) => {
                const buttons = antonymChoicesContainer.querySelectorAll('button');
                buttons.forEach(btn => {
                    btn.disabled = true;
                    if (btn.textContent === currentAntonymQuestion.a) {
                        btn.classList.add('correct');
                    } else if (btn.textContent === selectedcorrect) {
                        btn.classList.add('incorrect');
                    }
                });
                
                if (selectedcorrect === currentAntonymQuestion.a) {
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

            const checkPronunciationAnswer = (selectedcorrect) => {
                 const buttons = pronunciationChoicesContainer.querySelectorAll('button');
                buttons.forEach(btn => {
                    btn.disabled = true;
                    if (btn.textContent === currentPronunciationQuestion.correct) {
                        btn.classList.add('correct');
                    } else if (btn.textContent === selectedcorrect) {
                        btn.classList.add('incorrect');
                    }
                });
                
                if (selectedcorrect === currentPronunciationQuestion.correct) {
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
                speak(correctList[currentcorrectIndex]);
            });

            revealcorrectBtn.addEventListener('click', () => {
                flashcardInstruction.classList.add('hidden');
                correctText.classList.remove('invisible');
            });

            nextcorrectBtn.addEventListener('click', () => {
                currentcorrectIndex = (currentcorrectIndex + 1) % correctList.length;
                updateFlashcardView();
            });

            prevcorrectBtn.addEventListener('click', () => {
                currentcorrectIndex = (currentcorrectIndex - 1 + correctList.length) % correctList.length;
                updateFlashcardView();
            });

            saveListBtn.addEventListener('click', savecorrectList);

            // Pronunciation game listener
            playPronunciationAudioBtn.addEventListener('click', () => {
                speak(currentPronunciationQuestion.correct);
            });


            // --- INITIALIZATION ---
            correctListInput.value = correctList.join(', ');
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
