import torch
import numpy as np 
import json 
import cv2
from PromptTrack.tracker.byte_tracker import BYTETracker

"""from PromptTrack import Object_detection 
from Object_detection import get_inference"""
from PromptTrack.detection_utils  import get_inference
from PromptTrack.utils import read_video_mot
from PromptTrack.utils import xyxy_to_xywh 
from PromptTrack.utils import xywh_to_xyxy


#from utils import read_video_mot
#sys.path.append('/home/sophie/aggression_detection')
"""# Get the current script's directory
current_dir = os.path.dirname(os.path.realpath(__file__))
# Get the grandparent directory's path
grandparent_dir = os.path.abspath(os.path.join(current_dir, "../"))
# Add the grandparent directory to sys.path
sys.path.append(grandparent_dir)

# Now you can perform a relative import
"""


class PromptTracker():
    def __init__(self):
        self.track_thresh= 0
        self.match_thresh = 1
        self.frame_rate=25
        self.track_buffer = 10000
        self.max_time_lost= 10000
        print("")
        
    def process_a_frame(self,frame, frame_id, prompt="pigs",nms_threshold=0.8,detector="OWL-VITV2",detection_threshold=0):
        """ provide detection on each frame from the prompt and the selected zero-shot detector

        Args:
            frame (rgb image): image in numpy array
            frame_id (integer): the id of the frame in the video
            prompt (string): the text prompt
            detector (string) : name of the model you would like to use as detector

        Returns:
            dictionnary: dictionnary of detected object grouped by frames used as keys
        """
        return {frame_id: [get_inference(frame, prompt,nms_threshold,detection_threshold=detection_threshold )]}


    # Define a function for processing a single frame
    """def process_frame(self, frame, frame_id, result_queue):
        # Your frame processing code goes here
        # For example, you can perform some image processing on the frame
        print(frame_id, "\n")
        processed_frame = {frame_id: [get_inference(frame)]}
        result_queue.put(processed_frame)"""




    def detect_objects(self,  video_file, prompt="pigs",nms_threshold=0.8,detection_threshold=0 ,detector="OWL-VITV2"):
        processed_frames = []
        video_capture = cv2.VideoCapture(video_file)  # Replace with your video file path
        frame_id=0
        while True:
            ret, frame = video_capture.read()

            if not ret :#or frame_id==300:
                break
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            processed_frame = self.process_a_frame (frame, frame_id, prompt,nms_threshold,detection_threshold=detection_threshold,detector="OWL-VITV2") 
            processed_frames.append(processed_frame)
            frame_id+=1
            print("detections on frame id", frame_id)

        def key_function(item):
            return list(item.keys())[0]

        # Use argsort with the custom key function to sort the array
        sorted_indices = np.argsort(np.array([key_function(item) for item in processed_frames]))
        sorted_processed_frames = np.array(processed_frames)[sorted_indices]
        sorted_processed_frames= sorted_processed_frames.tolist()
        
        
        object_detection_file =video_file.split(".mp4")[0]+'_object_detection.json'
        with open(object_detection_file, 'w') as file:
            print('dumping the file')
            json.dump(sorted_processed_frames , file)

    def process_mot(self, video_file, fixed_parc=True, nbr_items=15, track_thresh=0, match_thresh=1, frame_rate=25, track_buffer=10000, max_time_lost=100,nbr_frames_fixing=10):
        """
        remplacer par Bytetrack qui a été crée avec des librairies existantes
        Args:
            video_file (str, optional): _description_. Defaults to "/home/sophie/aggression_detection/annotated/2019_11_22/000010/color.mp4".
        """
        self.track_thresh = track_thresh
        self.match_thresh = match_thresh
        self.frame_rate=frame_rate
        self.track_buffer = track_buffer
        self.max_time_lost= max_time_lost
        if fixed_parc ==False:
                nbr_items =float("inf")
                
        object_detection_file =video_file.split(".mp4")[0]+'_object_detection.json'
        with open(object_detection_file, "r") as file:
            # Parse the JSON data
            sorted_processed_frames = json.load(file)
        
        
        
        bytetracker = BYTETracker(track_thresh=self.track_thresh, fixed_parc=fixed_parc, track_buffer=self.track_buffer, match_thresh=self.match_thresh, frame_rate=frame_rate,max_time_lost=max_time_lost,nbr_frames_fixing=nbr_frames_fixing)  # j'oblige le modèle à faire matcher à de id existant ***mais ca ne marche pas *** 
        #bytetracker.max_time_lost = self.max_time_lost
        track_over_time={}
        #tracker = CentroidTracker(max_lost=180) # or IOUTracker(...), CentroidKF_Tracker(...), SORT(...)
        for detection_dictionnary  in sorted_processed_frames:
            frame_id = int(list(detection_dictionnary.keys())[0])
            
            detection_bboxes, detection_confidences, detection_class_ids = list(detection_dictionnary.values())[0][0]
            detection_with_score=[]
            for idx, box in enumerate(detection_bboxes):
                box = xywh_to_xyxy(box)
                box = list(box)
                box.append(detection_confidences[idx])
                box.append(torch.tensor(detection_class_ids[idx]))
                detection_with_score.append(np.array(box))
            #######
            
            
            """for track in bytetracker.tracked_stracks:
                    if track.track_id>nbr_items:
                        bytetracker.tracked_stracks.remove(track)"""
                

            
            
            #########
            if len(detection_bboxes)!=0:
                detection_with_score =torch.tensor(detection_with_score)
                online_targets = bytetracker.update( detection_with_score, [1,1])
                #output_tracks = tracker.update(detection_bboxes, detection_confidences, detection_class_ids)
                track_over_time[frame_id]={}
                for track in online_targets : # idx, track in enumerate(detection_bboxes): # output_tracks:
                    #track=[0,idx,track[0], track[1], track[2], track[3]]
                    #frame, id, bb_left, bb_top, bb_width, bb_height, confidence, x, y, z = track
                    #assert len(track) == 10
                    #print(track)
                    track_id = track.infos['track_id']#[4]
                    if track_id<nbr_items:
                        x, y, w, h =  track.infos['location']#xyxy_to_xywh(track[:4])
                        track_over_time[frame_id][track_id] = {"bbox":{'x':x, 'y':y, 'width':w, 'height':h},"confidence":round(track.infos["detection_score"],2)}#[6],2) }
            else:
                track_over_time[frame_id]={}
                
        tracking_file =video_file.split(".mp4")[0]+'_mot_.json'
        with open(tracking_file, 'w') as file:
            json.dump(track_over_time , file)

    
    
    

    def read_video_with_mot(self,video_file,fps=None):
        mot_file =video_file.split(".mp4")[0]+'_mot_.json'
        with open(mot_file, "r") as file:
            # Parse the JSON data
            tracks = json.load(file)    
        read_video_mot(video_file, tracks,fps=fps)

    #video_file = "/home/sophie/aggression_detection/annotated/2019_11_22/000010/color.mp4"

    