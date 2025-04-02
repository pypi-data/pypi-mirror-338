# author:    Kieran McVeigh
# website:   http://www.bklynhlth.com
import numpy as np
import pandas as pd
import os
import json
import logging

import cv2
from deepface import DeepFace
from dataclasses import dataclass, field
from sklearn.cluster import KMeans

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger()

@dataclass
class FaceData:
    face: np.ndarray = field(default_factory=lambda: np.array([]), repr=False)
    face_embedding: list = field(default_factory=list)
    bb_x: int = 0
    bb_y: int = 0
    bb_w: int = 0
    bb_h: int = 0
    right_eye_x: int = 0
    right_eye_y: int = 0
    left_eye_x: int = 0
    left_eye_y: int = 0
    confidence: float = 0.0
    frame_idx: int = -1

    def __post_init__(self):
        if not isinstance(self.face, np.ndarray):
            raise ValueError("Face must be a numpy ndarray.")

    def to_dict(self, keep_face_image=False):
        """
        ---------------------------------------------------------------------------------------------------

        This function converts the FaceData object to a dictionary.

        Parameters:
        ............
        keep_face_image : bool
            Whether to include the face image in the dictionary.

        Returns:
        ............
        facedata_dict : dict
            Dictionary representation of the FaceData object.
        """
        facedata_dict = {
            'face': self.face if keep_face_image else np.array([]),
            'face_embedding': self.face_embedding,
            'bb_x': self.bb_x,
            'bb_y': self.bb_y,
            'bb_w': self.bb_w,
            'bb_h': self.bb_h,
            'right_eye_x': self.right_eye_x,
            'right_eye_y': self.right_eye_y,
            'left_eye_x': self.left_eye_x,
            'left_eye_y': self.left_eye_y,
            'confidence': self.confidence,
            'frame_idx': self.frame_idx
        }
        return facedata_dict

    def set_face_from_image(self, image):
        """
        ---------------------------------------------------------------------------------------------------

        Crops the image using the stored bounding box coordinates and sets the cropped image as the face.
        Also checks to ensure the bounding box does not exceed the dimensions of the image.

        Parameters:
        ............
        image : np.ndarray
            A numpy array representing the entire image from which the face will be cropped.
        """
        if not isinstance(image, np.ndarray):
            raise ValueError("The provided image must be a numpy ndarray.")
        
        if (self.bb_x < 0 or self.bb_y < 0 or 
            self.bb_x + self.bb_w > image.shape[1] or 
            self.bb_y + self.bb_h > image.shape[0]):
            Warning("Bounding box exceeds the limits of the provided image. Setting bounding box to full frame and confidence to 0")

        cropped_image = image[self.bb_y:self.bb_y + self.bb_h, self.bb_x:self.bb_x + self.bb_w]
        self.face = cropped_image

def get_config(filepath, json_file):
    """
    ------------------------------------------------------------------------------------------------------

    This function reads the configuration file containing the column names for the output dataframes,
    and returns the contents of the file as a dictionary.

    Parameters:
    ...........
    filepath : str
        The path to the configuration file.
    json_file : str
        The name of the configuration file.

    Returns:
    ...........
    measures: A dictionary containing the names of the columns in the output dataframes.

    ------------------------------------------------------------------------------------------------------
    """
    dir_name = os.path.dirname(filepath)
    measure_path = os.path.abspath(os.path.join(dir_name, f"config/{json_file}"))

    file = open(measure_path)
    measures = json.load(file)
    return measures

def deepface_dict_to_facedata(data_dict, frame_idx):
    """
    ---------------------------------------------------------------------------------------------------

    Converts a dictionary with specific keys into a FaceData object.

    Parameters:
    ............
    data_dict : dict
        A dictionary containing keys for 'face', 'facial_area', and 'confidence'.
    frame_idx : int
        Frame index of the face data.

    Returns:
    ............
    face_data_instance : FaceData
        An instantiated object of FaceData filled with data from the dictionary.

    Raises:
    ............
    KeyError
        If a required key is missing in the dictionary.
    ValueError
        If data types are not as expected.
    ---------------------------------------------------------------------------------------------------
    """
    try:
        face = data_dict['face']
        bb_x = data_dict['facial_area']['x']
        bb_y = data_dict['facial_area']['y']
        bb_w = data_dict['facial_area']['w']
        bb_h = data_dict['facial_area']['h']
        right_eye_x = data_dict['facial_area']['right_eye'][0]
        right_eye_y = data_dict['facial_area']['right_eye'][1]
        left_eye_x = data_dict['facial_area']['left_eye'][0]
        left_eye_y = data_dict['facial_area']['left_eye'][1]
        confidence = data_dict['confidence']

        if not isinstance(face, np.ndarray):
            raise ValueError("The 'face' field must be a numpy ndarray.")

        face_data_instance = FaceData(
            face=face,
            bb_x=bb_x,
            bb_y=bb_y,
            bb_w=bb_w,
            bb_h=bb_h,
            right_eye_x=right_eye_x,
            right_eye_y=right_eye_y,
            left_eye_x=left_eye_x,
            left_eye_y=left_eye_y,
            confidence=confidence,
            frame_idx=frame_idx
        )
        return face_data_instance

    except KeyError as e:
        raise KeyError(f"Missing key in the input dictionary: {e}")
    except ValueError as e:
        raise ValueError(f"Value error: {e}")

