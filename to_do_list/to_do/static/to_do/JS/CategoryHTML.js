$("select[name='id']").change(function() {
     let selected = $(this).find("option:selected").text();
     $("input[name='new_name']").val(selected);
});

$('#select-option').on('change', function () {
    $('#submitChanges').prop('disabled', false);
});

$('#selectOption').on('change', function () {
    $('#submitDeletion').prop('disabled', false);
});

$("#createCategory").on("keyup", stateHandle);

function stateHandle(e) {
  console.log('input value vs. input value.trim()', '"' + e.target.value + '"', '"' + e.target.value.trim() + '"');
  if ($("#createCategory").text() == e.target.value || e.target.value.trim().length == 0) {
    $('#submitCreation').prop('disabled', true);
  }
  else {
      $('#submitCreation').prop('disabled', false);
  }
}
