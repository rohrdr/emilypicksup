import cv2 as cv
import sys
import numpy as np
import os.path
import os


class Eyes:

    def __init__(self, config, weights):
        # need to initialize some stuff
        self.config = config
        self.weights = weights
        
        self.net = cv.dnn.readNetFromDarknet(self.config, self.weights)
        self.net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
        self.net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

        return

    def run(self, image):

        bbox = self.inference(self.net, image)

        return bbox

    def inference(self,
                net,
                frame,
                inpWidth = 480,
                inpHeight = 480,
                confThreshold = 0.5,
                nmsThreshold = 0.1,
                ):
        # takes an image, runs a forward pass, and removes the overlapping pictures. Returns a list of list
        # each element of the list is a list containing [classID,Confidence interval, center_x, center_y width, height]
        

        def getOutputsNames(net):
    # Get the names of all the layers in the network
            layersNames = net.getLayerNames()
    # Get the names of the output layers, i.e. the layers with unconnected outputs
            return [layersNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

        def postprocess(frame, outs):
            
            #Helper function to process the output of Yolo
            
            frameHeight = frame.shape[0]
            frameWidth = frame.shape[1]
        
            classIds = []
            confidences = []
            boxes = []
            # Scan through all the bounding boxes output from the network and keep only the
            # ones with high confidence scores. Assign the box's class label as the class with the highest score.
            classIds = []
            confidences = []
            boxes = []
            for out in outs:
                #print("out.shape : ", out.shape)
                for detection in out:
                    #if detection[4]>0.001:
                    scores = detection[5:]
                    classId = np.argmax(scores)
                    
                    #if scores[classId]>confThreshold:
                    
                    
                    confidence = scores[classId]
    #                if detection[4]>confThreshold:
                       # print(detection[4], " - ", scores[classId], " - th : ", confThreshold)
    #                   print(detection)
                        
                        
                    if confidence > confThreshold:
                        center_x = int(detection[0] * frameWidth)
                        center_y = int(detection[1] * frameHeight)
                        width = int(detection[2] * frameWidth)
                        height = int(detection[3] * frameHeight)
                        left = int(center_x - width / 2)
                        top = int(center_y - height / 2)
                        classIds.append(classId)
                        confidences.append(float(confidence))
                        boxes.append([left, top, width, height])
            
            indices = cv.dnn.NMSBoxes(boxes, confidences, confThreshold, nmsThreshold)
        
            for i in indices:
                i = i[0]
                box = boxes[i]
                left = box[0]
                top = box[1]
                width = box[2]
                height = box[3]
                center_x= (left+width/2) 
                center_y= (top+height/2) 
                ans.append([classIds[i],confidences[i],center_x/frameWidth,center_y/frameHeight,width/frameWidth,height/frameHeight])

#       We initialize with an empty list that we will returm at the end

        ans=[]
        
#       We convert the image we got into a blob with the good dimensions

        blob = cv.dnn.blobFromImage(image, 1/255, (inpWidth, inpHeight), [0,0,0], 1, crop=False)
        
        # Sets the input to the network

        
        net.setInput(blob)
    
        # Runs the forward pass to get output of the output layers
        outs = net.forward(getOutputsNames(net))
    
        # Remove the bounding boxes with low confidence, add the resulting boxes to ans
        postprocess(frame, outs)  

        return ans