def get_config(filepath, json_file):
    """
    ------------------------------------------------------------------------------------------------------

    This function reads the configuration file containing the column names for the output dataframes,
    and returns the contents of the file as a dictionary.

    Parameters:
    ...........
    filepath : str
        The path to the configuration file.
    json_file : str
        The name of the configuration file.

    Returns:
    ...........
    measures: A dictionary containing the names of the columns in the output dataframes.

    ------------------------------------------------------------------------------------------------------
    """
    dir_name = os.path.dirname(filepath)
    measure_path = os.path.abspath(os.path.join(dir_name, f"config/{json_file}"))

    file = open(measure_path)
    measures = json.load(file)
    return measures


def extract_face_rgb(frame, back_end_str, enforce_detection):
    """
    ---------------------------------------------------------------------------------------------------

    Extracts faces from a given frame in RGB format using the DeepFace library.

    Parameters:
    ............
    frame : np.ndarray
        The input frame in BGR format.
    back_end_str : str
        The backend string specifying the face detection model to use.
    enforce_detection : bool
        A boolean flag indicating whether to enforce face detection.

    Returns:
    ............
    faces_detected : list
        A list of dictionaries, where each dictionary represents a detected face.
    ---------------------------------------------------------------------------------------------------
    """
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces_detected = DeepFace.extract_faces(
        frame,
        detector_backend=back_end_str,
        enforce_detection=enforce_detection,
        align=False
    )

    for face in faces_detected:
        face['face'] = np.array([])

    return faces_detected

def extract_face_bgr(frame, back_end_str, enforce_detection, align):
    """
    ---------------------------------------------------------------------------------------------------

    Extracts faces for backends with BGR format using the DeepFace library.

    Parameters:
    ............
    frame : np.ndarray
        The input frame in BGR format.
    back_end_str : str
        The backend string specifying the face detection model to use.
    enforce_detection : bool
        A boolean flag indicating whether to enforce face detection.
    align : bool
        A boolean flag indicating whether to align the face.

    Returns:
    ............
    faces_detected : list
        A list of dictionaries, where each dictionary represents a detected face.
    ---------------------------------------------------------------------------------------------------

    """
    faces_detected = DeepFace.extract_faces(
        frame,
        detector_backend=back_end_str,
        enforce_detection=enforce_detection,
        align=align
    )
    return faces_detected   

def extract_faces(
    frame, 
    frame_idx, 
    rgb_back_ends,
    back_end_str='mtcnn',
    align=True, 
    enforce_detection=False
):
    """
    ---------------------------------------------------------------------------------------------------

    Extracts faces from a given frame using the specified backend and alignment settings.

    Parameters:
    ............
    frame : np.ndarray
        The input frame in BGR format.
    frame_idx : int
        The frame index.
    back_end_str : str
        The backend string specifying the face detection model to use.
    align : bool
        A boolean flag indicating whether to align the face.
    enforce_detection : bool
        A boolean flag indicating whether to enforce face detection.

    Returns:
    ............
    faces_detected : list
        A list of FaceData objects representing detected faces.
    ---------------------------------------------------------------------------------------------------
    
    """
    if back_end_str in rgb_back_ends:
        faces_detected = extract_face_rgb(frame, back_end_str, enforce_detection)
    else:
        faces_detected = extract_face_bgr(frame, back_end_str, enforce_detection, align)

    faces_detected = [deepface_dict_to_facedata(face, frame_idx) for face in faces_detected]
    
    return faces_detected

