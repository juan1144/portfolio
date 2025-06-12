/* JAVASCRIPT TO RENDER SLIDESHOW */
document.addEventListener("DOMContentLoaded", () => {
  const slideshows = document.querySelectorAll(".slideshow");

  slideshows.forEach(slideshow => {
    const slidesContainer = slideshow.querySelector(".carousel-slides");
    const slides = slidesContainer.querySelectorAll("img");
    const prevBtn = slideshow.querySelector(".prevSlide");
    const nextBtn = slideshow.querySelector(".nextSlide");

    let currentSlide = 0;

    const updateSlide = () => {
      slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
    };

    prevBtn.addEventListener("click", () => {
      currentSlide = (currentSlide - 1 + slides.length) % slides.length;
      updateSlide();
    });

    nextBtn.addEventListener("click", () => {
      currentSlide = (currentSlide + 1) % slides.length;
      updateSlide();
    });
  });
});
