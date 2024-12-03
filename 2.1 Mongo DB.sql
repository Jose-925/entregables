// Conectar y crear la colección 'Estudiantes'
db.Estudiantes.insertMany([
    { "nombre": "alejo", "edad": 20, "ciudad": "arauca" },
    { "nombre": "mary", "edad": 22, "ciudad": "valledupar" },
    { "nombre": "luis", "edad": 19, "ciudad": "santa marta" }
]);

// Consultar todos los documentos de la colección
db.Estudiantes.find();

// Filtrar estudiantes por ciudad
db.Estudiantes.find({ "ciudad": "valledupar" });

// Consultar estudiantes mayores de 20 años
db.Estudiantes.find({ "edad": { $gt: 20 } });
