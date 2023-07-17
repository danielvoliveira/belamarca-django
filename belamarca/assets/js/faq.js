$(document).ready(function(){
  const faqItem = document.getElementsByClassName("faq-item");
  const faqList = document.querySelectorAll("#faq-list");

  function showElement(element) {
    element.classList.add("show");
  }

  function hideElement(element) {
    element.classList.remove("show");
  }
  for (var i = 0; i < faqList.length; i++) {
    faqItem[i].setAttribute("id", i)
    const divContext = faqList[i].querySelector(`#faq-text-${i}`)

    faqItem[i].onclick = function (e) {
      e.preventDefault()
      var image = this.getElementsByTagName('img')[0]
      if(divContext.classList.contains("show")) {
        image.setAttribute("src", "/static/assets/icons/icon-chevron-down-thin.svg");
        hideElement(divContext)
        $(divContext).css('display', 'none');
      } else {
        image.setAttribute("src", "/static/assets/icons/icon-chevron-up-thin.svg");
        showElement(divContext)
        $(divContext).css('display', 'block');
      }
  };
  }
})