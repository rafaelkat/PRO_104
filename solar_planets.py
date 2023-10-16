import cv2


img = cv2.imread("solar-system.jpg")

cv2.imshow("Resultado", img)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.putText(img,
    "Sol",
    (142,80),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Mercurio",
    (284,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)
cv2.putText(img,
    "Venus",
    (426,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
) 

cv2.putText(img,
    "Terra",
    (568,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Marte",
    (710,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Jupter",
    (852,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Saturno",
    (994,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Urano",
    (1136,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)

cv2.putText(img,
    "Netuno",
    (1278,213),
    cv2.font_hershey_complex,
    2,
    (0,0,255)
)
cv2.imwrite("Solar_systemwithname.jpg",img)