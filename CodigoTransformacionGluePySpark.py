def MyTransform(glueContext, dfc) -> DynamicFrameCollection:
    from pyspark.sql.functions import col, lower, length, year, current_date
    import datetime
    from awsglue.dynamicframe import DynamicFrame
    
    hoy = datetime.date.today()
    
    # Convertir DynamicFrame a DataFrame
    dyf = dfc.select(list(dfc.keys())[0])
    df = dyf.toDF()
    
    # Mostrar los datos originales
    print("Datos originales:")
    df.show(5)
    
    # Realizar transformaciones
    
    # 1. Convertir los nombres y correos electrónicos a minúsculas
    df = df.withColumn("nombre", lower(col("nombre")))
    df = df.withColumn("correo_electronico", lower(col("correo_electronico")))
    
    # 2. Calcular la edad actual
    df = df.withColumn("edad", year(current_date()) - year(col("fecha_nacimiento")))
    
    # 3. Añadir una nueva columna con la longitud del nombre
    df = df.withColumn("longitud_nombre", length(col("nombre")))
    
    # Mostrar los datos transformados
    print("Datos transformados:")
    df.show(5)
    
    # Convertir DataFrame de nuevo a DynamicFrame
    transformed_dyf = DynamicFrame.fromDF(df, glueContext, "transformed_dyf")
    
    return DynamicFrameCollection({"transformed_dyf": transformed_dyf}, glueContext)
