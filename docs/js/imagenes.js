document.addEventListener("DOMContentLoaded", function() {
  let preview = document.getElementById("preview");
  let content = document.getElementById("preview-content");

  if (preview) {
    // permite cerrar el modal.
    preview.addEventListener("click", function() {
      preview.classList.toggle("dn");
      preview.classList.toggle("flex");
    });

    // conecta el click sobre las imágenes para que se abra el modal.
    let imagenes = document.querySelectorAll(".post-content img");

    imagenes.forEach(function(imagen) {

      if (imagen.hasAttribute("x-sin-click")) {
        return;
      }

      imagen.classList.add("pointer");

      imagen.addEventListener("click", function() {
        preview.classList.toggle("dn");
        preview.classList.toggle("flex");

        content.innerHTML = `<img src=${this.src}>`;
      });
    });
  }
});
