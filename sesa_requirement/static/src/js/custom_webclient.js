openerp.sesa_requirement = function (instance) {
    var WebClient = instance.web.WebClient;

    WebClient.include({
        init: function (parent, client_options) {
            this._super(parent, client_options);
            // Your custom initialization code here
            this.set('title_part', { "zopenerp": "" });
        },
    });
};

$(document).ready(function () {
    $(document).on('keydown', 'input[type="text"], textarea, .o_field_many2one input', function(event) {
        if (event.which === 13) {
            event.preventDefault();

            var inputs = $('input[type="text"], textarea, .o_field_many2one input').filter(':visible:not([readonly]):not(:disabled)');
            var index = inputs.index(this);
            if (index < inputs.length - 1) {
                inputs.eq(index + 1).focus().select();
            } else {
                inputs.eq(0).focus().select();
            }
        }
    });
});
