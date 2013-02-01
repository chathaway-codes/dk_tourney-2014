require(['jquery', 'backbone', 'm/computers',
         'backbone-tastypie'],
    function($, Backbone, computers) {
    "use strict";

    var c = new computers;
    c.fetch();
});