def prep_face_data_for_embed(facedata_list, frame):
    """
    ---------------------------------------------------------------------------------------------------

    Ensures face data has all necessary components to embed face.

    Parameters:
    ............
    facedata_list : list
        List of FaceData objects.
    frame : np.ndarray
        The input frame in BGR format.

    Returns:
    ............
    facedata_list : list
        List of prepared FaceData objects.
    ---------------------------------------------------------------------------------------------------

    """
    for face_data in facedata_list:
        if face_data.face.shape[0] == 0:
            face_data.set_face_from_image(frame)
    return facedata_list

def embed_faces(face_data_list, model_name='Facenet'):
    """
    ---------------------------------------------------------------------------------------------------

    Embeds faces from a list of FaceData objects using the specified model.

    Parameters:
    ............
    face_data_list : list
        List of FaceData objects.
    model_name : str
        Name of the model to use for embedding.

    Returns:
    ............
    face_data_list : list
        List of FaceData objects with embeddings.
    ---------------------------------------------------------------------------------------------------
    
    """
    for face_data in face_data_list:
        deep_face_dict = DeepFace.represent(
            face_data.face,
            detector_backend='skip',
            model_name=model_name
        )
        face_data.face_embedding = deep_face_dict[0]['embedding']
        
        #save memory
        face_data.face = np.array([])

    return face_data_list 

def extract_embed_faces_from_frame(
    frame,
    frame_idx,
    rgb_back_ends,
    detector_backend='mtcnn',
    model_name='Facenet'
):
    """
    ---------------------------------------------------------------------------------------------------

    Extracts and embeds faces from a given frame using the specified backend and model.

    Parameters:
    ............
    frame : np.ndarray
        The input frame in BGR format.
    frame_idx : int
        The frame index.
    detector_backend : str
        The backend string specifying the face detection model to use.
    model_name : str
        Name of the model to use for embedding.

    Returns:
    ............
    face_data_list : list
        List of FaceData objects with embeddings.
    ---------------------------------------------------------------------------------------------------
    """
    try:
        face_data_list = extract_faces(
            frame,
            frame_idx,
            rgb_back_ends,
            back_end_str=detector_backend
        )

        face_data_list = prep_face_data_for_embed(face_data_list, frame)
        face_data_list = embed_faces(face_data_list, model_name=model_name)
    except Exception as e:
        logger.info(f"Error extracting and embedding faces: {e}, frame_idx: {frame_idx}")
        face_data_list = [FaceData()]
    return face_data_list

def load_facedata_from_video(
    video_path,
    rgb_back_ends,
    detector_backend='mtcnn',
    model_name='Facenet', 
    n_frames=np.inf, 
    capture_n_per_sec=3
):
    """
    ---------------------------------------------------------------------------------------------------

    Load video frames from a given video file, capturing only a specified
    number of frames per second.

    Parameters:
    ............
        video_path (str): Path to the video file.
        n_frames (int, optional): Maximum number of frames to capture. Defaults to np.inf.
        capture_n_per_sec (int, optional): Number of frames to capture per second. Defaults to 30.

    Returns:
    ............
        tuple: A tuple containing the list of captured frames, the list of their corresponding frame indices,
               and the frames per second (fps) of the video.
    ---------------------------------------------------------------------------------------------------
           
    """
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError(f"Error opening video file: {video_path}")
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    if capture_n_per_sec > fps:
        raise ValueError(f"Capture rate per second cannot exceed the video's frames per second, video fps: {fps}")

    num_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    n_skip = round(fps / capture_n_per_sec)
    facedata_list = []

    frame_index = 0
    n_frames_capture = 0

    while True:

        ret, frame = cap.read()
        if not ret:
            break

        if (frame_index % n_skip) == 0:
            frame_facedata = extract_embed_faces_from_frame(
                frame,
                frame_index, 
                rgb_back_ends,
                detector_backend=detector_backend,
                model_name=model_name
            )
            facedata_list.extend(frame_facedata)

            n_frames_capture += 1

        frame_index += 1

        if n_frames_capture >= n_frames:
            num_frames = n_frames * n_skip
            break

    cap.release()
    return facedata_list, fps, num_frames


def facedata_list_to_df(facedata_list):
    """
    ---------------------------------------------------------------------------------------------------

    Converts a list of FaceData objects to a pandas DataFrame.

    Parameters:
    ............
    facedata_list : list
        List of FaceData objects.

    Returns:
    ............
    facedata_df : pandas.DataFrame
        DataFrame containing the data from the FaceData objects.
    ---------------------------------------------------------------------------------------------------
    """
    facedata_dict_list = [facedata.to_dict() for facedata in facedata_list]
    facedata_df = pd.DataFrame(facedata_dict_list)
    facedata_df['cluster'] = -1
    return facedata_df

