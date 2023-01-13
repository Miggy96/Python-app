
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '@ndresc96-'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)


# settings
app.secret_key = 'mysecretkey'



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    return render_template('index.html', contacts = data)


@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        id = request.form['id']
        fullname = request.form['fullname']
        hobbie = request.form['hobbie']
        tipo_id = request.form['tipo id']
        cur = mysql.connection.cursor()
        cur.execute = "INSERT INTO  contacts (id, fullname, hobbie, tipo id) VALUES (%s, %s, %s, %s)",
        (id, fullname, hobbie, tipo_id)
        mysql.connection.commit()
        flash('Contacto añadido satisfactoriamente')
        return redirect(url_for('Index'))
         



@app.route('/see')
def see():
    return "see"   


  
@app.route('/edit/<id>')
def get_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE  id = %s', [id])
    data = cur.fetchall()
    return render_template('edit-contact.html', contact = data[0])

@app.route('/update/<id>')
def update_contact(id):
   if request.method == 'POST':
        id = request.form['id']
        fullname = request.form['fullname'] 
        hobbie = request.form['hobbie'] 
        tipo_id = request.form['tipo_id'] 
        cur = mysql.connection.cursor()
        cur.execute("""
        UPDATE contacts
        SET id =  %s,
        fullname = %s,
        hobbie = %s,
        tipo_id = %s,
        WHERE id = %s
        """, (id, fullname,hobbie,tipo_id, id))
        mysql.connection.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('Index'))



@app.route('/delete/<string:id>')
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE  id = {0}' .format(id))
    mysql.connection.commit()
    flash('Contacto eliminado satisfactoriamente')
    return redirect(url_for('Index'))






if __name__ == '__main__':
   app.run(port = 3000, debug = True)