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