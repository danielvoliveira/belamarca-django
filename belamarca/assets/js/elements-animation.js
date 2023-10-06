$(document).ready(function() {
    // Function to check if an element is in the viewport
    function isElementInViewport(element) {
        var rect = element.getBoundingClientRect();
    var windowHeight = window.innerHeight || document.documentElement.clientHeight;

    // Calculate the vertical midpoint of the viewport
    var viewportMidpoint = windowHeight / 3;

    // Calculate the vertical midpoint of the element
    var elementMidpoint = (rect.top + rect.bottom) / 3;

    // Check if the element's midpoint is within the viewport's midpoint
    return Math.abs(elementMidpoint - viewportMidpoint) < windowHeight / 3;
    }

    // Function to add animation class to elements when they are in the viewport
    function addAnimationClass() {
        var elements = document.querySelectorAll('.animation-container .animate-element');
        elements.forEach(function(element) {
            if (isElementInViewport(element)) {
                element.classList.add('animate__animated', 'animate__fadeIn'); // Add your desired animation classes here
            }
        });
    }

    // Initial check and add animation class if elements are in the viewport on page load
    addAnimationClass();

    // Check and add animation class on scroll
    window.addEventListener('scroll', addAnimationClass);


    /* Função de animação para ser usada na página de produto */

    // Function to check if an element is in the viewport
    function isElementInViewportFaster(element) {
        var rect = element.getBoundingClientRect();
    var windowHeight = window.innerHeight || document.documentElement.clientHeight;

    // Calculate the vertical midpoint of the viewport
    var viewportMidpoint = windowHeight / 3;

    // Calculate the vertical midpoint of the element
    var elementMidpoint = (rect.top + rect.bottom) / 3;

    // Check if the element's midpoint is within the viewport's midpoint
    return Math.abs(elementMidpoint - viewportMidpoint) < windowHeight / 2;
    }

    // Function to add animation class to elements when they are in the viewport
    function addAnimationClassFaster() {
        var elements = document.querySelectorAll('.animation-container-faster .animate-element-faster');
        elements.forEach(function(element) {
            if (isElementInViewportFaster(element)) {
                element.classList.add('animate__animated', 'animate__fadeIn'); // Add your desired animation classes here
            }
        });
    }

    // Initial check and add animation class if elements are in the viewport on page load
    addAnimationClassFaster();

    // Check and add animation class on scroll
    window.addEventListener('scroll', addAnimationClassFaster);
});