import cv2

# Инициализируем каскад Хаара для определения лиц
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Загружаем видеофайл
video_path = 'video.mp4'
try:
    video_capture = cv2.VideoCapture(video_path)
except Exception as e:
    print(f"Не удалось загрузить видеофайл {video_path}. Ошибка: {e}")
    exit()

# Проверяем успешность загрузки видеофайла
if not video_capture.isOpened():
    print(f"Не удалось открыть видеофайл {video_path}")
    exit()

# Открываем окно с видео
cv2.namedWindow('video', cv2.WINDOW_NORMAL)

while True:
    # Читаем кадр за кадром
    ret, frame = video_capture.read()

    # Проверяем, удалось ли прочитать кадр
    if not ret:
        print("Не удалось получить кадр из видеофайла")
        break

    # Преобразуем кадр в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Ищем лица на кадре
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Для каждого найденного лица
    for (x, y, w, h) in faces:
        # Рисуем рамку вокруг лица
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Добавляем подпись к рамке
        cv2.putText(frame, 'Vovanchik', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Отображаем кадр в окне
    cv2.imshow('Video', frame)

    # Если нажата клавиша 'q', завершаем цикл
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождаем ресурсы
video_capture.release()
cv2.destroyAllWindows()

print("Помог Саша, Помог Денис, Сдал Вова. Самый лучший препод в НКЭиВТ Щерба Евгений Андреич ♥♥♥")