from ultralytics import YOLO

# Cargar el modelo YOLO preentrenado
model = YOLO('yolov8n.pt')  

# Realizar predicciones en la imagen
results = model('C:/Users/jcmon/Desktop/final_inteligente/train/limite.jpeg',imgsz=1280) # Ruta de la imagen 1
results = model.predict(source='C:/Users/jcmon/Desktop/final_inteligente/train/KTJ3PDGDTRDRRKXZEC5L6XJJU4-1200x640.jpg', imgsz=1280) # Ruta de la imagen 1
results = model.predict(source='C:/Users/jcmon/Desktop/final_inteligente/train/p1.jpg' ,imgsz=1280)  # Solo detecta carros, buses, señales


# Mostrar resultados
results[0].show()


