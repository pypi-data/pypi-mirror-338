
import numpy as np
import copy
import cv2 
import warnings
def xyxy_to_xywh(xyxy_bbox):
    x_min, y_min, x_max, y_max = xyxy_bbox
    width = x_max - x_min
    height = y_max - y_min
    return x_min, y_min, width, height
def xywh_to_xyxy(xywh_bbox):
    x, y, width, height = xywh_bbox
    x_min = x
    y_min = y
    x_max = x + width
    y_max = y + height
    return x_min, y_min, x_max, y_max

def iou(box1, box2):
    # Calculate the coordinates of the intersection rectangle
    x1 = max(box1[0], box2[0])
    y1 = max(box1[1], box2[1])
    x2 = min(box1[2], box2[2])
    y2 = min(box1[3], box2[3])

    # Check for non-overlapping boxes
    if x1 < x2 and y1 < y2:
        # Calculate the area of the intersection rectangle
        intersection_area = (x2 - x1) * (y2 - y1)

        # Calculate the area of the bounding boxes
        area_box1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area_box2 = (box2[2] - box2[0]) * (box2[3] - box2[1])

        # Calculate the IoU
        iou = intersection_area / (area_box1 + area_box2 - intersection_area)
        return iou
    else:
        return 0.0
    
def read_box(bbox):
    return [bbox["x"], bbox["y"], bbox["width"], bbox["height"]]
def adherence(bbox1, bbox2):
    bbox1 =read_box(bbox1)
    bbox2 =read_box(bbox2)

    bbox1 = xywh_to_xyxy ( bbox1)
    bbox2 = xywh_to_xyxy ( bbox2)
    if iou (bbox1, bbox2)>0:
        return 1
    else:
        return 0 
    
def distance(bbox1, bbox2):
    bbox1 =read_box(bbox1)
    bbox2 =read_box(bbox2)
    point1 = np.array([bbox1[0]+bbox1[2]/2 , bbox1[1]+bbox1[3]/2])
    point2 = np.array([bbox2[0]+bbox2[2]/2 , bbox2[1]+bbox2[3]/2])
    """bbox1 = xywh_to_xyxy ( bbox1)
    bbox2 = xywh_to_xyxy ( bbox2)"""
    return np.linalg.norm(point1 - point2)
    

