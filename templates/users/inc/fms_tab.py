

<div class="table-responsive p-0">
    <table class="table align-items-center mb-3">
        <thead>
            <tr>
                <th><strong>Prueba</strong></th>
                <th><strong>Puntuación Parcial</strong></th>
                <th><strong>Observaciones</strong></th>
            </tr>
        </thead>
        <tbody>
            {% for test in fms %}
                {% if 'sentadilla_' in test.test_slug  %}
                <tr>
                    {% include '../inc/fms_table_items.py' with test=test %}
                </tr>

                {% elif 'paso_iz' in test.test_slug %}
                <tr>
                    {% include '../inc/fms_table_items.py' with test=test %}
                </tr>
                {% elif 'paso_der' in test.test_slug %}
                <tr>
                    {% include '../inc/fms_table_items.py' with test=test %}
                </tr>
                {% endif %}
            {% endfor %}
        </tbody>
    </table>
</div>
