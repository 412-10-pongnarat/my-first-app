<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>เกมเติมคำศัพท์อาหารเกาหลี 🇰🇷</title>

  <style>
    * {
      box-sizing: border-box;
      font-family: "Noto Sans Thai", "Tahoma", sans-serif;
    }

    body {
      margin: 0;
      min-height: 100vh;
      background: linear-gradient(135deg, #fff1f2, #ffe4e6, #fef3c7);
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 20px;
      color: #3f3f46;
    }

    .game {
      width: 100%;
      max-width: 600px;
      background: white;
      border-radius: 28px;
      padding: 30px;
      box-shadow: 0 15px 45px rgba(0, 0, 0, 0.12);
      text-align: center;
    }

    h1 {
      margin-top: 0;
      color: #dc2626;
      font-size: 30px;
    }

    .subtitle {
      color: #71717a;
      margin-bottom: 25px;
    }

    .score-board {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      margin-bottom: 25px;
    }

    .score-box {
      flex: 1;
      background: #fff1f2;
      padding: 12px;
      border-radius: 15px;
      font-weight: bold;
    }

    .question-card {
      background: #fafafa;
      border: 2px solid #f4f4f5;
      border-radius: 22px;
      padding: 30px 20px;
      margin-bottom: 20px;
    }

    .korean {
      font-size: 48px;
      font-weight: bold;
      color: #18181b;
      margin-bottom: 15px;
    }

    .meaning {
      font-size: 20px;
      color: #52525b;
      margin-bottom: 25px;
    }

    .answer-label {
      display: block;
      text-align: left;
      font-weight: bold;
      margin-bottom: 8px;
    }

    input {
      width: 100%;
      padding: 16px;
      border: 2px solid #d4d4d8;
      border-radius: 14px;
      font-size: 20px;
      text-align: center;
      outline: none;
      transition: 0.2s;
    }

    input:focus {
      border-color: #ef4444;
      box-shadow: 0 0 0 4px rgba(239, 68, 68, 0.1);
    }

    button {
      border: none;
      border-radius: 14px;
      padding: 14px 22px;
      font-size: 18px;
      font-weight: bold;
      cursor: pointer;
      transition: 0.2s;
    }

    .check-btn {
      width: 100%;
      margin-top: 15px;
      background: #dc2626;
      color: white;
    }

    .check-btn:hover {
      background: #b91c1c;
      transform: translateY(-2px);
    }

    .next-btn {
      background: #f59e0b;
      color: white;
      margin-top: 15px;
      display: none;
    }

    .next-btn:hover {
      background: #d97706;
    }

    .result {
      min-height: 35px;
      margin-top: 18px;
      font-size: 18px;
      font-weight: bold;
    }

    .correct {
      color: #16a34a;
    }

    .wrong {
      color: #dc2626;
    }

    .answer {
      margin-top: 8px;
      color: #52525b;
      font-weight: normal;
    }

    .progress {
      height: 8px;
      background: #e4e4e7;
      border-radius: 10px;
      overflow: hidden;
      margin-top: 20px;
    }

    .progress-bar {
      height: 100%;
      width: 0%;
      background: #ef4444;
      transition: width 0.3s;
    }

    .restart-btn {
      background: #27272a;
      color: white;
      margin-top: 15px;
      display: none;
    }

    .restart-btn:hover {
      background: #18181b;
    }

    .hint {
      margin-top: 15px;
      color: #a1a1aa;
      font-size: 14px;
    }

    @media (max-width: 500px) {
      .game {
        padding: 20px;
      }

      h1 {
        font-size: 25px;
      }

      .korean {
        font-size: 40px;
      }

      .meaning {
        font-size: 17px;
      }
    }
  </style>
</head>

<body>

  <div class="game">

    <h1>🇰🇷 เกมเติมคำศัพท์อาหารเกาหลี 🍜</h1>

    <div class="subtitle">
      ดูคำศัพท์เกาหลี แล้วพิมพ์คำอ่านภาษาไทย
    </div>

    <div class="score-board">
      <div class="score-box">
        คะแนน<br>
        <span id="score">0</span>
      </div>

      <div class="score-box">
        ข้อที่<br>
        <span id="questionNumber">1</span> / <span id="total">12</span>
      </div>
    </div>

    <div class="question-card">

      <div id="koreanWord" class="korean">
        비빔밥
      </div>

      <div id="meaning" class="meaning">
        ข้าวยำเกาหลี
      </div>

      <label class="answer-label" for="answer">
        ✏️ คำอ่านภาษาไทย
      </label>

      <input
        type="text"
        id="answer"
        placeholder="พิมพ์คำอ่านที่นี่..."
        autocomplete="off"
      >

      <button class="check-btn" id="checkBtn">
        ตรวจคำตอบ ✓
      </button>

      <div id="result" class="result"></div>

      <button class="next-btn" id="nextBtn">
        ข้อถัดไป →
      </button>

    </div>

    <div class="progress">
      <div class="progress-bar" id="progressBar"></div>
    </div>

    <div class="hint">
      💡 ตัวอย่าง: 비빔밥 → พีบิมบับ
    </div>

    <button class="restart-btn" id="restartBtn">
      🔄 เล่นใหม่
    </button>

  </div>


<script>

  // ==============================
  // ข้อมูลคำศัพท์อาหารเกาหลี
  // ==============================

  const vocabulary = [
    {
      korean: "비빔밥",
      thai: "พีบิมบับ",
      meaning: "ข้าวยำเกาหลี"
    },
    {
      korean: "불고기",
      thai: "พุลโกกิ",
      meaning: "เนื้อวัวผัดหรือย่างซีอิ๊วเกาหลี"
    },
    {
      korean: "삼겹살",
      thai: "ซัมกย็อบซัล",
      meaning: "หมูสามชั้นย่าง"
    },
    {
      korean: "볶음밥",
      thai: "บกอึมบับ",
      meaning: "ข้าวผัด"
    },
    {
      korean: "짜장면",
      thai: "จาจังมยอน",
      meaning: "บะหมี่ซอสถั่วดำ"
    },
    {
      korean: "냉면",
      thai: "แนงมยอน",
      meaning: "บะหมี่เย็น"
    },
    {
      korean: "김치찌개",
      thai: "คิมชิชีเก",
      meaning: "แกงกิมจิ"
    },
    {
      korean: "삼계탕",
      thai: "ซัมกเยทัง",
      meaning: "ไก่ตุ๋นโสม"
    },
    {
      korean: "떡볶이",
      thai: "ต็อกโปกกี",
      meaning: "แป้งต็อกผัดซอสเผ็ด"
    },
    {
      korean: "고기",
      thai: "โคกี",
      meaning: "เนื้อสัตว์"
    },
    {
      korean: "치킨",
      thai: "ชิชิน",
      meaning: "ไก่ทอดสไตล์เกาหลี"
    },
    {
      korean: "녹차",
      thai: "นกชา",
      meaning: "ชาเขียว"
    }
  ];


  // ==============================
  // ตัวแปรของเกม
  // ==============================

  let questions = [];
  let currentQuestion = 0;
  let score = 0;
  let answered = false;


  // ==============================
  // DOM
  // ==============================

  const koreanWord = document.getElementById("koreanWord");
  const meaning = document.getElementById("meaning");
  const answer = document.getElementById("answer");
  const result = document.getElementById("result");

  const scoreText = document.getElementById("score");
  const questionNumber = document.getElementById("questionNumber");
  const total = document.getElementById("total");

  const checkBtn = document.getElementById("checkBtn");
  const nextBtn = document.getElementById("nextBtn");
  const restartBtn = document.getElementById("restartBtn");
  const progressBar = document.getElementById("progressBar");


  // ==============================
  // สุ่มคำถาม
  // ==============================

  function shuffle(array) {
    return [...array].sort(() => Math.random() - 0.5);
  }


  // ==============================
  // เริ่มเกม
  // ==============================

  function startGame() {

    questions = shuffle(vocabulary);

    currentQuestion = 0;
    score = 0;

    scoreText.textContent = score;
    total.textContent = questions.length;

    restartBtn.style.display = "none";

    loadQuestion();
  }


  // ==============================
  // โหลดคำถาม
  // ==============================

  function loadQuestion() {

    answered = false;

    const question = questions[currentQuestion];

    koreanWord.textContent = question.korean;
    meaning.textContent = question.meaning;

    questionNumber.textContent = currentQuestion + 1;

    answer.value = "";
    answer.disabled = false;

    result.innerHTML = "";

    checkBtn.style.display = "block";
    nextBtn.style.display = "none";

    updateProgress();

    answer.focus();
  }


  // ==============================
  // ตรวจคำตอบ
  // ==============================

  function checkAnswer() {

    if (answered) return;

    const userAnswer = answer.value.trim();

    if (userAnswer === "") {
      result.innerHTML = `
        <div class="wrong">
          ⚠️ กรุณาพิมพ์คำตอบก่อน
        </div>
      `;
      return;
    }

    answered = true;

    const correctAnswer = questions[currentQuestion].thai;

    if (normalize(userAnswer) === normalize(correctAnswer)) {

      score++;

      scoreText.textContent = score;

      result.innerHTML = `
        <div class="correct">
          🎉 ถูกต้อง!
        </div>
        <div class="answer">
          ${questions[currentQuestion].korean}
          = ${correctAnswer}
        </div>
      `;

    } else {

      result.innerHTML = `
        <div class="wrong">
          ❌ ยังไม่ถูกนะ
        </div>

        <div class="answer">
          คำตอบที่ถูกคือ
          <strong>${correctAnswer}</strong>
        </div>
      `;
    }

    answer.disabled = true;

    checkBtn.style.display = "none";

    if (currentQuestion < questions.length - 1) {

      nextBtn.style.display = "inline-block";

    } else {

      showFinalScore();

    }
  }


  // ==============================
  // ทำให้การตรวจคำตอบยืดหยุ่นขึ้น
  // ==============================

  function normalize(text) {

    return text
      .toLowerCase()
      .trim()
      .replace(/\s+/g, "");
  }


  // ==============================
  // ข้อถัดไป
  // ==============================

  function nextQuestion() {

    currentQuestion++;

    loadQuestion();
  }


  // ==============================
  // แสดงคะแนนจบเกม
  // ==============================

  function showFinalScore() {

    const percentage =
      Math.round((score / questions.length) * 100);

    let message = "";

    if (percentage === 100) {
      message = "🏆 สุดยอด! จำคำศัพท์ได้ครบทุกคำ!";
    } else if (percentage >= 80) {
      message = "🌟 เก่งมาก! ใกล้เป็นผู้เชี่ยวชาญอาหารเกาหลีแล้ว";
    } else if (percentage >= 50) {
      message = "👍 ทำได้ดี! ลองเล่นอีกครั้งเพื่อจำคำศัพท์ให้แม่นขึ้น";
    } else {
      message = "💪 ลองเล่นอีกครั้ง แล้วจะจำคำศัพท์ได้มากขึ้น!";
    }

    result.innerHTML = `
      <div class="correct">
        🎊 จบเกม!
      </div>

      <div class="answer">
        คุณได้ ${score} / ${questions.length} คะแนน
        (${percentage}%)
        <br><br>
        ${message}
      </div>
    `;

    nextBtn.style.display = "none";
    restartBtn.style.display = "inline-block";
  }


  // ==============================
  // Progress Bar
  // ==============================

  function updateProgress() {

    const progress =
      ((currentQuestion) / questions.length) * 100;

    progressBar.style.width = progress + "%";
  }


  // ==============================
  // ปุ่มต่าง ๆ
  // ==============================

  checkBtn.addEventListener("click", checkAnswer);

  nextBtn.addEventListener("click", nextQuestion);

  restartBtn.addEventListener("click", startGame);


  // กด Enter เพื่อตรวจคำตอบ
  answer.addEventListener("keydown", function(event) {

    if (event.key === "Enter") {

      if (!answered) {
        checkAnswer();
      } else {
        nextQuestion();
      }

    }

  });


  // ==============================
  // เริ่มเกม
  // ==============================

  startGame();

</script>

</body>
</html>
