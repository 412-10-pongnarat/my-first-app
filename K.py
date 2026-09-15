<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>เกมคำศัพท์เกาหลี หมวดร้านอาหาร 🇰🇷🍲</title>
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;600&family=Noto+Sans+KR:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <div class="game-container">
        <header>
            <h1>🍱 Korean Diner Quiz 🇰🇷</h1>
            <p>เกมทายคำศัพท์เกาหลี หมวดร้านอาหาร & อาหาร</p>
        </header>

        <div class="score-board">
            <span>คะแนน: <strong id="score">0</strong></span>
            <span>ข้อที่: <strong id="current-question">1</strong>/<span id="total-questions">0</span></span>
        </div>

        <div id="quiz-box" class="quiz-card">
            <div class="korean-word" id="korean-word">คำศัพท์</div>
            <div class="pronunciation" id="pronunciation">(คำอ่าน)</div>
            <div class="options-container" id="options-container">
                <!-- ตัวเลือกจะถูกสร้างด้วย JavaScript -->
            </div>
        </div>

        <div id="result-box" class="result-card hidden">
            <h2>🎉 จบเกมแล้ว! 🎉</h2>
            <p class="final-score">คะแนนของคุณคือ: <span id="final-score">0</span></p>
            <button onclick="restartGame()" class="btn-restart">เล่นอีกครั้ง 🔄</button>
        </div>
    </div>

    <script src="script.js"></script>
</body>
</html>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: 'Kanit', 'Noto Sans KR', sans-serif;
}

body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 99%, #fecfef 100%);
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
}

.game-container {
    background: white;
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    width: 100%;
    max-width: 450px;
    text-align: center;
}

header h1 {
    color: #d32f2f;
    font-size: 1.8rem;
    margin-bottom: 5px;
}

header p {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 20px;
}

.score-board {
    display: flex;
    justify-content: space-between;
    background: #fff5f5;
    padding: 10px 15px;
    border-radius: 10px;
    margin-bottom: 20px;
    font-size: 1rem;
    color: #444;
}

.quiz-card {
    background: #fafafa;
    border: 2px dashed #ffcdd2;
    padding: 25px 15px;
    border-radius: 15px;
}

.korean-word {
    font-size: 2.5rem;
    font-weight: bold;
    color: #b71c1c;
    margin-bottom: 5px;
}

.pronunciation {
    color: #757575;
    font-size: 1rem;
    margin-bottom: 25px;
}

