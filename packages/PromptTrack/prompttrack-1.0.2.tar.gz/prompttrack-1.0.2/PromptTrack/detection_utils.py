import torch
print(torch.cuda.is_available())
from PIL import Image
import requests
import torchvision.transforms as T
import matplotlib.pyplot as plt
from collections import defaultdict
import torch.nn.functional as F
import numpy as np
from skimage.measure import find_contours

from matplotlib import patches,  lines
from matplotlib.patches import Polygon
from nms import nms , malisiewicz, fast
from transformers import Owlv2Processor, Owlv2ForObjectDetection

torch.set_grad_enabled(False)





# standard PyTorch mean-std input image normalization
transform = T.Compose([
    T.Resize(800),
    T.ToTensor(),
    T.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# for output bounding box post-processing
def box_cxcywh_to_xyxy(x):
    x_c, y_c, w, h = x.unbind(1)
    b = [(x_c - 0.5 * w), (y_c - 0.5 * h),
         (x_c + 0.5 * w), (y_c + 0.5 * h)]
    return torch.stack(b, dim=1)

def rescale_bboxes(out_bbox, size):
    img_w, img_h = size
    b = box_cxcywh_to_xyxy(out_bbox)
    b = b * torch.tensor([img_w, img_h, img_w, img_h], dtype=torch.float32)
    return b



# colors for visualization
COLORS = [[0.000, 0.447, 0.741], [0.850, 0.325, 0.098], [0.929, 0.694, 0.125],
          [0.494, 0.184, 0.556], [0.466, 0.674, 0.188], [0.301, 0.745, 0.933]]

def apply_mask(image, mask, color, alpha=0.5):
    """Apply the given mask to the image.
    """
    for c in range(3):
        image[:, :, c] = np.where(mask == 1,
                                  image[:, :, c] *
                                  (1 - alpha) + alpha * color[c] * 255,
                                  image[:, :, c])
    return image

def plot_results(pil_img, scores, boxes, labels, masks=None):
    plt.figure(figsize=(16,10))
    np_image = np.array(pil_img)
    ax = plt.gca()
    colors = COLORS * 100
    if masks is None:
      masks = [None for _ in range(len(scores))]
    assert len(scores) == len(boxes) == len(labels) == len(masks)
    for s, (xmin, ymin, xmax, ymax), l, mask, c in zip(scores, boxes.tolist(), labels, masks, colors):
        ax.add_patch(plt.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin,
                                   fill=False, color=c, linewidth=3))
        text = f'{l}: {s:0.2f}'
        ax.text(xmin, ymin, text, fontsize=15, bbox=dict(facecolor='white', alpha=0.8))

        if mask is None:
          continue
        np_image = apply_mask(np_image, mask, c)

        padded_mask = np.zeros((mask.shape[0] + 2, mask.shape[1] + 2), dtype=np.uint8)
        padded_mask[1:-1, 1:-1] = mask
        contours = find_contours(padded_mask, 0.5)
        for verts in contours:
          # Subtract the padding and flip (y, x) to (x, y)
          verts = np.fliplr(verts) - 1
          p = Polygon(verts, facecolor="none", edgecolor=c)
          ax.add_patch(p)


    plt.imshow(np_image)
    plt.axis('off')
    plt.show()


def add_res(results, ax, color='green'):
    #for tt in results.values():
    if True:
        bboxes = results['boxes']
        labels = results['labels']
        scores = results['scores']
        #keep = scores >= 0.0
        #bboxes = bboxes[keep].tolist()
        #labels = labels[keep].tolist()
        #scores = scores[keep].tolist()
    #print(torchvision.ops.box_iou(tt['boxes'].cpu().detach(), torch.as_tensor([[xmin, ymin, xmax, ymax]])))
    
    colors = ['purple', 'yellow', 'red', 'green', 'orange', 'pink']
    
    for i, (b, ll, ss) in enumerate(zip(bboxes, labels, scores)):
        ax.add_patch(plt.Rectangle((b[0], b[1]), b[2] - b[0], b[3] - b[1], fill=False, color=colors[i], linewidth=3))
        cls_name = ll if isinstance(ll,str) else CLASSES[ll]
        text = f'{cls_name}: {ss:.2f}'
        print(text)
        ax.text(b[0], b[1], text, fontsize=15, bbox=dict(facecolor='white', alpha=0.8))
        
        
        





def get_inference(im_or, caption="pigs",nms_threshold=0.8,detector="OWL-VITV2", detection_threshold=0.5):
  # propagate through the model
  if detector.lower()=="mdetr":
    im=Image.fromarray(im_or)
    # mean-std normalize the input image (batch-size: 1)
    img = transform(im).unsqueeze(0)
    if torch.cuda.is_available():
      img = img.cuda()
      
    model, postprocessor = torch.hub.load('ashkamath/mdetr:main', 'mdetr_efficientnetB5', pretrained=True, return_postprocessor=True, trust_repo=True)
    if torch.cuda.is_available():
      model = model.cuda()
    model.eval();
    memory_cache = model(img, [caption], encode_and_save=True)
    outputs = model(img, [caption], encode_and_save=False, memory_cache=memory_cache)
      # keep only predictions with 0.7+ confidence
    probas = 1 - outputs['pred_logits'].softmax(-1)[0, :, -1].cpu()
    keep = (probas > detection_threshold).cpu()
    
    bboxes_scaled1 = rescale_bboxes(outputs['pred_boxes'].cpu()[0, :], im.size)
    areas = np.array([(box[2]-box[0] )* (box[3]-box[1]) for box in bboxes_scaled1])
    
    #filtrage sur l'aire 
    """area_filtered = (8000< areas) & ( areas<90000)
    keep = keep &  area_filtered
    """
    ############NMS
    bboxes_scaled_tlw= [[int(box[0]),int(box[1]), int(box[2]-box[0]), int(box[3]-box[1]) ]   for box in bboxes_scaled1]
    best_keep_nms = nms.boxes(bboxes_scaled_tlw, probas, nms_algorithm=fast.nms, nms_threshold=nms_threshold)
    best_keep_nms = np.array( [ True if (idx in best_keep_nms) else False for idx, i in enumerate(keep) ] )
    
    keep =keep & best_keep_nms
    bboxes_scaled = rescale_bboxes(outputs['pred_boxes'].cpu()[0, keep], im.size)
    
    # Extract the text spans predicted by each box
    positive_tokens = (outputs["pred_logits"].cpu()[0, keep].softmax(-1) > 0.1).nonzero().tolist()
    predicted_spans = defaultdict(str)
    for tok in positive_tokens:
      item, pos = tok
      if pos < 255:
          span = memory_cache["tokenized"].token_to_chars(0, pos)
          predicted_spans [item] += " " + caption[span.start:span.end]

    labels = [predicted_spans [k] for k in sorted(list(predicted_spans .keys()))]
    
  if detector.lower()=="owl-vitv2":
    processor = Owlv2Processor.from_pretrained("google/owlv2-large-patch14-ensemble")
    model = Owlv2ForObjectDetection.from_pretrained("google/owlv2-large-patch14-ensemble")
    image = im=Image.fromarray(im_or)
    texts = [caption.split(",")]
    inputs = processor(text=texts, images=image, return_tensors="pt")
    if torch.cuda.is_available():
      model = model.cuda()
      inputs = {key: val.to("cuda") for key, val in inputs.items()}
    outputs = model(**inputs)
    # Target image sizes (height, width) to rescale box predictions [batch_size, 2]
    target_sizes = torch.Tensor([image.size[::-1]])
    # Convert outputs (bounding boxes and class logits) to Pascal VOC Format (xmin, ymin, xmax, ymax)
    results = processor.post_process_object_detection(outputs=outputs, target_sizes=target_sizes, threshold=0.1)
    i = 0  # Retrieve predictions for the first image for the corresponding text queries
    text = texts[i]
    boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]
    for box, score, label in zip(boxes, scores, labels):
        box = [round(i, 2) for i in box.tolist()]
        print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")
    probas=scores
    keep  = (probas > detection_threshold).cpu()
    bboxes_scaled=boxes[keep]
    #print(keep)

  else:
    raise ValueError("Value unaccept,value accepted are only: mdetr and OWL-VITV2")
    

  detection_bboxes = []
  detection_confidences = []
  detection_class_ids = []

  for idx, detection in enumerate(bboxes_scaled):
    if True: #detection[3]>100 (constraint for the pig dataset):# True: #8000<(detection[2]-detection[0])*(detection[3]-detection[1])<40000: # on filtre l'aire des 
      detection =detection.tolist()
      detection = [detection[0], detection[1], detection[2]-detection[0], detection[3]-detection[1]]
      #detection = to_elements(detection)
      detection_bboxes.append(detection)
      detection_confidences .append(probas[keep][idx].item())
      detection_class_ids  .append(1) #(labels[idx])
  
  return detection_bboxes, detection_confidences,detection_class_ids
  #plot_results(im, probas[keep], bboxes_scaled, labels)


