import cv2
img = cv2.imread("solar-system.jpg")

cv2.putText(img,
            "sun",
            (20,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "murcury",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (215,255,205)
            )
cv2.putText(img,
            "venus",
            (200,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (55,255,255)
            )
cv2.putText(img,
            "Earth",
            (300,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,55,255)
            )
cv2.putText(img,
            "mars",
            (400,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (55,25,55)
            )
cv2.putText(img,
            "jupiter",
            (550,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (25,55,25)
            )
cv2.putText(img,
            "satrun",
            (750,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (50,251,165)
            )
cv2.putText(img,
            "uranus",
            (980,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.putText(img,
            "neptune",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
            )
cv2.imshow("output",img)
cv2.imwrite("solar system",img)
cv2.waitKey(0)




