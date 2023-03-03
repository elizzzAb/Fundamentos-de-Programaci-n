print("Ingrese su apellido");
nombre = input()
print("Hola, muy buen dia para usted, ingeniero", nombre,);
print("Le damos la mas cordial bienvenida a nuestro Sistema");
print("Somos integrantes de un grupo de trabajo");

print("""Y el propósito de este programa, es darle solución
a una serie de problemas o actividades que se nos han propuesto detallar.""");

print("""Para ello,
presentamos a continuación a cada uno de los integrantes de esta actividad.""");
print("""
""");

print("DATOS DE LOS INTEGRANTES: ");
print("""
""");

nomInt1= "Sonia Elizabeth";
apellidoInt1= "Abrego Núñez";
sexoInt1= "Femenino";
edadInt1= "19";

nomInt2= "Carlos Ernesto";
apellidoInt2= "Landaverde Quintanilla";
sexoInt2= "Masculino";
edadInt2= "16";

nomInt3= "Félix Mauricio";
apellidoInt3= "Palacios Tejada";
sexoInt3= "Masculino";
edadInt3= "17";

nomInt4= "Iván Anderson";
apellidoInt4= "Membreño Guardado";
sexoInt4= "Masculino";
edadInt4= "18";

nomInt5= "Marilyn Alexandra";
apellidoInt5= "Menjivar Fuentes";
sexoInt5= "Femenino";
edadInt5= "17";
print(f"""Nombre:             Apellido:                Sexo:       Edad:""");  
print(f"""{nomInt1}     {apellidoInt1}             {sexoInt1}    {edadInt1}""");
print(f"""{nomInt2}      {apellidoInt2}   {sexoInt2}   {edadInt2}""");
print(f"""{nomInt3}      {apellidoInt3}          {sexoInt3}   {edadInt3}""");
print(f"""{nomInt4}       {apellidoInt4}        {sexoInt4}   {edadInt4}""");
print(f"""{nomInt5}   {apellidoInt5}         {sexoInt5}    {edadInt5}""");

print("""
""");


print("BUSCAR SUB-CADENA DEL INTEGRANTE UNO: ");
mensaje = "Este dia por la mañana, la integrante del grupo Sonia fue a comprar papas fritas";
buscarSubCadena = mensaje.find("Sonia");
print(buscarSubCadena);

print("""
""");

print("REALIZAR LA SUMA DE LAS EDADES DE LOS INTEGRANTES: ");
edadInt1 = 19;
edadInt2 = 16;
edadInt3 = 17;
edadInt4 = 18;
edadInt5 = 17;
resultado = edadInt1 + edadInt2 + edadInt3 + edadInt4 + edadInt5;
print(resultado);
print("""
""");


print("SACAR EL PROMEDIO DE LAS EDADES DE LOS INTEGRANTES: ");
resultado = resultado/5;
print(resultado);
print("""
""");

print("MOSTRAR CONCATENACION DE LAS VARIABLES: NOMBRE Y APELLIDO, DE CADA INTEGRANTE: ");
nomCompletoInt1 = nomInt1 +  apellidoInt1;
nomCompletoInt2 = nomInt2 +  apellidoInt2;
nomCompletoInt3 = nomInt3 +  apellidoInt3;
nomCompletoInt4 = nomInt4 +  apellidoInt4;
nomCompletoInt5 = nomInt5 +  apellidoInt5;
print("""
""");
print("Nombres y apellidos del integrante 1: ", nomCompletoInt1);
print("Nombres y apellidos del integrante 2: ", nomCompletoInt2);
print("Nombres y apellidos del integrante 3: ", nomCompletoInt3);
print("Nombres y apellidos del integrante 4: ", nomCompletoInt4);
print("Nombres y apellidos del integrante 5: ", nomCompletoInt5);

print("""
""");


print("""ENCONTRAR LA EDAD A LA QUE SE GRADUARÁN AL FINALIZAR LA CARRERA
LOS INTEGRANTES DEL GRUPO: """);
print("""
""");
edadInt1 = 19+5;
resultado = edadInt1;
print("Edad que tendrá Sonia Abrego al graduarse: ");
print(resultado);
print("""
""");

edadInt2 = 16+5;
resultado = edadInt2;
print("Edad que tendrá Carlos Landaverde al graduarse: ");
print(resultado);
print("""
""");

edadInt3 = 17+5;
resultado = edadInt3;
print("Edad que tendrá Félix Palacios al graduarse: ");
print(resultado);
print("""
""");

edadInt4 = 18+5;
resultado = edadInt4;
print("Edad que tendrá Iván Membreño al graduarse: ");
print(resultado);
print("""
""");

edadInt5 = 17+5;
resultado = edadInt5;
print("Edad que tendrá Marilyn Menjivar al graduarse: ");
print(resultado);
print("""
""");