def get_global_rectangle(bbox1,bbox2):
    """get rectangle englobant les 2 bounding boxes 

    Args:
        bbox1 (_type_): _description_
        bbox2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    rect1=[bbox1["x"], bbox1["y"], bbox1["width"]+bbox1["x"], bbox1["height"]+bbox1["y"]]
    rect2=[bbox2["x"], bbox2["y"], bbox2["width"]+bbox2["x"], bbox2["height"]+bbox2["y"]]
    min_x = min(rect1[0], rect2[0])
    min_y = min(rect1[1], rect2[1])
    max_x = max(rect1[2], rect2[2])
    max_y = max(rect1[3], rect2[3])

    # Return the bounding box as a tuple (x1, y1, x2, y2)
    bounding_box = (min_x, min_y, max_x -min_x, max_y-min_y)
    bounding_box ={"x":bounding_box[0],"y":bounding_box[1], "width":bounding_box[2], "height":bounding_box[3] }
    return bounding_box


"""def compute_acceleration():
    return 0"""

def get_centroid(bbox):
    bbox2=[bbox["x"], bbox["y"], bbox["width"], bbox["height"]]
    return [bbox2[0] + bbox2[2]/2, bbox2[1] + bbox2[3]/2, bbox["x"], bbox["y"], bbox["width"], bbox["height"]]

def sort_dictionnary(myDict):
    #we make sure frame id are integer 
    myDict = {int(k):v for k,v in myDict.items()}
    myKeys = list(myDict.keys())
    #myKeys = [int(i) for i in myKeys]
    myKeys.sort()
    sorted_dict = {str(i): myDict[i] for i in myKeys}
    return sorted_dict

def process_speed_acceleration(sparsed_track,pig_id,frame_id):
    """_summary_
    we assume the track is sparsed and ordered in term of frames, the track is provided in pig_id->frame_id 
    #previous_available_frame_id_for_track previous_frame_id
    Args:
        sparsed_track (_type_): _description_
        pig_id (_type_): _description_
        frame_id (_type_): _description_
    """
    if int(frame_id)>0:
        frame_id_idx = list(sparsed_track[pig_id].keys()).index(frame_id)
        try:
            previous_frame_id = list(sparsed_track[pig_id].keys())[frame_id_idx-1]
            previous_centroid = sparsed_track[pig_id][previous_frame_id]["centroid"]
        except:
            warnings.warn("a previous frame with this centroid doesn't exist")
            return sparsed_track
        delta_t = int(frame_id) - int(previous_frame_id)
        centroid = sparsed_track[pig_id][frame_id]["centroid"]
        
        delta_x =  centroid[0] - previous_centroid[0]
        delta_y =  centroid[1] - previous_centroid[1]
        sparsed_track[pig_id][frame_id]["speed"] = np.sqrt(delta_x**2 + delta_y**2) / delta_t
    if int(frame_id)>1:
        ###process acceleration
        frame_id_idx = list(sparsed_track[pig_id].keys()).index(frame_id)
        try:
            previous_frame_id = list(sparsed_track[pig_id].keys())[frame_id_idx-1]
            previous_speed = sparsed_track[pig_id][previous_frame_id]["speed"]
        except:
            warnings.warn("a previous frame with this speed doesn't exist")
            return sparsed_track
        
        delta_t = int(frame_id) - int(previous_frame_id)
        speed = sparsed_track[pig_id][frame_id]["speed"]
       
        delta_speed =  speed - previous_speed
        #delta_y =  speed[1] - previous_speed[1]
        sparsed_track[pig_id][frame_id]["acceleration"] = delta_speed/delta_t#np.sqrt(delta_x**2 + delta_y**2) / delta_t
    
    return sparsed_track
    #for frame_id in sparsed_track[pig_id].keys()[]

def process_centroid_speed_acceleration(informations):
    transformed={}
    informations = sort_dictionnary(informations)
    for frame_id,frame_info in informations.items():
        for pig_id, pig_info in frame_info.items():
            if pig_id not in transformed.keys():
                transformed[pig_id]={}
            transformed[pig_id][frame_id]={"centroid":get_centroid(pig_info["bbox"])}
            transformed = process_speed_acceleration(transformed, pig_id, frame_id)

    for frame_id, frame_info in informations.items():
        for pig_id, pig_info in frame_info.items():
            try:
                speed = transformed[pig_id][frame_id]["speed"]
                rounded_speed= round(speed, 2)
            except:
                speed = None
                rounded_speed = " N"
            try:  
                acceleration = transformed[pig_id][frame_id]["acceleration"]
                rounded_acceleration = round(acceleration,  2)
            except:
                acceleration= None
                rounded_acceleration=" N"
            informations[frame_id][pig_id].update({"speed":speed,  "acceleration":acceleration , "behaviour": "v:"+str(rounded_speed)+" acc:"+str(rounded_acceleration)})

    return informations
    max_time = max([int(i) for i in informations.keys()])
    assert max_time == list(informations.keys())[-1]
    time_range_with_missing = np.arange(0,max_time+1)
    for pig_id, pig_over_time_centroid in transformed.items():
        #à partir de python 3.7 les dictionnaire sont garanties d'être lu dans l'ordre d'insertion
        pig_time= np.array(list(pig_over_time_centroid.keys()))
        pig_over_time_centroid = np.array(list(pig_over_time_centroid.values()))
        
        # missing_time = [i for i in time_range_with_missing if i not in pig_time]
        x_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,0])
        y_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,1])
        
        xmin_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,2])
        ymin_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,3])
        w_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,4])
        h_with_interpolated = np.interp(time_range_with_missing, pig_time, pig_over_time_centroid[:,5])
        
        delta_t = np.diff(time_range_with_missing)#pig_time)
        delta_x = np.diff(x_with_interpolated)
        delta_y = np.diff(y_with_interpolated)
        
        speed = np.sqrt(delta_x**2 + delta_y**2) / delta_t
        acceleration = np.diff(speed) / delta_t[1:]
        
        for frame_id in time_range_with_missing[:-2]:
            if frame_id not in informations.keys():
                informations[frame_id]={}
            if pig_id not in informations[frame_id].keys():
                informations[frame_id][pig_id]={}
            
            informations[frame_id][pig_id].update({"bbox":{"x":xmin_with_interpolated[frame_id], "y":ymin_with_interpolated[frame_id], "width":w_with_interpolated[frame_id], "height":h_with_interpolated[frame_id]}, "centroid":[x_with_interpolated[frame_id], y_with_interpolated[frame_id]],"speed":speed[frame_id], "acceleration":acceleration[frame_id] })
      
    keys_to_remove = list(informations.keys())[-2:]
    new_informations= {key: informations[key] for key in informations if key not in keys_to_remove}
  
    return new_informations
        

def add_feature(informations, fps=6, aggression_duration= 10, acc_avg_th=5,acc_var_th=3, adh_index_percent=0.3, max_id=16 ):
    """
    dans le papier ils utilisent l'acceleration du groupe de bounding box comme feature de détection d'aggression
    je pense d'après les observations que c'est plutôt la variance dans l'acceleration, vitesse moyenne élevée, et un index d'adhesion élevé 
    """
    informations = {int(k):v for k,v in informations.items()}
    information_with= copy.deepcopy(informations)
    for frame_id, frame_information in informations.items():
        for pig_id_1, pig_info_1 in frame_information.items():
            for pig_id_2, pig_info_2 in frame_information.items():
                if pig_id_1!=pig_id_2:
                    join_pig_id=str(pig_id_1)+"and"+str(pig_id_2)
                    information_with[frame_id][join_pig_id] = {}
                    ad = adherence(pig_info_1["bbox"], pig_info_2["bbox"] )
                    
                    information_with[frame_id][join_pig_id]["adherence"]= ad
                    information_with[frame_id][join_pig_id]["distance"]= distance(pig_info_1["bbox"], pig_info_2["bbox"] )
                    information_with[frame_id][join_pig_id]["bbox"]= get_global_rectangle(pig_info_1["bbox"], pig_info_2["bbox"] )
                    #if ad: 
                    #    frame_information[join_pig_id]["adherence"]= ad
    information_with = process_centroid_speed_acceleration(information_with)
    
    
    ##we add acceleration and speed of the two pigs in a rectangle 
    for frame_id, frame_information in information_with.items():
        for pig_id, pig_info in frame_information.items():
            if "and" in pig_id:
                pig_1 = pig_id.split("and")[0]
                pig_2 = pig_id.split("and")[1]
                pig_info["acceleration1"] = information_with[frame_id][pig_1]["acceleration"]
                pig_info["acceleration2"] = information_with[frame_id][pig_2]["acceleration"]
                pig_info["speed1"] = information_with[frame_id][pig_1]["speed"]
                pig_info["speed2"] = information_with[frame_id][pig_2]["speed"]
    
    
    ############################compute aggression accordingly to chenchen 2017: #######################
    #1-Adhesion index of pair of rectangles: it's the percentage of frames where the pair of pigs have adhesion  in a fixed sequence of frames 
    # in our case we will consider 10 secondes (60 frames according to the pigbehavior dataset) as the lenght of each sequence 
    
    sequence_lenght = aggression_duration*fps
    list_of_pig_id=[str(float(i)) for i in range(1,max_id)] + [str(float(i))+"and"+str(float(j)) for i in range(1,max_id) for j in range(1,max_id)  if i!=j]
    key_list= { "distance":None, "acceleration":None, "acceleration1":None, "acceleration2":None,"speed1":None, "speed2":None, "speed":None,"adherence":None}# "bbox":None,
    transformed={}
    #informations = sort_dictionnary(information_with)
    behaviours={}
    previous =0
    for frame_id,frame_info in information_with.items():
        behaviours[frame_id]={}
        for pig_id in list_of_pig_id: #, pig_info in frame_info.items():
            if "and" in pig_id:
                if pig_id not in transformed.keys():
                    transformed[pig_id]={}
                if pig_id not in information_with[frame_id]:
                    transformed[pig_id][frame_id] =copy.deepcopy(key_list)
                else:
                    transformed[pig_id][frame_id]= copy.deepcopy(information_with[frame_id][pig_id]) 
                
                
        #if int(frame_id)<previous:
        #    continue
        previous=int(frame_id)+sequence_lenght
        
        for pig_id in list_of_pig_id: #, pig_info in frame_info.items():
            if "and" in pig_id:
                """if pig_id not in transformed.keys():
                    transformed[pig_id]={}
                if pig_id not in information_with[frame_id]:
                    transformed[pig_id][frame_id] =copy.deepcopy(key_list)
                else:
                    transformed[pig_id][frame_id]= copy.deepcopy(information_with[frame_id][pig_id]) 
                
                for key in key_list.keys() : #information_with[frame_id][pig_id].keys():
                    #if True: #key!="bbox":
                    #transformed[pig_id][frame_id][key+"-cumul"] = [transformed[pig_id][frame_id][key]]
                    if int(frame_id)==0:
                        transformed[pig_id][frame_id][key+"-cumul"] = []
                    #if int(frame_id)>0:
                    #    if frame_id in transformed[pig_id].keys():
                    #        transformed[pig_id][frame_id][key+"-cumul"] = transformed[pig_id][str(int(frame_id)-1)][key+"-cumul"] + [transformed[pig_id][frame_id][key]]
                    #    else:
                    else:"""
                           
                if int(frame_id)>sequence_lenght:
                    
                    for key in key_list.keys():
                        if "cumul" not in key  :
                            transformed[pig_id][frame_id][key+"-cumul"] = [transformed[pig_id][str(int(frame_i))][key] for frame_i in range(int(frame_id)-sequence_lenght+1,int(frame_id)+1 ) ] #+ [transformed[pig_id][frame_id][key]]
                            #transformed[pig_id][frame_id][key+"-cumul"] = transformed[pig_id][frame_id][key+"-cumul"][-sequence_lenght:]
                            tmp= [x for x in  transformed[pig_id][frame_id][key+"-cumul"][-sequence_lenght:] if x is not None]
                            transformed[pig_id][frame_id][key+"-cumul-avg"] = np.mean(tmp )
                            transformed[pig_id][frame_id][key+"-cumul-var"] = np.var(tmp , ddof=1)
                    adh_i = round(transformed[pig_id][frame_id]['adherence-cumul-avg'],1)
                    if adh_i> adh_index_percent:
                            behaviours[frame_id][pig_id]={}
                            for key in transformed[pig_id][frame_id].keys():
                                if 'cumul-' in key:
                                    behaviours[frame_id][pig_id][key] = transformed[pig_id][frame_id][key]
                            behaviours[frame_id][pig_id].update({'behaviour':"(i="+str(adh_i)+":"})
                                                                                            #+str(speed_avg)+","+str(acc_avg)+","+str(speed_var)+","+str(acc_var)+
                                                                                            #"-1:"+str(speed1_avg)+","+str(acc1_avg)+","+str(speed1_var)+","+str(acc1_var)+
                                                                                            #"-2:"+str(speed2_avg)+","+str(acc2_avg)+","+str(speed2_var)+","+str(acc2_var)+")" })
                    
                
    #return information_with
    #adh_index_th = adh_index_percent * sequence_lenght
    """behaviours={}
    for frame_id, frame_info in information_with.items():
        behaviours[frame_id]={}
        for pig_id, pig_info in frame_info.items():
            if 'and' in pig_id:
                information_with[frame_id][pig_id].update(transformed[pig_id][frame_id])  #transformed[pig_id][frame_id] #
                if int(frame_id)>sequence_lenght:
                    
                    adh_i = round(information_with[frame_id][pig_id]['adherence-cumul-avg'],1)
                    speed_avg = round(information_with[frame_id][pig_id]['speed-cumul-avg'],1)
                    acc_avg = round(information_with[frame_id][pig_id]['acceleration-cumul-avg'],1)
                    speed_var = round(information_with[frame_id][pig_id]['speed-cumul-var'],1)
                    acc_var = round(information_with[frame_id][pig_id]['acceleration-cumul-var'],1)
                    
                    speed1_avg = round(information_with[frame_id][pig_id]['speed1-cumul-avg'],1)
                    acc1_avg = round(information_with[frame_id][pig_id]['acceleration1-cumul-avg'],1)
                    speed1_var = round(information_with[frame_id][pig_id]['speed1-cumul-var'],1)
                    acc1_var = round(information_with[frame_id][pig_id]['acceleration1-cumul-var'],1)
                    
                    speed2_avg = round(information_with[frame_id][pig_id]['speed2-cumul-avg'],1)
                    acc2_avg = round(information_with[frame_id][pig_id]['acceleration2-cumul-avg'],1)
                    speed2_var = round(information_with[frame_id][pig_id]['speed2-cumul-var'],1)
                    acc2_var = round(information_with[frame_id][pig_id]['acceleration2-cumul-var'],1)
                    
                    if adh_i> adh_index_percent:
                        behaviours[frame_id][pig_id]={}
                        for key in information_with[frame_id][pig_id].keys():
                            if 'cumul-' in key:
                                behaviours[frame_id][pig_id][key] = information_with[frame_id][pig_id][key]
                        behaviours[frame_id][pig_id].update({'behaviour':"(i="+str(adh_i)+":"})
                                                                                        #+str(speed_avg)+","+str(acc_avg)+","+str(speed_var)+","+str(acc_var)+
                                                                                        #"-1:"+str(speed1_avg)+","+str(acc1_avg)+","+str(speed1_var)+","+str(acc1_var)+
                                                                                        #"-2:"+str(speed2_avg)+","+str(acc2_avg)+","+str(speed2_var)+","+str(acc2_var)+")" })
                    #else:
                    #   behaviours[frame_id][pig_id].update({"behavioue": '<index threshold'}) 
    """
    return behaviours# information_with
        
    

def add_rectangle_on_frame(frame, coordinates, title):
    """_summary_

    Args:
        frame (_type_): _description_
        coordinates (_type_): in x0, y0, w, h 
        text (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Add a rectangle to the frame
    rectangle_color = (0, 255, 0)  # Green color
    rectangle_thickness = 2
    coordinates = [int(i) for i in coordinates]
    cv2.rectangle(frame, (coordinates[0], coordinates[1]), (coordinates[0]+coordinates[2], coordinates[1]+coordinates[3]), rectangle_color, rectangle_thickness)

    # Add a title to the frame
    
    title_position = (coordinates[0], coordinates[1]-2)
    title_font = 0# cv2.FONT_HERSHEY_SIMPLEX
    title_font_scale = 0.6  
    title_color = (0, 255, 0)  # Green color
    cv2.putText(frame, title, title_position, title_font, title_font_scale, title_color, rectangle_thickness, cv2.LINE_AA)
    return frame 

def read_video_mot(video_file, annotations,fps=None):
    annotated_video_file = video_file.split(".mp4")[0]+'_with_id.mp4'
    cap = cv2.VideoCapture(video_file)
    # Check if the video file was opened successfully
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    if fps is None:
        fps = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # You can change the codec as needed
    out = cv2.VideoWriter(annotated_video_file, fourcc, fps, (frame_width, frame_height))

    if not cap.isOpened():
        print("Error: Could not open video file.")
        exit()

    frame_id=0
    while True:
        # Read a frame from the video
        ret, frame = cap.read()
        
        # Check if the video has ended
        if not ret :
            break
        
        if frame_id in annotations.keys() or str(frame_id) in annotations.keys():
            print("frame_id",frame_id)
            for pig_id,pig  in annotations[str(frame_id)].items():
                if True: #pig["isGroundTruth"]==True and pig["behaviour"]=="fight":
                    coordinates = [pig["bbox"]["x"],pig["bbox"]["y"], pig["bbox"]["width"], pig["bbox"]["height"]]
                    if 'behaviour' in pig.keys():
                        behaviour = pig["behaviour"]
                    else:
                        behaviour=""
                    frame= add_rectangle_on_frame(frame, coordinates, str(pig_id)+" :"+str(pig ["confidence"]))#+behaviour)
        
            out.write(frame)
        frame_id+=1
        # Process the frame (you can do whatever you want with it here)
        # For example, you can display the frame
        # cv2.imshow('Video', frame)
        # Exit when 'q' key is pressed
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #   break
    # Release the video capture object and close any windows
    #cap.release()
    out.release()

    cv2.destroyAllWindows()

        