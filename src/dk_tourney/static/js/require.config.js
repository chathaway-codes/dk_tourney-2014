var jam = {
    "packages": [
        {
            "name": "underscore",
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
        },
        {
            "name": "backbone",
            "location": "js/backbone",
            "main": "backbone.js"
        }
        {
            "name": "backbone-tastypie",
            "location": "js/backbone-tastypie",
            "main": "backbone-tastypie"
        },
    ],
    "version": "0.2.13",
    "shim": {
        "underscore": {
            "exports": "_"
        },
        "backbone": {
            "deps": [
                "jquery",
                "underscore"
            ],
            "exports": "Backbone"
        }
    }
};

if (typeof require !== "undefined" && require.config) {
    require.config({
    "packages": [
        {
            "name": "underscore",
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
        },
        {
            "name": "backbone",
            "location": "js/backbone",
            "main": "backbone.js"
        }
    ],
    "shim": {
        "underscore": {
            "exports": "_"
        },
        "backbone": {
            "deps": [
                "jquery",
                "underscore"
            ],
            "exports": "Backbone"
        }
    }
});
}
else {
    var require = {
    "packages": [
        {
            "name": "underscore",
            "location": "js/underscore",
            "main": "underscore.js"
        },
        {
            "name": "jquery",
            "location": "js/jquery",
            "main": "jquery.js"
        },
        {
            "name": "bootstrap",
            "location": "js/bootstrap"
        },
        {
            "name": "backbone",
            "location": "js/backbone",
            "main": "backbone.js"
        }
    ],
    "shim": {
        "underscore": {
            "exports": "_"
        },
        "backbone": {
            "deps": [
                "jquery",
                "underscore"
            ],
            "exports": "Backbone"
        }
    }
};
}

if (typeof exports !== "undefined" && typeof module !== "undefined") {
    module.exports = jam;
}
