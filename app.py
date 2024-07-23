from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)
app.secret_key = 'supersecretkey'  # Could add an app secret key here

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pin = request.form['pin']
        if pin == 'xxxx': #Insert real pin here  
            session['logged_in'] = True
            return redirect(url_for('registro'))
        else:
            flash('Invalid PIN')
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        # Get form data
        finca = request.form['finca']
        status = request.form['status']
        dv = request.form['dv']
        tomo_rollo = request.form['tomo_rollo']
        folio_doc = request.form['folio_doc']
        prov = request.form['prov']
        propietario = request.form['propietario']
        finca_madre = request.form['finca_madre']
        imto_anual_dgi = request.form['imto_anual_dgi']
        dueño_anterior = request.form['dueño_anterior']
        ubicacion = request.form['ubicacion']
        vsl = request.form['vsl']
        valor_ctstral_terreno = request.form['valor_ctstral_terreno']
        valor_ctstral_mejora = request.form['valor_ctstral_mejora']
        forma_de_adq = request.form['forma_de_adq']
        fecha_de_adquis = request.form['fecha_de_adquis']
        area = request.form['area']
        precio_por_hect = request.form['precio_por_hect']
        plano = request.form['plano']
        exoneracion_inicio = request.form['exoneracion_inicio']
        exoneracion_expira = request.form['exoneracion_expira']
        comentarios = request.form['comentarios']

        # Inserting data into database
        cur = mysql.connection.cursor()
        cur.execute("""
            INSERT INTO registro_fincas (
                finca, status, dv, tomo_rollo, folio_doc, prov, propietario, finca_madre,
                imto_anual_dgi, dueño_anterior, ubicacion, vsl, valor_ctstral_terreno,
                valor_ctstral_mejora, forma_de_adq, fecha_de_adquis, area, precio_por_hect,
                plano, exoneracion_inicio, exoneracion_expira, comentarios
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (finca, status, dv, tomo_rollo, folio_doc, prov, propietario, finca_madre, imto_anual_dgi, dueño_anterior, ubicacion, vsl, valor_ctstral_terreno, valor_ctstral_mejora, forma_de_adq, fecha_de_adquis, area, precio_por_hect, plano, exoneracion_inicio, exoneracion_expira, comentarios))
        mysql.connection.commit()
        cur.close()

        return render_template('success.html')
    return render_template('registro.html')

if __name__ == '__main__':
    app.run(debug=True)
