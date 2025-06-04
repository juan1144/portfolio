/* JAVASCRIPT TO RENDER SLIDESHOW */
document.addEventListener("DOMContentLoaded", () => {
  const slidesContainer = document.querySelector(".carousel-slides");
  const slides = slidesContainer.querySelectorAll("img");
  const totalSlides = slides.length;

  let currentSlide = 0;

  const updateSlide = () => {
    slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
  };

  document.getElementById("prevSlide").addEventListener("click", () => {
    currentSlide = (currentSlide - 1 + totalSlides) % totalSlides;
    updateSlide();
  });

  document.getElementById("nextSlide").addEventListener("click", () => {
    currentSlide = (currentSlide + 1) % totalSlides;
    updateSlide();
  });
});
