import ai2thor.controller
import cv2

c = ai2thor.controller.Controller()

c.start()
c.reset('FloorPlan201') # any scene is fine
c.step(dict(action='Initialize',renderImage=True, renderDepthImage=True, renderClassImage=True, renderObjectImage=True))

event0 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-1, z=0.5, y=2.6)))
event1 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-2, z=0.5, y=2.6)))
event2 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-3.5, z=0.5, y=2.6)))
event3 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-1, z=3.0, y=2.6)))
event4 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-2, z=3.0, y=2.6)))
event5 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-3.5, z=3.0, y=2.6)))
event6 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-1, z=5.3, y=2.6)))
event7 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-2, z=5.3, y=2.6)))
event8 = c.step(dict(action='AddThirdPartyCamera', rotation=dict(x=90, y=0, z=0), position=dict(x=-3.5, z=5.3, y=2.6)))

#print event.third_party_camera_frames # list equal to number of third party cameras; each element is the image in numpy identical in shape to the agent's camera image
b,g,r = cv2.split(event0.third_party_camera_frames[0])
cv2.imwrite('image0.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event1.third_party_camera_frames[1])
cv2.imwrite('image1.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event2.third_party_camera_frames[2])
cv2.imwrite('image2.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event3.third_party_camera_frames[3])
cv2.imwrite('image3.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event4.third_party_camera_frames[4])
cv2.imwrite('image4.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event5.third_party_camera_frames[5])
cv2.imwrite('image5.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event6.third_party_camera_frames[6])
cv2.imwrite('image6.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event7.third_party_camera_frames[7])
cv2.imwrite('image7.jpg',cv2.merge([r,g,b]))
b,g,r = cv2.split(event8.third_party_camera_frames[8])
cv2.imwrite('image8.jpg',cv2.merge([r,g,b]))

