$(document).ready(function(){

    $('#updateTableItemForm').submit(function(e) {
        e.preventDefault();

        var serializedData = {'csrfmiddlewaretoken': this.querySelector('[name="csrfmiddlewaretoken"]').value}
        serializedData['update_table_id'] = document.querySelector('[id="update_table_id"]').value
        serializedData['update_item_name'] = document.querySelector('[id="update_item_name"]').value
        serializedData['update_item_name_pk'] = document.querySelector('[id="update_item_name_pk"]').value

        $.ajax({
            url: $('updateTableItemForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('body').load(window.location.href);
            }
        })
    });

    $('.checkArea').on('click', function(e){
        e.preventDefault();

        var update_table_id = this.querySelector('[name="update_table_id"]').value;
        var update_item_name = this.querySelector('[name="update_item_name"]').value;
        var update_item_name_pk = this.querySelector('[name="update_item_name_pk"]').value;

        document.querySelector('[id="update_table_id"]').value = update_table_id;
        document.querySelector('[id="update_item_name"]').value = update_item_name;
        document.querySelector('[id="update_item_name_pk"]').value = update_item_name_pk;

        $('#updateTableItemForm').submit()
    });

    $('.deleteTableItem').submit(function(e) {
        e.preventDefault();

        var serializedData = $('.deleteTableItem').serialize();

        $.ajax({
            url: $('createGroupForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('body').load(window.location.href);
            }
        })
    });

    $('.deleteTable').submit(function(e) {
        e.preventDefault();

        var serializedData = $('.deleteTable').serialize();

        $.ajax({
            url: $('createGroupForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('body').load(window.location.href);
            }
        })
    });

    $('#confirmPasswordForm').submit(function(e) {
        e.preventDefault();

        var serializedData = $('#confirmPasswordForm').serialize();

        $.ajax({
            url: $('confirmPasswordForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                if (response.includes('Wrong password!') || response.includes('Password field is empty!')) {
                    document.getElementById('error-message').innerText = response;
                    document.getElementById('error-message').style.visibility = 'visible';
                } else {
                    document.getElementById('error-message').style.visibility = 'hidden';
                    window.location.href = 'http://127.0.0.1:8000' + response;
                }
            }
        });
    });

    $('#createGroupForm').submit(function(e) {
        e.preventDefault();

        var serializedData = $('#createGroupForm').serialize();

        $.ajax({
            url: $('createGroupForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('body').load(window.location.href);
            }
        })
    });

    $('#createTaskForm').submit(function(e) {
        e.preventDefault();

        var serializedData = $('#createTaskForm').serialize();

        $.ajax({
            url: $('createTaskForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function (response) {
                $('body').load(window.location.href);
            }
        })
    });
});