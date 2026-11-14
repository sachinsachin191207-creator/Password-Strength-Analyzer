
const passwordForm = document.getElementById("passwordForm");
const passwordInput = document.getElementById("passwordInput");
const togglePassword = document.getElementById("togglePassword");
const analyzeButton = document.getElementById("analyzeButton");
const resetButton = document.getElementById("resetButton");

const resultsSection = document.getElementById("results");
const errorMessage = document.getElementById("errorMessage");

// Show or hide password
togglePassword.addEventListener("click", function () {
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        togglePassword.textContent = "Hide";
    } else {
        passwordInput.type = "password";
        togglePassword.textContent = "Show";
    }
});

// Display security check results
function displayCheck(label, detected) {
    const item = document.createElement("div");
    item.className = "check-item";

    const status = detected ? "Detected" : "Not detected";

    item.textContent = `${label}: ${status}`;

    return item;
}

// Analyze password
passwordForm.addEventListener("submit", async function (event) {

    event.preventDefault();

    const password = passwordInput.value;

    errorMessage.textContent = "";

    if (!password) {
        errorMessage.textContent = "Please enter a password.";
        return;
    }

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";

    try {

        const response = await fetch("/api/analyze", {
            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                password: password
            })
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.error || "Analysis failed.");
        }

        // Display score
        document.getElementById("score").textContent =
            result.score + "/100";

        document.getElementById("strength").textContent =
            result.strength;

        // Display progress bar
        document.getElementById("progressBar").style.width =
            result.score + "%";

        // Display password details
        document.getElementById("length").textContent =
            result.length;

        document.getElementById("pool").textContent =
            result.character_pool;

        document.getElementById("types").textContent =
            result.character_types;

        document.getElementById("entropy").textContent =
            result.entropy + " bits";

        // Display security checks
        const checksContainer =
            document.getElementById("securityChecks");

        checksContainer.replaceChildren();

        const checks = [
            ["Lowercase Letters", result.lowercase],
            ["Uppercase Letters", result.uppercase],
            ["Numbers", result.digits],
            ["Special Characters", result.special],
            ["Common Password", result.is_common],
            ["Repeated Characters", result.repeated],
            ["Predictable Pattern", result.has_pattern]
        ];

        checks.forEach(function (check) {
            checksContainer.appendChild(
                displayCheck(check[0], check[1])
            );
        });

        // Display recommendations
        const recommendationsList =
            document.getElementById("recommendations");

        recommendationsList.replaceChildren();

        if (result.recommendations.length === 0) {

            const item = document.createElement("li");
            item.textContent = "No improvement suggestions.";
            recommendationsList.appendChild(item);

        } else {

            result.recommendations.forEach(function (recommendation) {

                const item = document.createElement("li");
                item.textContent = recommendation;

                recommendationsList.appendChild(item);
            });
        }

        // Show results
        resultsSection.classList.remove("hidden");

        resultsSection.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        errorMessage.textContent = error.message;

    } finally {

        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Password";
    }
});

// Reset analyzer
resetButton.addEventListener("click", function () {

    passwordForm.reset();

    passwordInput.type = "password";
    togglePassword.textContent = "Show";

    resultsSection.classList.add("hidden");

    errorMessage.textContent = "";

    passwordInput.focus();
});
