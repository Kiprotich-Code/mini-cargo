(function () {
  "use strict";

  /**
   * Apply .scrolled class to the body as the page is scrolled down
   */
  function toggleScrolled() {
    const selectBody = document.querySelector('body');
    const selectHeader = document.querySelector('#header');
    if (!selectHeader.classList.contains('scroll-up-sticky') && !selectHeader.classList.contains('sticky-top') && !selectHeader.classList.contains('fixed-top')) return;
    window.scrollY > 100 ? selectBody.classList.add('scrolled') : selectBody.classList.remove('scrolled');
  }

  document.addEventListener('scroll', toggleScrolled);
  window.addEventListener('load', toggleScrolled);

  /**
   * Mobile nav toggle
   */
  const mobileNavToggleBtn = document.querySelector('.mobile-nav-toggle');

  function mobileNavToogle() {
    document.querySelector('body').classList.toggle('mobile-nav-active');
    mobileNavToggleBtn.classList.toggle('bi-list');
    mobileNavToggleBtn.classList.toggle('bi-x');
  }
  mobileNavToggleBtn.addEventListener('click', mobileNavToogle);

  /**
   * Hide mobile nav on same-page/hash links
   */
  document.querySelectorAll('#navmenu a').forEach(navmenu => {
    navmenu.addEventListener('click', () => {
      if (document.querySelector('.mobile-nav-active')) {
        mobileNavToogle();
      }
    });

  });

  /**
   * Toggle mobile nav dropdowns
   */
  document.querySelectorAll('.navmenu .toggle-dropdown').forEach(navmenu => {
    navmenu.addEventListener('click', function (e) {
      e.preventDefault();
      this.parentNode.classList.toggle('active');
      this.parentNode.nextElementSibling.classList.toggle('dropdown-active');
      e.stopImmediatePropagation();
    });
  });

  /**
   * Preloader
   */
  const preloader = document.querySelector('#preloader');
  if (preloader) {
    window.addEventListener('load', () => {
      preloader.remove();
    });
  }

  /**
   * Scroll top button
   */
  let scrollTop = document.querySelector('.scroll-top');

  function toggleScrollTop() {
    if (scrollTop) {
      window.scrollY > 100 ? scrollTop.classList.add('active') : scrollTop.classList.remove('active');
    }
  }
  scrollTop.addEventListener('click', (e) => {
    e.preventDefault();
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    });
  });

  window.addEventListener('load', toggleScrollTop);
  document.addEventListener('scroll', toggleScrollTop);

  /**
   * Animation on scroll function and init
   */
  function aosInit() {
    AOS.init({
      duration: 600,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    });
  }
  window.addEventListener('load', aosInit);

  /**
   * Initiate Pure Counter
   */
  new PureCounter();

  /**
   * Initiate glightbox
   */
  const glightbox = GLightbox({
    selector: '.glightbox'
  });

  /**
   * Init swiper sliders
   */
  function initSwiper() {
    document.querySelectorAll(".init-swiper").forEach(function (swiperElement) {
      let config = JSON.parse(
        swiperElement.querySelector(".swiper-config").innerHTML.trim()
      );

      if (swiperElement.classList.contains("swiper-tab")) {
        initSwiperWithCustomPagination(swiperElement, config);
      } else {
        new Swiper(swiperElement, config);
      }
    });
  }

  window.addEventListener("load", initSwiper);

  /**
   * Frequently Asked Questions Toggle
   */
  document.querySelectorAll('.faq-item h3, .faq-item .faq-toggle').forEach((faqItem) => {
    faqItem.addEventListener('click', () => {
      faqItem.parentNode.classList.toggle('faq-active');
    });
  });

})();

// 'DOMContentLoaded', 
// STEPPER 
document.addEventListener('DOMContentLoaded', () => {
  const trackButton = document.getElementById('track-btn');
  const trackingInput = document.getElementById('tracking-id-input');

  trackButton?.addEventListener('click', () => {
    const trackingId = trackingInput?.value;

    if (trackingId) {
      fetch(`/track-shipment/?tracking_no=${trackingId}`)
        .then(response => response.json())
        .then(data => {
          const status = data?.status;
          if (status) {
            updateStepper(status);
          } else {
            console.error('No status found in the response.');
          }
        })
        .catch(error => console.error('Error:', error));
    } else {
      alert('Please enter a tracking ID.');
    }
  });
});


function updateStepper(status) {
  const stepperContainer = document.getElementById('stepper-container');
  let stepperHTML = `
      <div class="stepper">
          <div class="step ${status === 'Picked Up' || status === 'Processing' || status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-cube"></i></div>
              <p>Picked Up</p>
          </div>
          <div class="step ${status === 'Processing' || status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-cogs"></i></div>
              <p>Processing</p>
          </div>
          <div class="step ${status === 'In Transit' || status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-truck"></i></div>
              <p>In Transit</p>
          </div>
          <div class="step ${status === 'On Hold' || status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-pause"></i></div>
              <p>On Hold</p>
          </div>
          <div class="step ${status === 'Delivered' ? 'completed' : ''}">
              <div class="circle"><i class="fa fa-check-circle"></i></div>
              <p>Delivered</p>
          </div>
      </div>
  `;
  stepperContainer.innerHTML = stepperHTML;
}
