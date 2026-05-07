from ultralytics import YOLO
import cv2

# Cargar modelo preentrenado o entrenado
model = YOLO('yolov8n.pt')  # Cambia por 'best.pt' si entrenaste un modelo

# Captura de video en tiempo real
cap = cv2.VideoCapture(0)  # 0 para la cámara integrada

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Realizar detecciones
    results = model(frame)

    # Mostrar resultados en el frame
    annotated_frame = results[0].plot()
    cv2.imshow("Detección de Seguridad Vial", annotated_frame)

    # Presiona 'q' para salir
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
