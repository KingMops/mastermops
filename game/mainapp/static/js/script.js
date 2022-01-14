let navbar = document.querySelector('.navbar');
          document.querySelector('.menutoogle').onclick = () =>{
	        navbar.classList.toggle('active');
	        seacrhForm.classList.remove('active');
              }

          let seacrhForm = document.querySelector('.search-form');
          document.querySelector('.find').onclick = () =>{
	        seacrhForm.classList.toggle('active');
	        navbar.classList.remove('active');
              }
          window.onscroll = () =>{
          	navbar.classList.remove('active');
          	 seacrhForm.classList.remove('active');
          }
document.querySelectorAll('.accordion-container .accordion').forEach(accordion =>{
  accordion.onclick = () =>{
    accordion.classList.toggle('active');
  }
})




  