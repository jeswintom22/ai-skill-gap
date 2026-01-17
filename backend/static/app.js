const form = document.getElementById("analyzeForm");
const result = document.getElementById("result");
const output = document.getElementById("output");
const loading = document.getElementById("loading");
const submitBtn = form.querySelector("button");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  loading.classList.remove("hidden");
  submitBtn.disabled = true;

  const file = document.getElementById("resume").files[0];
  const jobDesc = document.getElementById("jobDesc").value;

  const formData = new FormData();
  formData.append("resume", file);
  formData.append("job_description", jobDesc);

  const res = await fetch("/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();

 output.innerHTML = `
  <div class="result-grid">
    <div class="metric">
      <span>Readiness Score</span>
      <strong>${data.analysis.readiness_score}%</strong>
    </div>

    <div class="metric">
      <span>Missing Skills</span>
      <strong>${data.analysis.missing_skills.join(", ")}</strong>
    </div>
  </div>

  <h3>30-Day Learning Roadmap</h3>
  ${renderRoadmap(data.ai_roadmap)}
`;

  loading.classList.add("hidden");
  submitBtn.disabled = false;
  result.classList.remove("hidden");
});

function renderRoadmap(roadmapText) {
  // 1️⃣ Split text whenever "Week <number>" appears
  const weeks = roadmapText
    .split(/Week\s\d+/)
    .filter(part => part.trim() !== "");

  // 2️⃣ Convert each week into a card
  return weeks.map((content, index) => {
    return `
      <div class="roadmap-card">
        <h4>Week ${index + 1}</h4>
        <p>${content.trim()}</p>
      </div>
    `;
  }).join("");
}