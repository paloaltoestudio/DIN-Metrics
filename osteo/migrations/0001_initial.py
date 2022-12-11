# Generated by Django 4.1 on 2022-08-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Osteo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pain', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Dolor')),
                ('resting', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='En reposo')),
                ('moving', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='En movimiento')),
                ('on_palpitation', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='A la palpación')),
                ('zone', models.CharField(blank=True, max_length=30, verbose_name='Zona')),
                ('intensity', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Intensidad')),
                ('superficial_sensitivity', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Sensibilidad superficial')),
                ('deep_sensitivity', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Sensibilidad profunda')),
                ('inflammation', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Inflamación')),
                ('edema', models.CharField(blank=True, choices=[('NR', 'No Refiere'), ('C', 'Conservado'), ('A', 'Alterado'), ('NE', 'No Evaluado')], max_length=2, verbose_name='Edema')),
                ('pectoralis_minor_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Pectoral menor - Izquierdo')),
                ('pectoralis_minor_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Pectoral menor - Derecho')),
                ('pectoralis_major_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Pectoral mayor - Izquierdo')),
                ('pectoralis_major_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Pectoral mayor - Derecho')),
                ('shoulder_internal_rotator_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Rotador interno de hombro - Izquierdo')),
                ('shoulder_internal_rotator_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Rotador interno de hombro - Derecho')),
                ('shoulder_external_rotator_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Rotador externo de hombro - Izquierdo')),
                ('shoulder_external_rotator_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Rotador externo de hombro - Derecho')),
                ('psoas_iliaco_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='PSOAS ilíaco - Izquierdo')),
                ('psoas_iliaco_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='PSOAS ilíaco - Derecho')),
                ('hip_adductors_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Aductores de cadera - Izquierdo')),
                ('hip_adductors_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Aductores de cadera - Derecho')),
                ('tensioner_fascia_liata_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Tensor de la fascia lata - Izquierdo')),
                ('tensioner_fascia_liata_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Tensor de la fascia lata - Derecho')),
                ('low_spinal_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Espinales bajos - Izquierdo')),
                ('low_spinal_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Espinales bajos - Derecho')),
                ('hamstrings_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Isquitibiales - Izquierdo')),
                ('hamstrings_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Isquitibiales - Derecho')),
                ('quadriceps_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Cuadriceps - Izquierdo')),
                ('quadriceps_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Cuadriceps - Derecho')),
                ('achilles_tendon_l', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Tendón de Aquiles - Izquierdo')),
                ('achilles_tendon_r', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Tendón de Aquiles - Derecho')),
                ('spine_lumbar', models.CharField(blank=True, choices=[('L', 'Leve'), ('M', 'Moderada'), ('S', 'Severa'), ('NE', 'No evaluado'), ('NR', 'No retracción')], max_length=2, verbose_name='Columna vertebral lumbar')),
                ('real_upper_r', models.CharField(blank=True, max_length=10, verbose_name='Miembro superior derecho | Reales')),
                ('real_upper_l', models.CharField(blank=True, max_length=10, verbose_name='Miembro superior izquierdo | Reales')),
                ('real_lower_r', models.CharField(blank=True, max_length=10, verbose_name='Miembro inferior derecho | Reales')),
                ('real_lower_l', models.CharField(blank=True, max_length=10, verbose_name='Miembro inferior izquierdo | Reales')),
                ('apparent_upper_r', models.CharField(blank=True, max_length=10, verbose_name='Miembro superior derecho | Aparentes')),
                ('apparent_upper_l', models.CharField(blank=True, max_length=10, verbose_name='Miembro superior izquierdo | Aparentes')),
                ('apparent_lower_r', models.CharField(blank=True, max_length=10, verbose_name='Miembro inferior derecho | Aparentes')),
                ('apparent_lower_l', models.CharField(blank=True, max_length=10, verbose_name='Miembro inferior izquierdo | Aparentes')),
                ('arm_r_mt', models.CharField(blank=True, max_length=10, verbose_name='Brazo derecho | TM')),
                ('arm_l_mt', models.CharField(blank=True, max_length=10, verbose_name='Brazo izquierdo | TM')),
                ('forearm_r_mt', models.CharField(blank=True, max_length=10, verbose_name='Antebrazo derecho | TM')),
                ('forearm_l_mt', models.CharField(blank=True, max_length=10, verbose_name='Antebrazo izquierdo | TM')),
                ('thigh_r_mt', models.CharField(blank=True, max_length=10, verbose_name='Muslo derecho | TM')),
                ('thigh_l_mt', models.CharField(blank=True, max_length=10, verbose_name='Muslo izquierdo | TM')),
                ('leg_r_mt', models.CharField(blank=True, max_length=10, verbose_name='Pierna derecha | TM')),
                ('leg_l_mt', models.CharField(blank=True, max_length=10, verbose_name='Pierna izquierda | TM')),
            ],
        ),
    ]
