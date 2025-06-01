document.addEventListener("DOMContentLoaded", function () {
    const formElements = document.querySelectorAll("input, select");

    formElements.forEach(element => {
        element.addEventListener("focus", () => {
            element.style.transform = "scale(1.05)";
        });

        element.addEventListener("blur", () => {
            element.style.transform = "scale(1)";
        });
    });

    // Background Animation Effect
    let background = document.querySelector(".background");
    document.addEventListener("mousemove", (event) => {
        let moveX = (event.clientX / window.innerWidth) * 50;
        let moveY = (event.clientY / window.innerHeight) * 50;
        background.style.backgroundPosition = `${moveX}px ${moveY}px`;
    });
});
