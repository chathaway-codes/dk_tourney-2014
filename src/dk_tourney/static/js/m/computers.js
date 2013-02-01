define(["m/computer", "jquery", "m/models", "backbone-tastypie"], function(computer, $, models) {
    "use strict";

    var datas = models.extend({
        baseUrl: window.API_RAW + "computer/",
        model: computer,
    });

    return datas;
});