.options-container {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.option-btn {
    background: white;
    border: 2px solid #e0e0e0;
    padding: 12px;
    border-radius: 10px;
    font-size: 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
}

.option-btn:hover {
    border-color: #ff5252;
    background: #ffebee;
}

.option-btn.correct {
    background: #4caf50 !important;
    color: white;
    border-color: #4caf50;
}

.option-btn.wrong {
    background: #f44336 !important;
    color: white;
    border-color: #f44336;
}

.btn-restart {
    background: #d32f2f;
    color: white;
    border: none;
    padding: 12px 25px;
    font-size: 1rem;
    border-radius: 10px;
    cursor: pointer;
    margin-top: 15px;
    transition: 0.2s;
}

.btn-restart:hover {
    background: #b71c1c;
}

.hidden {
    display: none;
}
// คลังคำศัพท์เกาหลี หมวดร้านอาหาร
const vocabulary = [
    { word: "메뉴판", reading: "เม-นยู-พัน", correct: "เมนูอาหาร", options: ["เมนูอาหาร", "ใบเสร็จ", "โต๊ะอาหาร", "ตะเกียบ"] },
    { word: "물", reading: "มุล", correct: "น้ำเปล่า", options: ["น้ำเปล่า", "กิมจิ", "ข้าวสวย", "ซุป"] },
    { word: "젓가락", reading: "ช็อด-กา-รัก", correct: "ตะเกียบ", options: ["ช้อน", "ตะเกียบ", "จาน", "แก้วน้ำ"] },
    { word: "숟가락", reading: "ซุด-กา-รัก", correct: "ช้อน", options: ["ตะเกียบ", "ช้อน", "มีด", "ทิชชู่"] },
    { word: "김치", reading: "คิม-ชี", correct: "กิมจิ", options: ["กิมจิ", "ต๊อกโบกี", "บิบิมบับ", "รามยอน"] },
    { word: "삼겹살", reading: "ซัม-กย็อบ-ซัล", correct: "หมูสามชั้น", options: ["เนื้อวัว", "หมูสามชั้น", "ไก่ทอด", "ซี่โครงหมู"] },
    { word: "계산서", reading: "คเย-ซาน-ซอ", correct: "ใบเสร็จ/บิล", options: ["เมนูอาหาร", "ทิชชู่", "ใบเสร็จ/บิล", "บัตรเครดิต"] },
    { word: "이모님", reading: "อี-โม-นิม", correct: "ป้าครับ/ค่ะ (เรียกพนักงาน)", options: ["เจ้าของร้าน", "ป้าครับ/ค่ะ (เรียกพนักงาน)", "เชฟ", "คุณลูกค้า"] },
    { word: "공기밥", reading: "คง-กี-บับ", correct: "ข้าวสวย", options: ["ข้าวสวย", "ข้าวผัด", "ข้าวต้ม", "เส้นก๋วยเตี๋ยว"] },
    { word: "맛있어요", reading: "มา-ชิ-ซอ-โย", correct: "อร่อย", options: ["เผ็ด", "เค็ม", "อร่อย", "ไม่อร่อย"] }
];

let currentQuestionIndex = 0;
let score = 0;

const wordEl = document.getElementById('korean-word');
const pronunEl = document.getElementById('pronunciation');
const optionsEl = document.getElementById('options-container');
const scoreEl = document.getElementById('score');
const currentQEl = document.getElementById('current-question');
const totalQEl = document.getElementById('total-questions');
const quizBox = document.getElementById('quiz-box');
const resultBox = document.getElementById('result-box');
const finalScoreEl = document.getElementById('final-score');

totalQEl.textContent = vocabulary.length;

function loadQuestion() {
    const currentQ = vocabulary[currentQuestionIndex];
    wordEl.textContent = currentQ.word;
    pronunEl.textContent = `(${currentQ.reading})`;
    currentQEl.textContent = currentQuestionIndex + 1;
    
    optionsEl.innerHTML = '';
    
    // สลับลำดับตัวเลือก
    const shuffledOptions = [...currentQ.options].sort(() => Math.random() - 0.5);

    shuffledOptions.forEach(option => {
        const button = document.createElement('button');
        button.classList.add('option-btn');
        button.textContent = option;
        button.onclick = () => checkAnswer(button, option, currentQ.correct);
        optionsEl.appendChild(button);
    });
}

function checkAnswer(selectedBtn, selectedAnswer, correctAnswer) {
    const allButtons = optionsEl.querySelectorAll('.option-btn');
    allButtons.forEach(btn => btn.disabled = true); // ป้องกันการกดซ้ำ

    if (selectedAnswer === correctAnswer) {
        selectedBtn.classList.add('correct');
        score++;
        scoreEl.textContent = score;
    } else {
        selectedBtn.classList.add('wrong');
        // แสดงคำตอบที่ถูกต้อง
        allButtons.forEach(btn => {
            if (btn.textContent === correctAnswer) {
                btn.classList.add('correct');
            }
        });
    }

    setTimeout(() => {
        currentQuestionIndex++;
        if (currentQuestionIndex < vocabulary.length) {
            loadQuestion();
        } else {
            showResult();
        }
    }, 1200);
}

function showResult() {
    quizBox.classList.add('hidden');
    resultBox.classList.remove('hidden');
    finalScoreEl.textContent = `${score} / ${vocabulary.length}`;
}

function restartGame() {
    currentQuestionIndex = 0;
    score = 0;
    scoreEl.textContent = score;
    resultBox.classList.add('hidden');
    quizBox.classList.remove('hidden');
    loadQuestion();
}

// เริ่มเกมครั้งแรก
loadQuestion();
