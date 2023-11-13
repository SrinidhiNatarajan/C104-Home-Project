import cv2

img = cv2.imread("solar-system.jpg")

solar_system = img[120:360,400:500]


cv2.putText(img,  
           "Sun",
           (20, 70),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mercury",
           (115, 250),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Venus",
           (195, 270),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Earth",
           (290, 270),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.putText(img,  
           "Mars",
           (390, 270),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (570, 370),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (780, 315),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (979, 315),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (1120, 315),  
           cv2.FONT_HERSHEY_COMPLEX_SMALL,
           0.5,  
           color=(255,255,255)
           )

cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("output",img)

cv2.waitKey(0)