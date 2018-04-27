const snackbarOptions = {
  style: "snackbar",
  timeout: 500
};

$(document).ready(function() {
  $(".product .btn.add-item").on("click", function() {
    $(this).snackbar(snackbarOptions);
  });
});
