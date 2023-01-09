function DropdownMenu() {
    document.getElementById("myDropdown").classList.toggle("show");
    document.getElementById("myDropdown").onclick = onClick
  }

  
  function onClick(event) {
      console.log(2);
    if (!event.target.matches('.FilterButton')) {
      console.log(3);
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }