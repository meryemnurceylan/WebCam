import cv2
# bu kütüphaneyi bilgisayar kamerasından video akışını yakalamak ve görüntüyü ekranda göstermek için kullanırız.

kamera = cv2.VideoCapture(0)
# varsayılan kamera çağırılır.

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
# MJPEG, Motion JPEG'ın kısaltmasıdır ve video sıkıştırma formatıdır.
# MJPEG, her kareyi ayrı bir JPEG görüntüsü olarak sıkıştırır ve ardışık görüntülerin hızlı bir şekilde oynatılmasını sağlar.

kayit = cv2.VideoWriter('videolar/kayit.avi', fourcc, 20.0, (640, 480))
#videolar adlı dosyaya kayit.avi biçiminde bu video kaydedilecek.

while (True):
# bu döngü sürekli olarak kameradan gelen görüntüyü yakalar ve ekranda gösterecek

    ret, videoGoruntu = kamera.read()
# goruntu değişkenleriyle kameradan alınan bir video çerçevesini döndürür
# ret çerçevenin doğru şekilde alınıp alınmadığını belirten bir boolean değerdir
# videoGoruntu alınan çerçevenin kendisidir.

    if ret:
      #  renk = cv2.cvtColor(videoGoruntu, cv2.Color...)
        kayit.write(videoGoruntu)  # video yazma
        cv2.imshow('WebCam', videoGoruntu)
        if cv2.waitKey(25) & 0xFF == ord('t'):
#kodu, her döngüde klavyeden bir tuşa basılıp basılmadığını kontrol eder.
# Eğer 't' tuşuna basılırsa, döngüyü sonlandırır.(burda butonla sonlandırcaz)
            break
    else:
        break

kamera.release()  # kameraya erişim serbest bırakılır
kayit.release()  # kaydı durdur
cv2.destroyAllWindows()  # açılan pencereleri kapat
