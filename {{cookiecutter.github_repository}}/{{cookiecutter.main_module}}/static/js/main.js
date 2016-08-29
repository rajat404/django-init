// Add your javascript code here.
{%- if cookiecutter.add_webpack.lower() == 'y' %}
require("../css/normalize.css");
require("../css/main.css");
{%- endif %}
