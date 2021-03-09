function procesar_theme() {
  const getTheme = window.localStorage && window.localStorage.getItem("theme");
  const isDark = getTheme === "dark";

  if (getTheme !== null) {
    document.body.classList.toggle("dark-theme", isDark);
  }

  document.addEventListener("DOMContentLoaded", function() {
    const themeToggle = document.querySelector(".theme-toggle");
    themeToggle.addEventListener("click", () => {
      document.body.classList.toggle("dark-theme");
      window.localStorage &&
        window.localStorage.setItem(
          "theme",
          document.body.classList.contains("dark-theme") ? "dark" : "light"
        );
    });
  });
}
