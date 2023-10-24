Shery.textAnimate(".first" /* Element to target.*/, {
  //Parameters are optional.
  style: 2,
  y: 10,
  delay: 0.1,
  duration: 2,
  ease: "cubic-bezier(0.23, 1, 0.320, 1)",
  // multiplier: 0.1,
});

// contest slider

var swiper = new Swiper(".mySwiper", {
  cssMode: true,
  navigation: {
    nextEl: ".slider-prev",
    prevEl: ".slider-next",
  },
  pagination: {
    el: ".swiper-pagination",
  },
  mousewheel: true,
  keyboard: true,
});

var contestSwiper = new Swiper(".contestSlider", {
    slidesPerView: 3,
    spaceBetween: 30,
    navigation: {
        nextEl: ".slider-prev",
        prevEl: ".slider-next",
      },
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });