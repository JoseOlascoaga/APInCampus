############# importar librerias o recursos#####
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin

# inicializaciones
app = Flask(__name__)
CORS(app)




# Mysql Conexión
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ncampus' # NOMBRE DE LA BASE DE DATOS#
mysql = MySQL(app)

# Flask utilizará esta clave para poder cifrar la información de la cookie
app.secret_key = "mysecretkey"


 

### ---------------------------------TABLA ESTUDIANTES----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DEL ESTUDIANTE DE LA TABLA 'estudiantes' ####
@cross_origin()
@app.route('/add_estudiantes', methods=['POST'])
def add_estudiantes():
    if request.method == 'POST':
        identificacion = request.json['identificacion']  
        nombre = request.json['nombres']  
        apellido = request.json['apellidos']  
        idProfe = request.json['idProfe']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO estudiante (identificacion, nombre, apellido, idProfe) VALUES (%s,%s,%s,%s)", (identificacion, nombre, apellido, idProfe))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'estudiantes' ####
@cross_origin()
@app.route('/getAllestu', methods=['GET'])
def getAllestu():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiante')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idEstu': result[0],'identificacion': result[1], 'nombre': result[2], 'apellido': result[3], 'idProfe': result[4]}
       payload.append(content)
       content = {}
    return jsonify({"informacion":"Registro exitoso"})

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'estudiantes' ####
@cross_origin()
@app.route('/getAllByidEstu/<idEstu>',methods=['GET'])
def getAllByidEstu(idEstu):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM estudiante WHERE idEstu = %s', (idEstu))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idEstu': result[0], 'identificacion': result[1], 'nombre': result[2], 'apellido': result[3], 'idProfe': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)

### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'estudiante' ###
@cross_origin()
@app.route('/update_estudiantes/<idEstu>', methods=['PUT'])
def update_estudiantes(idEstu):
    identificacion = request.json['identificacion']  
    nombre = request.json['nombre']  
    apellido = request.json['apellido'] 
    idProfe = request.json['idProfe'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE estudiante
        SET identificacion = %s,
            nombre = %s,
            apellido = %s,
            idProfe = %s,
        WHERE idEstu = %s
    """, (identificacion, nombre, apellido, idProfe, idEstu))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})

### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'estudiante' ###
@cross_origin()
@app.route('/delete_estu/<idEstu>', methods = ['DELETE'])
def delete_estu(idEstu):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM estudiante WHERE idEstu = %s', (idEstu,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### ------------------------------------TABLA NOTAS-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'notas' ####
@cross_origin()
@app.route('/add_nota', methods=['POST'])
def add_nota():
    if request.method == 'POST':
        corteuno = request.json['corteuno'] 
        cortedos = request.json['cortedos']  
        cortetres = request.json['cortetres']  
        promedio = request.json['promedio']  
        proGeneral = request.json['proGeneral']
        idEstu = request.json['idEstu']  
        idProfe = request.json['idProfe']  
        idProaca = request.json['idProaca']
        idSemes = request.json['idSemes']
        idAsign = request.json['idAsign']  
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO notas (corteuno, cortedos, cortetres, promedio, proGeneral, idEstu, idProfe, idProaca, idSemes, idAsign) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (corteuno, cortedos, cortetres, promedio, proGeneral, idEstu, idProfe, idProaca, idSemes, idAsign))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'notas' ####
@cross_origin()
@app.route('/getAllnotas', methods=['GET'])
def getAllnotas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM notas')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idNota': result[0], 'corteuno': result[1], 'cortedos': result[2], 'cortetres': result[3], 'promedio': result[4], 'proGeneral': result[5], 'idEstu': result[6], 'idProfe': result[7], 'idProaca': result[8], 'idSemes': result[9], 'idAsign': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'notas' ####
@cross_origin()
@app.route('/getAllByidnotas/<IdNota>',methods=['GET'])
def getAllByidnotas(idNota):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM notas WHERE idNota = %s', (idNota))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idNota': result[0],'corteuno': result[1], 'cortedos': result[2], 'cortetres': result[3], 'promedio': result[4], 'proGeneral': result[5], 'idEstu': result[6], 'idProfe': result[7], 'idProaca': result[8], 'idSemes': result[9], 'idAsign': result[10]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'notas' ###
@cross_origin()
@app.route('/updatenota/<IdNota>', methods=['PUT'])
def update_nota(idNota):
    corteuno = request.json['corteuno'] 
    cortedos = request.json['cortedos']  
    cortetres = request.json['cortetres']  
    promedio = request.json['promedio'] 
    proGeneral = request.json['proGeneral'] 
    idEstu = request.json['idEstu']  
    idProfe = request.json['idProfe']  
    idProaca = request.json['idProaca']
    idSemes = request.json['idSemes']
    idAsign = request.json['idAsign'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE notas
        SET corteuno = %s,
            cortedos = %s,
            cortetres = %s,
            promedio = %s,
            proGeneral = %s,
            idEstu = %s,
            idProfe = %s,
            idProaca = %s,
            idSemes = %s,
            idAsign = %s
        WHERE idNota = %s
    """, (corteuno, cortedos, cortetres, promedio, proGeneral, idEstu, idProfe, idProaca, idSemes, idAsign, idNota))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'notas' ###

@cross_origin()
@app.route('/delete_notas/<idNota>', methods = ['DELETE'])
def delete_notas(idNota):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM notas WHERE idNota = %s', (idNota,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -------------------------------------TABLA PROFESORES------------------------------------###


#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'profesores' ####
@cross_origin()
@app.route('/add_profe', methods=['POST'])
def add_profe():
    if request.method == 'POST':
        identificacion = request.json['identificacion']  
        nombre = request.json['nombre']  
        apellido = request.json['apellido']   
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO profesores (identificacion,nombre,apellido) VALUES (%s,%s,%s)", (identificacion,nombre, apellido))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'profesores' ####
@cross_origin()
@app.route('/getAllprofe', methods=['GET'])
def getAllprofe():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idProfesores': result[0],'identificacion': result[1], 'nombre': result[2], 'apellido': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)



#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'profesores' ####
@cross_origin()
@app.route('/getAllByidprofe/<idProfesores>', methods=['GET'])
def getAllByidprofe(idProfesores ):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores WHERE idProfesores  = %s', (idProfesores ))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idProfesores': result[0],'identificacion': result[1], 'nombre': result[2], 'apellido': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'profesores' ###
@cross_origin()
@app.route('/update_profe/<idProfesores>', methods=['PUT'])
def update_profe(idProfesores):
    identificacion = request.json['identificacion']  
    nombre = request.json['nombre']  
    apellido = request.json['apellido']  
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE profesores
        SET identificacion = %s,
            nombre = %s,
            apellido = %s
        WHERE idProfesores = %s
    """, (identificacion, nombre, apellido))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'profesores' ###
@cross_origin()
@app.route('/delete_profe/<idProfesores>', methods = ['DELETE'])
def delete_profe(idProfesores):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM profesores WHERE idProfesores = %s', (idProfesores,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -----------------------------------TABLA ASIGNATURAS----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'asignaturas' ####
@cross_origin()
@app.route('/add_asignatura', methods=['POST'])
def add_asignatura():
    if request.method == 'POST':
        nombreAsig = request.json['nombreAsig']
        jornada = request.json['jornada']
        idProaca = request.json['idProaca'] 
        idEstu = request.json['idEstu']
        idProfe = request.json['idProfe']
        idSemes = request.json['idSemes']     
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asignaturas (nombreAsig, jornada, idProaca, idEstu, idProfe, idSemes ) VALUES (%s,%s,%s,%s,%s,%s)", (nombreAsig, jornada, idProaca, idEstu, idProfe, idSemes))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'asignaturas' ####
@cross_origin()
@app.route('/getAllasignaturas', methods=['GET'])
def getAllasignaturas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asignaturas')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idAsignatura ': result[0], 'nombreAsig ': result[1], 'jornada ': result[2], 'idProaca': result[3], 'idEstu': result[4], 'idProfe': result[5], 'idSemes': result[6]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'asignaturas' ####
@cross_origin()
@app.route('/getAllByidasignatura/<idAsignatura>',methods=['GET'])
def getAllByidasignatura(idAsignatura ):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asignaturas WHERE idAsignatura  = %s', (idAsignatura ))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idAsignatura ': result[0], 'nombreAsig ': result[1], 'jornada ': result[2], 'idProaca': result[3], 'idEstu': result[4], 'idProfe': result[5], 'idSemes': result[6]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'asignaturas' ###
@cross_origin()
@app.route('/update_asignatura/<idAsignatura>', methods=['PUT'])
def update_asignatura(idAsignatura):
    nombreAsig = request.json['nombreAsig']
    jornada = request.json['jornada']
    idProaca = request.json['idProaca'] 
    idEstu = request.json['idEstu']
    idProfe = request.json['idProfe']
    idSemes = request.json['idSemes']    
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE asignaturas
        SET nombreasig = %s,
            jornada = %s,
            idProaca = %s,
            idEstu = %s,
            idProfe = %s,
            idSemes = %s,
        WHERE idAsignatura = %s
    """, (nombreAsig, jornada, idProaca, idEstu, idProfe, idSemes, idAsignatura ))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'asignaturas' ###
@cross_origin()
@app.route('/delete_asignatura/<idAsignatura>', methods = ['DELETE'])
def delete_asignatura(idAsignatura):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM asignaturas WHERE idAsignatura = %s', (idAsignatura,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -----------------------------------TABLA SEMESTRE-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'semestre' ####
@cross_origin()
@app.route('/add_semestre', methods=['POST'])
def add_semestre():
    if request.method == 'POST':
        semestres = request.json['semestres']  
        idEstu = request.json['idEstu']  
        idProfe = request.json['idProfe']  
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO semestres (semestre, idEstu, idProfe) VALUES (%s,%s,%s)", (semestres, idEstu, idProfe ))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'semestre' ####
@cross_origin()
@app.route('/getAllsemestre', methods=['GET'])
def getAllsemestre():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM semestre')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdSemestre': result[0],'semestre': result[1], 'IdEstu': result[2], 'IdProfe': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'semestre' ####
@cross_origin()
@app.route('/getAllByIdsemestre/<IdSemestre>',methods=['GET'])
def getAllByIdsemestre(IdSemestre ):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM semestre WHERE IdSemestre  = %s', (IdSemestre ))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdSemestre ': result[0], 'semestre': result[1], 'IdEstu': result[2], 'IdProfe': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)

### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'semestre' ###
@cross_origin()
@app.route('/update5/<idSemestre>', methods=['PUT'])
def update_semestre5(idSemestre):
    semestre = request.json['semestre'] 
    idEstu = request.json['IdEstu']  
    idProfe = request.json['IdProfe'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE semestre
        SET semestre = %s,
            idAsignatura  = %s,
            idEstu = %s,
            idProfe = %s
        WHERE idSemestre = %s
    """, (semestre, idEstu, idProfe, idSemestre ))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'semestre' ###
@cross_origin()
@app.route('/delete5/<idSemestre>', methods = ['DELETE'])
def delete_semestre5(idSemestre):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM semestre WHERE IdSemestre = %s', (idSemestre,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})

### ------------------------------------------------------------------------------------###

###*************************************************************************************###

### -----------------------------------TABLA PROGRAMAS ACADEMICOS-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'programas academicos' ####
@cross_origin()
@app.route('/add_proacad', methods=['POST'])
def add_proacad():
    if request.method == 'POST':
        nombreProacad = request.json['nombreProacad']  
        IdEstu = request.json['IdEstu']  
        IdSemes = request.json['IdSemes']
        IdProfe = request.json['IdProfe']    
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO proacad (nombreProacad, IdEstu, IdSemeS, idProfe) VALUES (%s,%s,%s,%s)", (nombreProacad, IdEstu, IdSemes, IdProfe))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'proacad' ####
@cross_origin()
@app.route('/getAllproacad', methods=['GET'])
def getAllproacad():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proacad')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'IdProacad': result[0],'nombreProacad': result[1], 'IdEstu': result[2], 'IdSemestre': result[3], 'IdProfe': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'proacad' ####
@cross_origin()
@app.route('/getAllByidProacad/<idProacad>',methods=['GET'])
def getAllByidProacad(idProacad):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM proacad WHERE idProacad  = %s', (idProacad))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idProacad': result[0], 'nombreProacad': result[1], 'idEstu': result[2], 'idSemes': result[3], 'idProfe': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'proacad' ###
@cross_origin()
@app.route('/proacad/<IdProacad>', methods=['PUT'])
def update_proacad(idProacad):
    nombreprog = request.json['nombreProacad']  
    idEstu = request.json['idEstu']
    idSemes = request.json['idSemes'] 
    idProfe = request.json['idProfe']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE proacad
        SET nombreprog = %s,
            idEstu = %s,
            idSemes  = %s,
            idProfe = %s
        WHERE Idprogramaacad = %s
    """, (nombreprog, idEstu, idSemes, idProfe, idProacad))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'proacad' ###
@cross_origin()
@app.route('/proacad/<IdProacad>', methods = ['DELETE'])
def delete_proacad(IdProacad):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM proacad WHERE IdProacad = %s', (IdProacad,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


### -----------------------------------TABLA CURSO-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'CURSOS' ####
@cross_origin()
@app.route('/add_cursos', methods=['POST'])
def add_cursos():
    if request.method == 'POST':
        numCurso = request.json['numCurso']  
        idEstu = request.json['idEstu']  
        idProfe = request.json['idProfe'] 
        idMatric = request.json['idMatric'] 
        idSemes = request.json['idSemes']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO cursos (numCurso, IdEstu, idProfe, idMatric, IdSemes) VALUES (%s,%s,%s,%s,%s)", (numCurso, idEstu, idProfe, idMatric, idSemes))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    
    
    
#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'cursos' ####
@cross_origin()
@app.route('/getAllcursos', methods=['GET'])
def getAllcursos():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cursos')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idCurso': result[0],'numCurso': result[1], 'idEstu': result[2], 'IdProfe': result[3], 'idMatric': result[4], 'idSemes': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)

    

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'cursos' ####
@cross_origin()
@app.route('/getAllByidCurso/<idCurso>',methods=['GET'])
def getAllByidCurso(idCurso):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM cursos WHERE idCurso  = %s', (idCurso))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idCurso': result[0],'numCurso': result[1], 'idEstu': result[2], 'IdProfe': result[3], 'idMatric': result[4], 'idSemes': result[5]}
       payload.append(content)
       content = {}
    return jsonify(payload)



### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'cursos' ###
@cross_origin()
@app.route('/update6/<idCurso>', methods=['PUT'])
def update_cursos(idCurso):
    numCurso = request.json['numCurso']  
    idEstu = request.json['idEstu']
    idProfe = request.json['idProfe']
    idMatric = request.json['idMatric']
    idSemes = request.json['idSemes'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE cursos
        SET numCurso = %s,
            idEstu = %s,
            idProfe = %s,
            idMatric = %s,
            idSemes  = %s
        WHERE idCurso = %s
    """, (numCurso, idEstu, idProfe, idMatric, idSemes, idCurso))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'cursos' ###
@cross_origin()
@app.route('/delete6/<idCurso>', methods = ['DELETE'])
def delete_cursos(idCurso):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM cursos WHERE idCurso = %s', (idCurso,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})  
    
    
    
    
### -----------------------------------TABLA MATRICULA-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'matriculas' ####
@cross_origin()
@app.route('/add_matriculas', methods=['POST'])
def add_matriculas():
    if request.method == 'POST':  
        idEstu = request.json['idEstu']    
        idSemes = request.json['idSemes']
        idAsign = request.json['idAsign']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO matriculas (idEstu, idSemes, idAsign) VALUES (%s,%s,%s)", (idEstu, idSemes, idAsign))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    
    
    
#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'matriculas' ####
@cross_origin()
@app.route('/getAllcursos', methods=['GET'])
def getAllmatriculas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM matriculas')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idMatricula': result[0], 'idEstu': result[1], 'idSemes': result[2], 'idAsign': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)

    

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'matriculas' ####
@cross_origin()
@app.route('/getAllByidMatricula/<idMatricula>',methods=['GET'])
def getAllByidMatricula(idMatricula):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM matriculas WHERE idMatricula  = %s', (idMatricula))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idMatricula': result[0], 'idEstu': result[1], 'idSemes': result[2], 'idAsign': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)



### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'matriculas' ###
@cross_origin()
@app.route('/update6/<idMatricula>', methods=['PUT'])
def update_matriculas(idMatricula):
    idEstu = request.json['idEstu']    
    idSemes = request.json['idSemes']
    idAsign = request.json['idAsign'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE cursos
        SET numCurso = %s,
            idEstu = %s,
            idSemes  = %s,
            idAsign = %s
        WHERE idMatricula = %s
    """, (idEstu, idSemes, idAsign, idMatricula))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'matriculas' ###
@cross_origin()
@app.route('/delete6/<idMatricula>', methods = ['DELETE'])
def delete_matriculas(idMatricula):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM matriculas WHERE idMatricula = %s', (idMatricula,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"}) 



### -----------------------------------TABLA ASISTENCIAS-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'asistencias' ####

@cross_origin()
@app.route('/add_asistencias', methods=['POST'])
def add_asistencias():
    if request.method == 'POST':
        idAsistencia = request.json['idAsistencia']  
        asistencia = request.json['asistencia']
        fecha = request.json['fecha'] 
        idProfe = request.json['idProfe'] 
        idEstu = request.json['idEstu']  
        idAsign = request.json['idAsign']  
        idSemes = request.json['idSemes']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO asistencias (idAsistencia, asistencia, fecha, idProfe, idEstu, idAsign, idSemes) VALUES (%s,%s,%s%s,%s,%s,%s)", (idAsistencia, asistencia, fecha, idProfe, idEstu, idAsign, idSemes))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    
    
    
#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'asistencias' ####
@cross_origin()
@app.route('/getAllasistencias', methods=['GET'])
def getAllasistencias():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idAsistencia': result[0], 'asistencia': result[1], 'fecha': result[2], 'idProfe': result[3], 'idEstu': result[4], 'idAsign': result[5], 'idSemes': result[6]}
       payload.append(content)
       content = {}
    return jsonify(payload)

    

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'asistencias' ####
@cross_origin()
@app.route('/getAllByidAsistencia/<idAsistencia>',methods=['GET'])
def getAllByidAsistencia(idAsistencia):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM asistencias WHERE idAsistencia  = %s', (idAsistencia))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {}
       payload.append(content)
       content = {'idAsistencia': result[0], 'asistencia': result[1], 'fecha': result[2], 'idProfe': result[3], 'idEstu': result[4], 'idAsign': result[5], 'idSemes': result[6]}
    return jsonify(payload)



### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'matriculas' ###
@cross_origin()
@app.route('/update_asistencias/<idAsistencia>', methods=['PUT'])
def update_asistencias(idAsistencia):
    idAsistencia = request.json['idAsistencia']  
    asistencia = request.json['asistencia']
    fecha = request.json['fecha'] 
    idProfe = request.json['idProfe'] 
    idEstu = request.json['idEstu']  
    idAsign = request.json['idAsign']  
    idSemes = request.json['idSemes']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE asistencias
        SET asistencia = %s,
            fecha = %s,
            idProfe  = %s,
            idEstu = %s,
            idAsign = %s,
            idSemes = %s
        WHERE idAsistencia = %s
    """, (asistencia, fecha, idProfe, idEstu, idAsign, idSemes, idAsistencia))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'matriculas' ###
@cross_origin()
@app.route('/delete_asistencia/<idAsistencia>', methods = ['DELETE'])
def delete_asistencias(idAsistencia):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM asistencias WHERE idAsistencia = %s', (idAsistencia,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"}) 



### -----------------------------------TABLA DETALLE MATRICULA-----------------------------------###

#### RUTA PARA CREAR UN REGISTRO DE LA TABLA 'detallematricula' ####
@cross_origin()
@app.route('/add_detallematricula', methods=['POST'])
def add_detallematricula():
    if request.method == 'POST':
        vlrMatricula = request.json['vlrMatricula']  
        idMatric = request.json['idMatric']   
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO detallematricula (vlrMatricula, idMatric) VALUES (%s,%s)", (vlrMatricula, idMatric ))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})
    

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'detallematricula' ####
@cross_origin()
@app.route('/getAlldetallematricula', methods=['GET'])
def getAlldetallematricula():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM detallematricula')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idDetalle': result[0],'vlrMatricula': result[1], 'idMatric': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'detallematricula' ####
@cross_origin()
@app.route('/getAllByidDetalle/<idDetalle>',methods=['GET'])
def getAllByidDetalle(idDetalle):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM detallematricula WHERE idDetalle  = %s', (idDetalle))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'idDetalle': result[0],'vlrMatricula': result[1], 'idMatric': result[2]}
       payload.append(content)
       content = {}
    return jsonify(payload)

### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'detallematricula' ###
@cross_origin()
@app.route('/update_detallematricula/<idDetalle>', methods=['PUT'])
def update_detallematricula(idDetalle):
    vlrMatricula = request.json['vlrMatricula']  
    idMatric = request.json['idMatric'] 
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE detallematricula
        SET vlrMatricula = %s,
            idMatric = %s
        WHERE idDetalle = %s
    """, (vlrMatricula, idMatric, idDetalle ))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'semestre' ###
@cross_origin()
@app.route('/delete_detallematricula/<idDetalle>', methods = ['DELETE'])
def delete_detallematricula(idDetalle):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM detallematricula WHERE idDetalle = %s', (idDetalle,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})








### -----------------------------------TABLA CONTACTS-----------------------------------###

## LA TABLA CONTACTS SERVIRÁ PARA LLEVAR EL REGISTRO DE LAS PERSONAS QUE ADQUIERAN UN LIBRO
## DE LA BIBLIOTECA

#### RUTA PARA CONSULTAR LOS REGISTROS DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/getAll', methods=['GET'])
def getAll():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id': result[0], 'identificacion': result[1],  'fullname': result[2], 'phone': result[3], 'email': result[4]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CONSULTAR POR PARÁMETRO LOS REGISTROS DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/getAllById/<id>',methods=['GET'])
def getAllById(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id LIKE %s', (id,))
    rv = cur.fetchall()
    cur.close()
    payload = []
    content = {}
    for result in rv:
       content = {'id': result[0], 'fullname': result[1], 'phone': result[2], 'email': result[3]}
       payload.append(content)
       content = {}
    return jsonify(payload)


#### RUTA PARA CREAR UN REGISTRO DE PRESTAMO DE LA TABLA 'contacts' ####
@cross_origin()
@app.route('/add_contact', methods=['POST'])
def add_contact():
    if request.method == 'POST':
        identificacion = request.json['identificacion'] 
        fullname = request.json['fullname']  ## nombre
        phone = request.json['phone']        ## telefono
        email = request.json['email']        ## email
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contacts (identificacion, fullname, phone, email) VALUES (%s,%s,%s,%s)", (identificacion, fullname, phone, email))
        mysql.connection.commit()
        return jsonify({"informacion":"Registro exitoso"})


### RUTA PARA ACTUALIZAR UN REGISTRO EN LA TABLA 'contacts' ###
@cross_origin()
@app.route('/update/<id>', methods=['PUT'])
def update_contact(id):
    identificacion = request.json['identificacion'] 
    fullname = request.json['fullname']
    phone = request.json['phone']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("""
        UPDATE contacts
        SET identificacion = %s,
            fullname = %s,
            email = %s,
            phone = %s
        WHERE id = %s
    """, (identificacion,fullname, email, phone, id))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro actualizado"})


### RUTA PARA ELIMINAR UN REGISTRO EN LA TABLA 'contacts' ###
@cross_origin()
@app.route('/delete/<id>', methods = ['DELETE'])
def delete_contact(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id = %s', (id,))
    mysql.connection.commit()
    return jsonify({"informacion":"Registro eliminado"})


### ------------------------------------------------------------------------------------###

###*************************************************************************************###


# La API inicia
if __name__ == "__main__":
    app.run(port=3000, debug=True)