def cluster_embeddings(facedata_df, confidence_threshold=0.7, n_clusters=2):
    """
    ---------------------------------------------------------------------------------------------------
    This function clusters face embeddings based on confidence threshold and number of clusters.

    Parameters:
    ............
    facedata_df : pandas.DataFrame
        DataFrame containing face data.
    confidence_threshold : float
        Confidence threshold for face data.
    n_clusters : int
        Number of clusters to create.

    Returns:
    ............
    facedata_df : pandas.DataFrame
        DataFrame with cluster assignments for each face.
    ---------------------------------------------------------------------------------------------------
    
    """

    threshold_bools = facedata_df['confidence'] > confidence_threshold
    thresholded_facedata_df = facedata_df[threshold_bools]
    cluster_model = KMeans(n_clusters=n_clusters)
    cluster_assignments = cluster_model.fit_predict(
        np.vstack(thresholded_facedata_df['face_embedding'])
    )
    facedata_df.loc[threshold_bools, 'cluster'] = cluster_assignments
    return facedata_df

def cluster_facedata(
    face_data_across_frames,
    threshold,
    n_clusters=2
):
    """
    ---------------------------------------------------------------------------------------------------

    Clusters the face data across frames using embeddings.

    Parameters:
    ............
        face_data_across_frames (list): A list of face data across frames.
        threshold (float): The confidence threshold for clustering.
        n_clusters (int, optional): The number of clusters to create. Defaults to 2.

    Returns:
    ............
        pandas.DataFrame: The clustered face data.
    ---------------------------------------------------------------------------------------------------

    """
    facedata_df = facedata_list_to_df(
        face_data_across_frames
    )

    facedata_df = cluster_embeddings(
        facedata_df,
        confidence_threshold=threshold,
        n_clusters=n_clusters
    )

    return facedata_df

def create_single_face_output(
        cluster_df: pd.DataFrame, 
        min_frames_face_present: int,
        frames_per_row: int,
        fps: int,
        bbox_cols: list,
        interpolate=True
    ):
    """
    ---------------------------------------------------------------------------------------------------

    Identifies the frame indices in clusters where the number of frames is below a specified minimum threshold.

    Parameters:
    ............
    cluster_df : pandas.DataFrame
        DataFrame containing face cluster information with columns 'cluster_presences' and 'frame_idx'.
    min_frames_face_present : int
        Minimum number of frames required for a face to be considered present.
    frames_per_row : int
        Number of frames per row.
    fps : int
        Frames per second of the video.
    bbox_cols : list
        List of column names for the bounding box data.
    interpolate : bool
        Whether to interpolate missing values in the bounding box data.

    Returns:
    ............
    frame_idx_not_meeting_min : list
        List of frame indices that do not meet the minimum threshold.
    ---------------------------------------------------------------------------------------------------
    """
    interpolated_section_dfs = []
    cluster_df['cluster_presences'] = np.cumsum(
        cluster_df.sample_time.diff() > ((frames_per_row / fps)*1.5) # 1.5 is hacky but just gives rounding room for fps and frames per row
    )

    for _, presence_df in cluster_df.groupby('cluster_presences'):
        n_frames_present = len(presence_df) * frames_per_row
        if n_frames_present > min_frames_face_present:

            max_frame = presence_df.frame_idx.max()
            min_frame = presence_df.frame_idx.min()
            frames_in_clusters = list(range(min_frame, max_frame))
            upsampled_df = pd.DataFrame(frames_in_clusters, columns=['frame_idx'])
            bb_dict_df = presence_df[bbox_cols]

            merged_bb_df = upsampled_df.merge(
                bb_dict_df,
                how='outer',
                on='frame_idx'
            )
            if interpolate:
                interpolated_df = merged_bb_df.interpolate()
            else:
                interpolated_df = merged_bb_df.ffill()

            interpolated_section_dfs.append(interpolated_df)
    
    if len(interpolated_section_dfs) == 0:
        return pd.DataFrame(columns=bbox_cols)
    
    df_for_all_presences = pd.concat(interpolated_section_dfs)

    return df_for_all_presences


