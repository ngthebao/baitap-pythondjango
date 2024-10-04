const sidebarToggle = document.querySelector("#sidebar-toggle");
sidebarToggle.addEventListener("click",function(){
    document.querySelector("#sidebar").classList.toggle("collapsed");
});

document.querySelector(".theme-toggle").addEventListener("click",() => {
    toggleLocalStorage();
    toggleRootClass();
});

function toggleRootClass(){
    const current = document.documentElement.getAttribute('data-bs-theme');
    const inverted = current == 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-bs-theme',inverted);
}

function toggleLocalStorage(){
    if(isLight()){
        localStorage.removeItem("light");
    }else{
        localStorage.setItem("light","set");
    }
}

function isLight(){
    return localStorage.getItem("light");
}

if(isLight()){
    toggleRootClass();
}

$(document).ready(function() {
    $('.pagination').twbsPagination({
      totalPages: $('table').data('total-pages'),
      visiblePages: 5,
      onPageClick: function (event, page) {
        // Gửi yêu cầu AJAX đến server để lấy dữ liệu cho trang `page`
        // Hiển thị dữ liệu lên bảng
      }
    });
  });

  $(document).ready(function() {
    $('.pagination').twbsPagination({
      totalPages: $('table').data('total-pages'),
      visiblePages: 5,
      onPageClick: function (event, page) {
        $.ajax({
          url: '/api/students/page/' + page,
          method: 'GET',
          success: function (data) {
            // Hiển thị dữ liệu lên bảng
          }
        });
      }
    });
  });
  
  