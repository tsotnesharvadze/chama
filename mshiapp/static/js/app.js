(function(w, d) {
    var app = {
        init: function()
        {
            this.loadElements();
            this.bindEvents();
        },

        loadElements: function()
        {

        },

        bindEvents: function()
        {
            //searchField.addEventListener('keyup', this.onSearchFieldKeyUp, true);
        },

        onSearchBoxKeyUp: function(e)
        {
            var value = this.value.trim().replace(/\s*,\s*/g, ',');

            if (value !== '' && e.keyCode === 13) {
                console.log(value);
                jQuery.ajax({
                    url: '/mshiapp/get/?query=' + value,
                    dataType: 'json',
                    success: function (response)
                    {
                        console.log(response)
                    }
                });
            }
        }
    };

    window.app = app;
})(window, document);