def prep_face_clusters_for_output(
    facedata_df, 
    min_frames_face_present, 
    capture_n_frames_per_second,
    fps,
    num_frames_vid,
    n_clusters,
    bbox_cols,
    interpolate=True
):
    """
    ---------------------------------------------------------------------------------------------------

    Filters and prepares face clusters for output.

    Parameters:
    ............
        facedata_df (pandas.DataFrame): The DataFrame containing face data.
        min_frames_face_present (int): The minimum number of frames a face must be present in a cluster.
        frames_per_row (int): The number of frames per row.
        fps (int): The frames per second of the video.
        num_frames_vid (int): The total number of frames in the video.
        n_clusters (int): The number of clusters.
        bbox_cols (list): The list of column names for the bounding box data.
        interpolate (bool): Whether to interpolate missing values in the bounding box data.

    Returns:
    ............
        dict: A dictionary containing face bounding box lists for each cluster.
    ---------------------------------------------------------------------------------------------------

    """
    
    facedata_df['sample_time']=facedata_df['frame_idx']/fps
    frames_per_row = round(fps/capture_n_frames_per_second)

    face_list_dict = {}
    for cluster_idx in range(n_clusters):
        out_df = pd.DataFrame(range(num_frames_vid),columns=['frame_idx'])
        cluster_df = facedata_df.loc[
            facedata_df.cluster==cluster_idx
        ]
        
        face_bbox_df = create_single_face_output(
            cluster_df,
            min_frames_face_present,
            frames_per_row,
            fps,
            bbox_cols,
            interpolate=interpolate
        )
        
        out_df = out_df.merge(
            face_bbox_df,
            how='outer',
            on='frame_idx'
        )

        bbox_df = out_df[bbox_cols].applymap(
            lambda x:int(x) if not pd.isna(x) else x
        )

        face_bbox_list = bbox_df.to_dict(orient='records')

        face_list_dict[cluster_idx] = face_bbox_list

    return face_list_dict

def preprocess_face_video(
    video_path,  
    n_people=2,
    capture_n_frames_per_second=3,
    model_name='Facenet',
    detector_backend='mtcnn', 
    face_threshold=.95, 
    min_sec_face_present=3, 
    n_frames=np.inf,
    interpolate=True
):
    """
    Preprocesses a face video by extracting face data, clustering the faces, and preparing the output.

    Parameters:
    - video_path (str): Path to the input video file.
    - n_people (int): Number of people in video used to set number of clusters to create. Default is 2, assuming this is a clinical interview.
    - capture_n_frames_per_second (int): Number of frames to capture per second. Increasing this parameter should increase the quality of clustering but will cause the function to run for longer. Default is 2.
    - model_name (str): Name of the face recognition model to use. Default is 'Facenet'.
    - detector_backend (str): Backend to use for face detection. Can be any model used in the Deepface library. Default is 'mtcnn'.
    - face_threshold (float): Similarity threshold for identifying faces. Default is 0.95.
    - min_sec_face_present (int): Minimum number of seconds a face must be present after clustering to not be filtered out. Default is 3.
    - n_frames (int): Maximum number of frames to process. Default is np.inf (i.e. process all frames).
    - interpolate (bool): Whether to interpolate missing values in the bounding box data. Default is True.
   
    Returns:
    - bb_dict (dict): Dictionary containing the framewise bounding boxes for each face of n_people in video. keys are zero indexed n_people integers.
    - facedata_df (pandas.DataFrame): DataFrame containing the face data and cluster info.
    """

    config = get_config(os.path.abspath(__file__), 'preprocess.json')

    bb_dict = {}
    facedata_df = pd.DataFrame()
    bbox_cols=config["bbox_dict_cols"]

    try:
        face_data_across_frames, fps, num_frames_vid = load_facedata_from_video(
            video_path,
            config['rgb_back_ends'],
            n_frames=n_frames,
            capture_n_per_sec=capture_n_frames_per_second,
            detector_backend=detector_backend,
            model_name=model_name
        )

        facedata_df = cluster_facedata(
            face_data_across_frames,
            face_threshold,
            n_clusters=n_people
        )

        min_frames_face_present = fps * min_sec_face_present
        bb_dict = prep_face_clusters_for_output(
            facedata_df, 
            min_frames_face_present, 
            capture_n_frames_per_second,
            fps,
            num_frames_vid,
            n_people,
            bbox_cols=bbox_cols,
            interpolate=interpolate
        )

    except Exception as e:
        logger.info(f"Error preprocessing video: file: {video_path} & Error: {e}'")
        
    return  bb_dict, facedata_df
