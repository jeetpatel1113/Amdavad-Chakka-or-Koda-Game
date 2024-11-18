const canvas = document.getElementById("game-board");
const context = canvas.getContext("2d");

// Set canvas dimensions
canvas.width = 800; // Width: 800px
canvas.height = 600; // Height: 600px

// Draw the game board background
context.fillStyle = "#e0e0e0";
context.fillRect(0, 0, canvas.width, canvas.height);

// Function to draw grid lines
function drawGrid(cellSize) {
    context.strokeStyle = "#000"; // Line color
    context.lineWidth = 1; // Line width

    // Draw vertical lines
    for (let x = 0; x <= canvas.width; x += cellSize) {
        context.beginPath();
        context.moveTo(x, 0);
        context.lineTo(x, canvas.height);
        context.stroke();
    }

    // Draw horizontal lines
    for (let y = 0; y <= canvas.height; y += cellSize) {
        context.beginPath();
        context.moveTo(0, y);
        context.lineTo(canvas.width, y);
        context.stroke();
    }
}

// Draw a 500x500 colored box on the left side
function drawColoredBox() {
    const boxWidth = 500;
    const boxHeight = 500;
    const boxX = 50; // Leftmost side
    const boxY = (canvas.height - boxHeight) / 2; // Centered vertically

    context.fillStyle = "#add8e6"; // Light blue color
    context.fillRect(boxX, boxY, boxWidth, boxHeight);

    context.strokeStyle = "#000"; // Border color
    context.lineWidth = 2; // Border width
    context.strokeRect(boxX, boxY, boxWidth, boxHeight);
}

// Call the functions
drawColoredBox(); // Draw the colored box
// drawGrid(25); // Draw the grid

// Draw Chakka (disc) on the right side
context.beginPath();
context.arc(750, 300, 40, 0, Math.PI * 2);
context.fillStyle = "#ff6347";
context.fill();
context.strokeStyle = "#000";
context.stroke();
context.closePath();

// Draw tokens
for (let i = 0; i < 3; i++) {
    context.beginPath();
    context.arc(100 + i * 150, 300, 20, 0, Math.PI * 2);
    context.fillStyle = "#4682b4";
    context.fill();
    context.stroke();
    context.closePath();
}
